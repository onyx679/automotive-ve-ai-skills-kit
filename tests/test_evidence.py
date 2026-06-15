import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ve_ai_skills_kit.evidence import EvidenceClaim, render_evidence_matrix, summarize_claims


class EvidenceClaimTest(unittest.TestCase):
    def test_verified_claim_is_resume_ready(self):
        claim = EvidenceClaim(
            claim="Published project",
            source_kind="repository-artifact",
            evidence_level="L4",
            verdict="confirmed",
            evidence_status="verified",
            evidence_url="https://example.com/repo",
            resume_wording="Published an open-source project with CI",
            boundary="Portfolio project only",
        )

        self.assertEqual(claim.claim_level, "resume-ready")
        self.assertEqual(claim.risk_flags, [])

    def test_open_pr_requires_boundary_wording(self):
        claim = EvidenceClaim(
            claim="Submitted upstream PR",
            source_kind="platform-record",
            evidence_level="L4",
            verdict="confirmed",
            evidence_status="open",
            evidence_url="https://example.com/pull/1",
            resume_wording="Submitted PR #1 for review",
            boundary="Open PR; do not claim merged",
        )

        self.assertEqual(claim.claim_level, "boundary-only")

    def test_overclaimed_open_pr_is_blocked(self):
        claim = EvidenceClaim(
            claim="Contributor status",
            source_kind="platform-record",
            evidence_level="L4",
            verdict="confirmed",
            evidence_status="open",
            evidence_url="https://example.com/pull/1",
            resume_wording="Became contributor after merged PR",
            boundary="Open PR",
        )

        self.assertEqual(claim.claim_level, "do-not-claim")
        self.assertIn("unsupported-completion-wording", claim.risk_flags)

    def test_verified_claim_with_weak_evidence_is_blocked(self):
        claim = EvidenceClaim(
            claim="Reported impact",
            source_kind="self-reported",
            evidence_level="L1",
            verdict="confirmed",
            evidence_status="verified",
            evidence_url="https://example.com/blog",
            resume_wording="Verified a 40 percent impact",
            boundary="Self-reported only",
        )

        self.assertEqual(claim.claim_level, "do-not-claim")
        self.assertIn("weak-evidence-level", claim.risk_flags)

    def test_verified_claim_with_doubtful_verdict_is_blocked(self):
        claim = EvidenceClaim(
            claim="Reported impact",
            source_kind="platform-record",
            evidence_level="L4",
            verdict="doubtful",
            evidence_status="verified",
            evidence_url="https://example.com/run",
            resume_wording="Verified a 40 percent impact",
            boundary="Doubtful verdict",
        )

        self.assertEqual(claim.claim_level, "do-not-claim")
        self.assertIn("negative-or-doubtful-verdict", claim.risk_flags)

    def test_report_summarizes_and_lists_do_not_claim_section(self):
        claims = [
            EvidenceClaim("A", "repository-artifact", "L4", "confirmed", "verified", "https://example.com/a", "Published A", "Portfolio only"),
            EvidenceClaim("B", "platform-record", "L4", "confirmed", "open", "https://example.com/b", "Submitted B", "Open PR"),
            EvidenceClaim("C", "platform-record", "L1", "doubtful", "missing", "", "Merged C", ""),
        ]

        self.assertEqual(
            summarize_claims(claims),
            {"total": 3, "resume-ready": 1, "boundary-only": 1, "do-not-claim": 1},
        )

        report = render_evidence_matrix(claims)

        self.assertIn("# Evidence Claim Matrix", report)
        self.assertIn("## Do Not Claim Yet", report)
        self.assertLess(report.index("| C |"), report.index("| B |"))


if __name__ == "__main__":
    unittest.main()
