---
name: ve-skill-benchmark-adapter
description: Benchmark community Claude Code, Codex, or AI-agent Skills and adapt their reusable patterns into automotive value-engineering Skill designs. Use when reviewing open-source Skill repositories, deciding whether to reuse an existing Skill structure, or converting a generic Skill into a VE/VAVE workflow with proper evidence, validation, and attribution.
---

# VE Skill Benchmark Adapter

Use this skill to adapt public Skill patterns into automotive value-engineering workflows without copying blindly.

## Inputs

Accept any of:

- Links or notes from open-source Skill repositories.
- Existing `SKILL.md` files or Skill folder structures.
- A target VE workflow such as BOM review, VAVE opportunity drafting, quote readiness, SOP writing, or adoption feedback.
- Constraints from the target team: data sensitivity, review owner, output format, and validation method.

## Workflow

1. Identify the source Skill's reusable pattern: interview workflow, checklist, scoring rubric, document generator, evidence auditor, CLI script, or reference library.
2. Separate reusable structure from domain-specific content.
3. Map the reusable structure to one narrow VE workflow.
4. Decide the adaptation depth:
   - `reference-only`: use as inspiration, no direct content reuse.
   - `structure-reuse`: keep the folder/resource pattern but rewrite domain logic.
   - `script-adapt`: adapt code or command flow with tests and attribution.
   - `fork-contribute`: improve the upstream project with a PR before or alongside local reuse.
5. Add attribution boundaries:
   - keep license-compatible source links in project docs or PR notes;
   - do not claim original authorship for community patterns;
   - clearly state what was redesigned for VE/VAVE.
6. Define validation:
   - sample redacted input;
   - expected Markdown/CSV output;
   - unit or smoke test;
   - human-review gate for engineering, supplier, cost, and quality decisions.

## Output

Return:

```markdown
# Skill Benchmark Adaptation Brief

## Source Pattern

| Source Skill | Source Repo | Reusable Pattern | License/Attribution Note |
|---|---|---|---|

## VE Adaptation Plan

| Target VE Scenario | Adaptation Depth | New Skill Name | Required Resources | Validation |
|---|---|---|---|---|

## Redesign Notes

- What is reused:
- What is rewritten:
- What must not be copied:
- Human-review boundary:

## Implementation Checklist

- [ ] Create or update `SKILL.md`.
- [ ] Add only necessary `references/`, `scripts/`, or `assets/`.
- [ ] Add sample input and output.
- [ ] Run quick validation and project tests.
- [ ] Record evidence links honestly in resume or portfolio material.
```

## Quality Checks

- Do not hide copied source material behind a renamed Skill.
- Prefer adapting workflow shape, validation gates, and resource organization over copying prose.
- Make the VE scenario more specific than the source Skill.
- Treat attribution and license compatibility as part of the deliverable.
- Keep sensitive automotive data out of public examples.
