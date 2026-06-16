import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class LandingPlanTest(unittest.TestCase):
    def test_landing_plan_has_weeks_outputs_and_boundaries(self):
        text = (ROOT / "docs" / "landing-plan.md").read_text(encoding="utf-8")

        self.assertIn("# 30-Day AI BP Landing Plan", text)
        self.assertIn("Week 1: Workflow Discovery", text)
        self.assertIn("Week 2: Pilot Selection", text)
        self.assertIn("Week 3: Skill MVP", text)
        self.assertIn("Week 4: Adoption Review", text)
        self.assertIn("Do not claim this is a Seres internal plan.", text)
        self.assertIn("Resume-Safe Summary", text)

    def test_readmes_link_landing_plan(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        zh_readme = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

        self.assertIn("docs/landing-plan.md", readme)
        self.assertIn("docs/landing-plan.md", zh_readme)


if __name__ == "__main__":
    unittest.main()
