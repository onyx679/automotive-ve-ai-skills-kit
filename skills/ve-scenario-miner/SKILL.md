---
name: ve-scenario-miner
description: Extract value-engineering business scenarios, high-frequency tasks, reusable methods, and Skill candidates from interview notes, meeting notes, SOPs, or shadowing records. Use when analyzing value engineering, VAVE, cost analysis, BOM review, supplier collaboration, or process documentation materials.
---

# VE Scenario Miner

Use this skill to turn messy value-engineering notes into structured AI-Skill opportunities.

## Inputs

Accept any of:

- Interview notes from value engineering colleagues.
- Meeting minutes from cost review, VAVE review, supplier discussion, or project review.
- Existing SOPs, templates, checklists, or weekly reports.
- Shadowing notes from observing daily work.

If inputs include confidential cost, supplier, drawing, or project data, remind the user to use approved enterprise tooling and redact sensitive details before external processing.

## Workflow

1. Identify the business role involved: cost analysis, VAVE, procurement collaboration, project management, documentation, or other.
2. Extract repeated tasks and record frequency signals: daily, weekly, monthly, per project, per supplier, or ad hoc.
3. For each task, capture input, action steps, decisions, output, downstream user, tools used, and common rework reasons.
4. Mark standardization potential:
   - High: clear inputs, repeated format, low business judgment.
   - Medium: repeated structure with human review.
   - Low: mostly expert judgment, negotiation, or sensitive decision-making.
5. Convert high and medium candidates into Skill cards.
6. Flag risks: missing data, confidentiality, engineering judgment, supplier sensitivity, unclear ownership, or quality/safety review.

## Output

Return:

```markdown
# VE Scenario Mining Output

## Scenario Map

| Scenario | Role | Frequency | Current Pain | Input | Output | Standardization Potential |
|---|---|---:|---|---|---|---|

## Skill Candidate Cards

### 1. <Skill candidate name>

- Trigger:
- Users:
- Required inputs:
- Steps the Skill can automate:
- Steps requiring human review:
- Output format:
- Success metric:
- Risks and boundaries:

## Questions For Business Validation

1.
2.
3.
```

## Quality Checks

- Do not invent processes not present in the source notes.
- Keep uncertain items under "Questions For Business Validation".
- Separate facts, assumptions, and recommended next steps.
- Prefer small Skills that solve one frequent task over broad assistant concepts.
