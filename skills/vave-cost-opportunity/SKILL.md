---
name: vave-cost-opportunity
description: Structure VAVE or value-engineering cost-reduction opportunities from BOM, quotation summaries, teardown notes, benchmarking notes, and meeting records. Use for automotive cost analysis, should-cost review, supplier comparison, and opportunity-pipeline drafting.
---

# VAVE Cost Opportunity

Use this skill to create a disciplined first draft of a cost-reduction opportunity register. It assists analysis but never replaces engineering, quality, procurement, finance, or supplier approval.

## Safety Boundary

Never fabricate cost, quotation, material, supplier, or engineering feasibility data.

Every conclusion must be labeled as one of:

- `Fact`: directly present in the source.
- `Calculation`: derived from stated numbers and formula.
- `Hypothesis`: plausible but not proven.
- `Needs confirmation`: requires business owner review.

## Inputs

Useful inputs include:

- BOM or parts list.
- Supplier quotation summary.
- Material, weight, process, tooling, logistics, or packaging notes.
- Teardown or benchmarking notes.
- Historical cost or target cost.
- Meeting minutes and action items.

If key inputs are missing, start by listing required missing fields.

## Workflow

1. Normalize the source material into a part-level table.
2. Identify cost drivers: material, weight, process, tooling, yield, logistics, packaging, quality requirements, supplier margin, or volume.
3. Compare available baselines: current vs target, supplier A vs B, internal history, benchmark, or estimated should-cost.
4. Generate opportunity hypotheses only when evidence exists.
5. For each opportunity, capture expected impact, confidence, risk, validation path, owner, and next action.
6. Separate quick wins from engineering-change opportunities and strategic supplier opportunities.

## Output

```markdown
# VAVE Cost Opportunity Register

## Data Completeness

| Required Field | Status | Notes |
|---|---|---|

## Cost Driver Summary

| Part/System | Main Cost Driver | Evidence | Confidence |
|---|---|---|---|

## Opportunity Register

| ID | Opportunity | Evidence Type | Potential Impact | Risk | Required Review | Next Action | Owner |
|---|---|---|---|---|---|---|---|

## Assumptions And Open Questions

1.
2.
3.
```

## Quality Checks

- Do not rank opportunities solely by estimated savings; include risk and validation effort.
- Mark any missing cost baseline explicitly.
- Do not expose supplier-sensitive information in broad summaries.
- Route safety, regulatory, quality, and warranty-impacting changes to human review.
