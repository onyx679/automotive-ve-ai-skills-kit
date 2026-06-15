from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from ve_ai_skills_kit.scoring import candidate_from_mapping, render_candidate_report


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/score_skill_candidates.py <scenario_candidates.csv>", file=sys.stderr)
        return 2

    source = Path(sys.argv[1])
    with source.open("r", encoding="utf-8", newline="") as handle:
        candidates = [candidate_from_mapping(row) for row in csv.DictReader(handle)]

    print(render_candidate_report(candidates), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

