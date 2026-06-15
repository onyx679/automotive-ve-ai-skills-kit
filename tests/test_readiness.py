import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ve_ai_skills_kit.readiness import BomQuoteRow, render_readiness_report, summarize_readiness


class BomQuoteReadinessTest(unittest.TestCase):
    def test_missing_required_fields_blocks_skill_run(self):
        row = BomQuoteRow(
            component="Seat bracket",
            supplier="",
            quoted_cost="18.40",
            currency="CNY",
            annual_volume="",
            evidence_source="",
            tax_status="",
            target_cost="17.00",
            material="steel",
            process="stamping",
        )

        self.assertEqual(row.readiness_level, "blocked-missing-required")
        self.assertEqual(
            row.missing_required_fields,
            ["supplier", "annual_volume", "evidence_source", "tax_status"],
        )

    def test_summary_counts_ready_review_and_blocked_rows(self):
        rows = [
            BomQuoteRow("A", "S1", "10", "CNY", "10000", "quote pack", "tax-included", "9", "steel", "stamping"),
            BomQuoteRow("B", "S2", "12", "CNY", "8000", "quote pack", "tax-excluded", "", "", ""),
            BomQuoteRow("C", "", "7", "CNY", "", "", "", "", "", ""),
        ]

        self.assertEqual(
            summarize_readiness(rows),
            {
                "total": 3,
                "ready-for-skill": 1,
                "needs-business-review": 1,
                "blocked-missing-required": 1,
            },
        )

    def test_report_lists_blocked_rows_before_review_rows(self):
        rows = [
            BomQuoteRow("B", "S2", "12", "CNY", "8000", "quote pack", "tax-excluded", "", "", ""),
            BomQuoteRow("C", "", "7", "CNY", "", "", "", "", "", ""),
        ]

        report = render_readiness_report(rows)

        self.assertIn("# BOM and Quotation Readiness Report", report)
        self.assertLess(report.index("| C |"), report.index("| B |"))
        self.assertIn("Do not infer supplier, volume, tax, or source fields.", report)


if __name__ == "__main__":
    unittest.main()
