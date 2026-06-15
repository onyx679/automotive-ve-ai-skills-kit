import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ve_ai_skills_kit.adoption import AdoptionMetric, summarize_adoption_metrics


class AdoptionMetricsTest(unittest.TestCase):
    def test_decrease_metric_can_improve(self):
        metric = AdoptionMetric(
            metric="Draft preparation time",
            before=90,
            after=45,
            unit="min",
            direction="decrease",
            note="demo",
        )

        self.assertTrue(metric.improved)
        self.assertEqual(metric.change_label(), "-50%")

    def test_summary_counts_watch_items(self):
        metrics = [
            AdoptionMetric("Field completeness", 68, 91, "%", "increase", "demo"),
            AdoptionMetric("Rework", 1, 2, "", "decrease", "demo"),
        ]

        self.assertEqual(summarize_adoption_metrics(metrics), {"total": 2, "improved": 1, "watch": 1})


if __name__ == "__main__":
    unittest.main()
