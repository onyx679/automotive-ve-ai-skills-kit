import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ve_ai_skills_kit.adaptation import SkillBenchmark, rank_benchmarks, render_benchmark_report


class SkillAdaptationTest(unittest.TestCase):
    def test_recommendation_thresholds(self):
        benchmark = SkillBenchmark(
            source_skill="skill-creator",
            source_repo="anthropics/skills",
            reusable_pattern="Skill anatomy",
            target_ve_scenario="VE Skill packaging",
            domain_fit=5,
            workflow_similarity=5,
            customization_depth=5,
            validation_strength=5,
            attribution_clarity=5,
        )

        self.assertEqual(benchmark.total_score, 25)
        self.assertEqual(benchmark.recommendation, "adapt-now")

    def test_rank_benchmarks_by_score_then_name(self):
        low = SkillBenchmark("B", "repo", "pattern", "scenario", 3, 3, 3, 3, 3)
        high = SkillBenchmark("A", "repo", "pattern", "scenario", 5, 5, 5, 5, 5)

        self.assertEqual(rank_benchmarks([low, high]), [high, low])

    def test_render_report_contains_recommendation_rules(self):
        report = render_benchmark_report(
            [SkillBenchmark("source", "repo", "pattern", "scenario", 4, 4, 4, 4, 4)]
        )

        self.assertIn("Community Skill Benchmark Adaptation Report", report)
        self.assertIn("prototype-with-review", report)


if __name__ == "__main__":
    unittest.main()
