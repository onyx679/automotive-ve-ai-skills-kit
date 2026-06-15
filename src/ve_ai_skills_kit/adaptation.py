from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


ADAPTATION_SCORE_FIELDS = (
    "domain_fit",
    "workflow_similarity",
    "customization_depth",
    "validation_strength",
    "attribution_clarity",
)


@dataclass(frozen=True)
class SkillBenchmark:
    source_skill: str
    source_repo: str
    reusable_pattern: str
    target_ve_scenario: str
    domain_fit: int
    workflow_similarity: int
    customization_depth: int
    validation_strength: int
    attribution_clarity: int

    @property
    def total_score(self) -> int:
        return sum(getattr(self, field) for field in ADAPTATION_SCORE_FIELDS)

    @property
    def recommendation(self) -> str:
        if self.total_score >= 21:
            return "adapt-now"
        if self.total_score >= 16:
            return "prototype-with-review"
        return "reference-only"

    def to_markdown_row(self) -> str:
        values = [
            self.source_skill,
            self.source_repo,
            self.reusable_pattern,
            self.target_ve_scenario,
            str(self.total_score),
            self.recommendation,
        ]
        return "| " + " | ".join(values) + " |"


def _score(value: str | int) -> int:
    score = int(value)
    if score < 1 or score > 5:
        raise ValueError(f"score must be between 1 and 5, got {score}")
    return score


def benchmark_from_mapping(row: dict[str, str]) -> SkillBenchmark:
    return SkillBenchmark(
        source_skill=row["source_skill"].strip(),
        source_repo=row["source_repo"].strip(),
        reusable_pattern=row["reusable_pattern"].strip(),
        target_ve_scenario=row["target_ve_scenario"].strip(),
        domain_fit=_score(row["domain_fit"]),
        workflow_similarity=_score(row["workflow_similarity"]),
        customization_depth=_score(row["customization_depth"]),
        validation_strength=_score(row["validation_strength"]),
        attribution_clarity=_score(row["attribution_clarity"]),
    )


def rank_benchmarks(benchmarks: Iterable[SkillBenchmark]) -> list[SkillBenchmark]:
    return sorted(benchmarks, key=lambda item: (-item.total_score, item.source_skill.lower()))


def render_benchmark_report(benchmarks: Iterable[SkillBenchmark]) -> str:
    ranked = rank_benchmarks(benchmarks)
    lines = [
        "# Community Skill Benchmark Adaptation Report",
        "",
        "| Source Skill | Source Repo | Reusable Pattern | Target VE Scenario | Score | Recommendation |",
        "|---|---|---|---|---:|---|",
    ]
    lines.extend(benchmark.to_markdown_row() for benchmark in ranked)
    lines.extend(
        [
            "",
            "Recommendation rules:",
            "",
            "- `adapt-now`: score >= 21",
            "- `prototype-with-review`: score 16-20",
            "- `reference-only`: score <= 15",
            "",
            "Use this report to justify which community patterns are safe to adapt and which should only inform original VE Skill design.",
        ]
    )
    return "\n".join(lines) + "\n"
