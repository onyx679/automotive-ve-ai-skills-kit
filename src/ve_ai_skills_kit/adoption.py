from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AdoptionMetric:
    metric: str
    before: float
    after: float
    unit: str
    direction: str
    note: str

    @property
    def delta(self) -> float:
        return self.after - self.before

    @property
    def relative_change(self) -> float | None:
        if self.before == 0:
            return None
        return self.delta / self.before

    @property
    def improved(self) -> bool:
        if self.direction == "increase":
            return self.after > self.before
        if self.direction == "decrease":
            return self.after < self.before
        raise ValueError(f"direction must be increase or decrease, got {self.direction}")

    def change_label(self) -> str:
        relative = self.relative_change
        if relative is None:
            return "new baseline"
        return f"{relative:+.0%}"

    def to_markdown_row(self) -> str:
        status = "improved" if self.improved else "watch"
        values = [
            self.metric,
            f"{self.before:g}{self.unit}",
            f"{self.after:g}{self.unit}",
            self.change_label(),
            status,
            self.note,
        ]
        return "| " + " | ".join(values) + " |"


def metric_from_mapping(row: dict[str, str]) -> AdoptionMetric:
    return AdoptionMetric(
        metric=row["metric"].strip(),
        before=float(row["before"]),
        after=float(row["after"]),
        unit=row.get("unit", "").strip(),
        direction=row["direction"].strip(),
        note=row.get("note", "").strip(),
    )


def summarize_adoption_metrics(metrics: list[AdoptionMetric]) -> dict[str, int]:
    improved = sum(1 for metric in metrics if metric.improved)
    return {
        "total": len(metrics),
        "improved": improved,
        "watch": len(metrics) - improved,
    }


def render_adoption_report(metrics: list[AdoptionMetric]) -> str:
    summary = summarize_adoption_metrics(metrics)
    lines = [
        "# AI Skill Adoption Report",
        "",
        f"Metrics reviewed: {summary['total']}",
        f"Improved metrics: {summary['improved']}",
        f"Watch metrics: {summary['watch']}",
        "",
        "| Metric | Before | After | Change | Status | Note |",
        "|---|---:|---:|---:|---|---|",
    ]
    lines.extend(metric.to_markdown_row() for metric in metrics)
    return "\n".join(lines) + "\n"

