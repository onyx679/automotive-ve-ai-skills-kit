from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


SCORE_FIELDS = (
    "frequency",
    "time_cost",
    "standardization",
    "risk_control",
    "data_availability",
    "visible_benefit",
    "user_willingness",
)


@dataclass(frozen=True)
class ScenarioCandidate:
    name: str
    role: str
    pain: str
    frequency: int
    time_cost: int
    standardization: int
    risk_control: int
    data_availability: int
    visible_benefit: int
    user_willingness: int

    @property
    def total_score(self) -> int:
        return sum(getattr(self, field) for field in SCORE_FIELDS)

    @property
    def priority(self) -> str:
        if self.total_score >= 28:
            return "pilot-now"
        if self.total_score >= 22:
            return "validate-next"
        return "document-first"

    def to_markdown_row(self) -> str:
        values = [
            self.name,
            self.role,
            str(self.total_score),
            self.priority,
            self.pain,
        ]
        return "| " + " | ".join(values) + " |"


def _score(value: str | int) -> int:
    score = int(value)
    if score < 1 or score > 5:
        raise ValueError(f"score must be between 1 and 5, got {score}")
    return score


def candidate_from_mapping(row: dict[str, str]) -> ScenarioCandidate:
    return ScenarioCandidate(
        name=row["name"].strip(),
        role=row["role"].strip(),
        pain=row["pain"].strip(),
        frequency=_score(row["frequency"]),
        time_cost=_score(row["time_cost"]),
        standardization=_score(row["standardization"]),
        risk_control=_score(row["risk_control"]),
        data_availability=_score(row["data_availability"]),
        visible_benefit=_score(row["visible_benefit"]),
        user_willingness=_score(row["user_willingness"]),
    )


def rank_candidates(candidates: Iterable[ScenarioCandidate]) -> list[ScenarioCandidate]:
    return sorted(candidates, key=lambda item: (-item.total_score, item.name.lower()))


def render_candidate_report(candidates: Iterable[ScenarioCandidate]) -> str:
    ranked = rank_candidates(candidates)
    lines = [
        "# VE AI Skill Candidate Ranking",
        "",
        "| Scenario | Role | Score | Priority | Pain |",
        "|---|---|---:|---|---|",
    ]
    lines.extend(candidate.to_markdown_row() for candidate in ranked)
    lines.extend(
        [
            "",
            "Priority rules:",
            "",
            "- `pilot-now`: score >= 28",
            "- `validate-next`: score 22-27",
            "- `document-first`: score <= 21",
        ]
    )
    return "\n".join(lines) + "\n"

