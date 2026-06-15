from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


REQUIRED_FIELDS = (
    "component",
    "supplier",
    "quoted_cost",
    "currency",
    "annual_volume",
    "evidence_source",
    "tax_status",
)

RECOMMENDED_FIELDS = (
    "target_cost",
    "material",
    "process",
)

READINESS_ORDER = {
    "blocked-missing-required": 0,
    "needs-business-review": 1,
    "ready-for-skill": 2,
}


@dataclass(frozen=True)
class BomQuoteRow:
    component: str
    supplier: str
    quoted_cost: str
    currency: str
    annual_volume: str
    evidence_source: str
    tax_status: str
    target_cost: str
    material: str
    process: str

    @property
    def missing_required_fields(self) -> list[str]:
        return _missing_fields(self, REQUIRED_FIELDS)

    @property
    def missing_recommended_fields(self) -> list[str]:
        return _missing_fields(self, RECOMMENDED_FIELDS)

    @property
    def readiness_level(self) -> str:
        if self.missing_required_fields:
            return "blocked-missing-required"
        if self.missing_recommended_fields:
            return "needs-business-review"
        return "ready-for-skill"

    def to_markdown_row(self) -> str:
        values = [
            self.component,
            self.supplier or "-",
            self.readiness_level,
            _format_missing(self.missing_required_fields),
            _format_missing(self.missing_recommended_fields),
        ]
        return "| " + " | ".join(values) + " |"


def _missing_fields(row: BomQuoteRow, fields: Iterable[str]) -> list[str]:
    missing = []
    for field in fields:
        value = getattr(row, field)
        if not str(value).strip():
            missing.append(field)
    return missing


def _format_missing(fields: list[str]) -> str:
    return ", ".join(fields) if fields else "-"


def row_from_mapping(row: dict[str, str]) -> BomQuoteRow:
    return BomQuoteRow(
        component=row.get("component", "").strip(),
        supplier=row.get("supplier", "").strip(),
        quoted_cost=row.get("quoted_cost", "").strip(),
        currency=row.get("currency", "").strip(),
        annual_volume=row.get("annual_volume", "").strip(),
        evidence_source=row.get("evidence_source", "").strip(),
        tax_status=row.get("tax_status", "").strip(),
        target_cost=row.get("target_cost", "").strip(),
        material=row.get("material", "").strip(),
        process=row.get("process", "").strip(),
    )


def rank_readiness_rows(rows: Iterable[BomQuoteRow]) -> list[BomQuoteRow]:
    return sorted(
        rows,
        key=lambda row: (READINESS_ORDER[row.readiness_level], row.component.lower()),
    )


def summarize_readiness(rows: Iterable[BomQuoteRow]) -> dict[str, int]:
    summary = {
        "total": 0,
        "ready-for-skill": 0,
        "needs-business-review": 0,
        "blocked-missing-required": 0,
    }
    for row in rows:
        summary["total"] += 1
        summary[row.readiness_level] += 1
    return summary


def render_readiness_report(rows: Iterable[BomQuoteRow]) -> str:
    ranked = rank_readiness_rows(rows)
    summary = summarize_readiness(ranked)
    lines = [
        "# BOM and Quotation Readiness Report",
        "",
        "## Summary",
        "",
        f"- Total rows: {summary['total']}",
        f"- Ready for Skill: {summary['ready-for-skill']}",
        f"- Needs business review: {summary['needs-business-review']}",
        f"- Blocked by missing required fields: {summary['blocked-missing-required']}",
        "",
        "## Row Readiness",
        "",
        "| Component | Supplier | Readiness | Missing required | Missing recommended |",
        "|---|---|---|---|---|",
    ]
    lines.extend(row.to_markdown_row() for row in ranked)
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not infer supplier, volume, tax, or source fields.",
            "- Treat missing target cost, material, or process as a business-review item.",
            "- Use this report to prepare a human review queue before drafting VAVE opportunities.",
        ]
    )
    return "\n".join(lines) + "\n"
