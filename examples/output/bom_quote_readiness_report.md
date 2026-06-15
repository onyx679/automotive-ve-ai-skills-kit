# BOM and Quotation Readiness Report

## Summary

- Total rows: 3
- Ready for Skill: 1
- Needs business review: 1
- Blocked by missing required fields: 1

## Row Readiness

| Component | Supplier | Readiness | Missing required | Missing recommended |
|---|---|---|---|---|
| HV harness clip | - | blocked-missing-required | supplier, annual_volume, evidence_source | target_cost |
| Battery tray fastener | Supplier B | needs-business-review | - | target_cost, material, process |
| Seat bracket | Supplier A | ready-for-skill | - | - |

## Guardrails

- Do not infer supplier, volume, tax, or source fields.
- Treat missing target cost, material, or process as a business-review item.
- Use this report to prepare a human review queue before drafting VAVE opportunities.
