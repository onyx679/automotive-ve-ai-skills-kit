---
name: ve-manual-writer
description: Convert value-engineering workflow notes, SOP drafts, meeting decisions, templates, or best-practice examples into concise operating manuals, checklists, FAQs, and training materials for value engineering teams.
---

# VE Manual Writer

Use this skill to turn process knowledge into documents that colleagues can actually use.

## Inputs

- Raw process notes.
- Existing SOP fragments.
- Meeting decisions.
- Screenshots or descriptions of tool workflows.
- Templates and example reports.
- Feedback from users.

## Workflow

1. Identify the target reader: new joiner, cost analyst, VAVE engineer, project manager, procurement collaborator, or manager.
2. Define the task boundary: when to use the process and when not to use it.
3. Convert the process into steps with inputs, actions, outputs, owner, and checks.
4. Add common mistakes and exception handling.
5. Add a concise example using redacted or synthetic data.
6. Add a version record and feedback channel.

## Output

```markdown
# <Manual Title>

## Purpose

## When To Use

## Required Inputs

## Procedure

| Step | Action | Owner | Output | Quality Check |
|---|---|---|---|---|

## Exceptions

| Situation | What To Do | Escalation |
|---|---|---|

## Example

## FAQ

## Version Record

| Version | Date | Change | Owner |
|---|---|---|---|
```

## Style Rules

- Use short steps and active verbs.
- Prefer tables for repeated process information.
- Put business rules in checklists.
- Avoid long background explanations in operating manuals.
- Clearly mark confidential or internal-only sections.
