# Case Study: From Workflow Notes to Reusable AI Skills

This case study explains how the portfolio converts repeated business work into reusable AI Skills, scripts, and reviewable outputs. It is based on simulated public examples and does not use Seres internal data, supplier quotes, vehicle BOMs, or real customer records.

中文说明：本文用于展示“业务流程 -> AI Skill -> 脚本/文档/验证”的转化方法。所有样例均为模拟数据，不包含赛力斯内部资料、真实供应商报价、真实整车 BOM 或真实客户记录。

## 1. Business Problem

Value engineering and operations teams often repeat the same preparation work:

- collect inputs from spreadsheets, meeting notes, and feedback;
- normalize fields and identify missing information;
- draft opportunity registers, checklists, SOPs, or weekly reports;
- ask business owners to confirm cost, supplier, quality, inventory, and customer-impact decisions;
- track whether the new workflow is actually used.

The risk is not only wasted time. The larger risk is that AI output can look confident while hiding missing evidence. This kit treats AI as a structured drafting layer, not as the final business decision maker.

## 2. Skillization Pattern

The reusable pattern is:

1. Define the source inputs and required fields.
2. Block incomplete rows before drafting.
3. Score which scenarios are worth turning into Skills.
4. Write a `SKILL.md` with triggers, steps, output templates, review gates, and success metrics.
5. Generate Markdown outputs from CSV examples so reviewers can inspect the result.
6. Audit every public claim against evidence and safe wording.

## 3. Automotive VE Example

In the automotive VE demo, the workflow starts with candidate scenarios and readiness checks:

- `examples/scenario_candidates.csv` feeds `scripts/score_skill_candidates.py`.
- `examples/bom_quote_readiness.csv` feeds `scripts/check_bom_quote_readiness.py`.
- `skills/vave-cost-opportunity/SKILL.md` defines how a VAVE opportunity draft should be structured.
- `skills/ve-evidence-auditor/SKILL.md` keeps resume and portfolio claims tied to evidence.

The important design choice is that rows with missing supplier, volume, tax, or source evidence are not treated as AI-ready. They are routed to human review first.

## 4. Ecommerce Transfer Example

The ecommerce supplement proves the same method can transfer to another business workflow:

- order, inventory, and support inputs are normalized as CSV files;
- SKU risk is scored from low stock, refunds, delayed fulfillment, and unresolved negative tickets;
- a Markdown weekly risk report and action queue are generated;
- inventory, refund, customer commitment, and owner assignment decisions remain human-reviewed.

This supplement is not vehicle-domain evidence. It is operating-method evidence: the candidate can decompose repeated work, define inputs and outputs, build tooling, document boundaries, and measure whether the workflow is usable.

## 5. Reviewer Takeaways

For an AI BP / Skill product role, the strongest evidence is not a polished prompt. It is the ability to:

- interview a workflow and identify repeatable tasks;
- separate facts, calculations, hypotheses, and items needing confirmation;
- ship a small usable tool with examples and tests;
- document adoption metrics and feedback loops;
- state honest boundaries before a reviewer has to ask.

## 6. What This Does Not Claim

- It is not a Seres internal project.
- It does not use real supplier quotes, real vehicle BOMs, or proprietary vehicle-program data.
- It does not claim final cost, supplier, quality, engineering, refund, or customer commitments.
- It does not claim open-source PRs are merged unless the public PR state proves it.
