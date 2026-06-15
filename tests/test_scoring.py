import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ve_ai_skills_kit.scoring import ScenarioCandidate, rank_candidates


class ScenarioScoringTest(unittest.TestCase):
    def test_priority_thresholds(self):
        candidate = ScenarioCandidate(
            name="VAVE opportunity register draft",
            role="Cost analyst",
            pain="Missing evidence",
            frequency=5,
            time_cost=5,
            standardization=4,
            risk_control=3,
            data_availability=4,
            visible_benefit=5,
            user_willingness=4,
        )

        self.assertEqual(candidate.total_score, 30)
        self.assertEqual(candidate.priority, "pilot-now")

    def test_rank_candidates_by_score_then_name(self):
        low = ScenarioCandidate("B", "role", "pain", 3, 3, 3, 3, 3, 3, 3)
        high = ScenarioCandidate("A", "role", "pain", 5, 5, 5, 5, 5, 5, 5)

        self.assertEqual(rank_candidates([low, high]), [high, low])


if __name__ == "__main__":
    unittest.main()
