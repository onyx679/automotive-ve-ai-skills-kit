from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


VERIFIED = "verified"
OPEN = "open"
PENDING_REVIEW = "pending-review"
MISSING = "missing"

EVIDENCE_STATUSES = {VERIFIED, OPEN, PENDING_REVIEW, MISSING}
EVIDENCE_LEVELS = {"L4", "L3", "L2", "L1"}
POSITIVE_VERDICTS = {"confirmed", "largely-credible"}

LEVEL_ORDER = {
    "do-not-claim": 0,
    "boundary-only": 1,
    "resume-ready": 2,
}

OVERCLAIM_TERMS = (
    "accepted",
    "approved",
    "became contributor",
    "contributor",
    "merged",
    "selected",
)


@dataclass(frozen=True)
class EvidenceClaim:
    claim: str
    source_kind: str
    evidence_level: str
    verdict: str
    evidence_status: str
    evidence_url: str
    resume_wording: str
    boundary: str

    @property
    def normalized_status(self) -> str:
        status = self.evidence_status.strip().lower()
        return status if status in EVIDENCE_STATUSES else MISSING

    @property
    def normalized_evidence_level(self) -> str:
        level = self.evidence_level.strip().upper()
        return level if level in EVIDENCE_LEVELS else "L1"

    @property
    def normalized_verdict(self) -> str:
        return self.verdict.strip().lower() or "doubtful"

    @property
    def risk_flags(self) -> list[str]:
        flags: list[str] = []
        if not self.evidence_url.strip():
            flags.append("missing-evidence-url")
        if not self.resume_wording.strip():
            flags.append("missing-safe-wording")
        if self.normalized_status == MISSING:
            flags.append("missing-evidence")
        if self.normalized_status != VERIFIED and self._wording_overclaims_completion():
            flags.append("unsupported-completion-wording")
        if self.normalized_status in {OPEN, PENDING_REVIEW} and not self.boundary.strip():
            flags.append("missing-boundary")
        if self.normalized_status == VERIFIED and self.normalized_evidence_level not in {"L4", "L3"}:
            flags.append("weak-evidence-level")
        if self.normalized_status == VERIFIED and self.normalized_verdict not in POSITIVE_VERDICTS:
            flags.append("negative-or-doubtful-verdict")
        return flags

    @property
    def claim_level(self) -> str:
        if self.risk_flags:
            return "do-not-claim"
        if self.normalized_status == VERIFIED:
            return "resume-ready"
        return "boundary-only"

    def to_markdown_row(self) -> str:
        values = [
            self.claim,
            self.source_kind or "-",
            self.normalized_evidence_level,
            self.normalized_verdict,
            self.normalized_status,
            self.claim_level,
            self.evidence_url or "-",
            self.resume_wording or "-",
            self.boundary or "-",
        ]
        return "| " + " | ".join(_clean_cell(value) for value in values) + " |"

    def _wording_overclaims_completion(self) -> bool:
        wording = self.resume_wording.lower()
        return any(term in wording for term in OVERCLAIM_TERMS)


def claim_from_mapping(row: dict[str, str]) -> EvidenceClaim:
    return EvidenceClaim(
        claim=row.get("claim", "").strip(),
        source_kind=row.get("source_kind", "").strip(),
        evidence_level=row.get("evidence_level", "").strip(),
        verdict=row.get("verdict", "").strip(),
        evidence_status=row.get("evidence_status", "").strip(),
        evidence_url=row.get("evidence_url", "").strip(),
        resume_wording=row.get("resume_wording", "").strip(),
        boundary=row.get("boundary", "").strip(),
    )


def rank_claims(claims: Iterable[EvidenceClaim]) -> list[EvidenceClaim]:
    return sorted(
        claims,
        key=lambda claim: (LEVEL_ORDER[claim.claim_level], claim.claim.lower()),
    )


def summarize_claims(claims: Iterable[EvidenceClaim]) -> dict[str, int]:
    summary = {
        "total": 0,
        "resume-ready": 0,
        "boundary-only": 0,
        "do-not-claim": 0,
    }
    for claim in claims:
        summary["total"] += 1
        summary[claim.claim_level] += 1
    return summary


def render_evidence_matrix(claims: Iterable[EvidenceClaim]) -> str:
    ranked = rank_claims(claims)
    summary = summarize_claims(ranked)
    lines = [
        "# Evidence Claim Matrix",
        "",
        "## Summary",
        "",
        f"- Total claims: {summary['total']}",
        f"- Resume-ready: {summary['resume-ready']}",
        f"- Boundary-only: {summary['boundary-only']}",
        f"- Do-not-claim: {summary['do-not-claim']}",
        "",
        "## Claim Review",
        "",
        "| Claim | Source | Evidence level | Verdict | Status | Claim level | Evidence | Safe wording | Boundary |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    lines.extend(claim.to_markdown_row() for claim in ranked)

    blocked = [claim for claim in ranked if claim.claim_level == "do-not-claim"]
    if blocked:
        lines.extend(["", "## Do Not Claim Yet", ""])
        for claim in blocked:
            flags = ", ".join(claim.risk_flags)
            lines.append(f"- {claim.claim}: {flags}")

    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not describe open PRs as merged, accepted, or contributor status.",
            "- Keep internal deployment, supplier quote, and real BOM claims out unless approved evidence exists.",
            "- Treat L1/self-reported claims as drafting material, not resume-ready proof.",
            "- Prefer conservative wording that names the evidence state.",
        ]
    )
    return "\n".join(lines) + "\n"


def _clean_cell(value: str) -> str:
    return str(value).replace("|", "/").replace("\n", " ").strip()
