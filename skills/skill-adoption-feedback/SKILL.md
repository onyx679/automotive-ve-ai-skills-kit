---
name: skill-adoption-feedback
description: Track AI Skill usage, user feedback, productivity impact, quality issues, and iteration priorities for internal business-process Skills. Use after piloting Claude Code, Codex, OpenCode, or similar agent Skills with business teams.
---

# Skill Adoption Feedback

Use this skill to turn scattered user feedback into an iteration plan and measurable adoption report.

## Inputs

- Usage logs or manual usage counts.
- User feedback forms.
- Interview notes.
- Before/after task-time samples.
- Examples of good and bad Skill outputs.
- Version history.

## Workflow

1. Segment feedback by user role and scenario.
2. Measure adoption:
   - Active users.
   - Usage count.
   - Repeat usage.
   - Task coverage.
3. Measure productivity:
   - Baseline time.
   - Skill-assisted time.
   - Rework count.
   - Output completeness.
4. Classify problems:
   - Trigger unclear.
   - Input hard to prepare.
   - Output format wrong.
   - Domain rule missing.
   - Hallucination or unsupported conclusion.
   - Permission or data-boundary issue.
5. Prioritize iterations by impact, frequency, risk, and effort.
6. Produce a version plan.

## Output

```markdown
# Skill Adoption Report

## Executive Summary

## Adoption Metrics

| Metric | Current | Baseline/Target | Trend | Notes |
|---|---:|---:|---|---|

## Feedback Themes

| Theme | User Role | Frequency | Example | Root Cause |
|---|---|---:|---|---|

## Quality Issues

| Issue | Severity | Evidence | Fix |
|---|---|---|---|

## Iteration Backlog

| Priority | Change | Expected Impact | Effort | Owner |
|---|---|---|---|---|

## Next Pilot Plan
```

## Quality Checks

- Do not treat usage count alone as success.
- Always include output quality and user trust.
- Separate product issues from training issues.
- Keep sensitive examples redacted.
