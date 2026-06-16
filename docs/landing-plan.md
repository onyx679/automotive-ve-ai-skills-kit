# 30-Day AI BP Landing Plan

This plan explains how the portfolio workflow would be used after joining an automotive value engineering team. It is a public, non-confidential plan based on the demo project. It is not a Seres internal process description.

## Principles

- Start with interviews and shadowing before building tools.
- Select low-risk, high-frequency workflows first.
- Keep AI output as draft preparation, not final business authority.
- Measure adoption before scaling.
- Keep every claim tied to observable evidence.

## Week 1: Workflow Discovery

Goal: understand repeated work before proposing automation.

Activities:

- Interview value engineering, cost, sourcing, quality, and program stakeholders.
- Observe repeated document workflows such as scenario intake, BOM or quotation checks, VAVE opportunity drafting, SOP writing, and Skill feedback collection.
- Record each workflow as inputs, steps, outputs, rework causes, human decisions, and sensitive fields.
- Mark data that cannot be used in AI tooling without approval.

Outputs:

- Scenario map.
- Interview notes.
- Input-field inventory.
- Sensitive-data boundary list.

Evidence in this repository:

- `skills/ve-scenario-miner/SKILL.md`
- `examples/scenario_candidates.csv`
- `scripts/score_skill_candidates.py`

## Week 2: Pilot Selection

Goal: choose one workflow that is useful, repeatable, and low-risk.

Selection criteria:

- Frequency.
- Time cost.
- Standardization potential.
- Data availability.
- Human review clarity.
- Expected benefit.
- User willingness.

Recommended first pilots:

- Meeting notes to workflow summary.
- Draft VAVE opportunity register from already-approved public/simulated fields.
- SOP or checklist generation from existing workflow notes.
- Feedback summary for AI Skill usage.

Outputs:

- Skill backlog.
- Pilot scorecard.
- Pilot success metrics.
- Review gate definition.

Evidence in this repository:

- `examples/output/skill_candidate_ranking.md`
- `skills/vave-cost-opportunity/SKILL.md`
- `skills/ve-manual-writer/SKILL.md`

## Week 3: Skill MVP

Goal: ship a small Skill that business users can safely try.

Activities:

- Write the Skill trigger, inputs, steps, output format, and review boundary.
- Create sample inputs and expected outputs.
- Add blocked-field logic when data is incomplete or sensitive.
- Run trial sessions with business users.
- Capture issues as defects, wording gaps, or missing fields.

Outputs:

- Skill MVP.
- Sample input and output.
- Human-review checklist.
- Trial notes.

Evidence in this repository:

- `scripts/check_bom_quote_readiness.py`
- `examples/output/bom_quote_readiness_report.md`
- `skills/ve-evidence-auditor/SKILL.md`

## Week 4: Adoption Review

Goal: decide whether to iterate, expand, or stop the pilot.

Metrics:

- Usage count.
- Preparation time saved.
- Rework count.
- Field completeness.
- User satisfaction.
- Number of outputs requiring human correction.

Outputs:

- Adoption report.
- Issue backlog.
- Iteration plan.
- Scale-or-stop recommendation.

Evidence in this repository:

- `scripts/generate_adoption_report.py`
- `examples/adoption_metrics.csv`
- `examples/output/adoption_report.md`
- `skills/skill-adoption-feedback/SKILL.md`

## Do Not Claim

- Do not claim this is a Seres internal plan.
- Do not claim access to real supplier quotations, vehicle BOMs, or confidential cost data.
- Do not claim AI can make final cost, sourcing, quality, or engineering decisions.
- Do not claim external PRs are merged unless the public PR state proves it.

## Resume-Safe Summary

> Built a public automotive value engineering AI workflow kit and documented a 30-day landing plan for turning repeated business workflows into AI Skills. The plan covers stakeholder interviews, pilot selection, Skill MVP design, review gates, adoption metrics, and evidence boundaries. All examples are public and non-confidential.
