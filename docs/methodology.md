# Methodology

This project uses a readiness gate plus a five-step workflow to convert automotive value engineering work into AI Skills.

## 0. Check Input Readiness

Before a Skill drafts VAVE opportunities, check whether BOM and quotation rows contain the minimum fields needed for safe processing:

- component
- supplier
- quoted cost
- currency
- annual volume
- evidence source
- tax status

Missing supplier, volume, tax, or source fields should block AI-assisted drafting until a human fills them. Missing target cost, material, or process should be treated as a business-review item.

## 1. Mine The Workflow

Start with interviews, meeting notes, SOP fragments, or shadowing records.

Capture:

- user role
- trigger event
- inputs
- repeated actions
- decisions
- output
- downstream user
- rework causes
- sensitive data boundaries

The goal is not to automate everything. The goal is to find frequent, structured work where AI can prepare better drafts for human review.

## 2. Score Skill Candidates

Score each candidate from 1 to 5 across seven dimensions:

| Dimension | Question |
|---|---|
| Frequency | Does this happen daily or weekly? |
| Time cost | Does it consume meaningful analyst or project-manager time? |
| Standardization | Are inputs, steps, and outputs repeatable? |
| Risk control | Can AI assist without making final safety, quality, supplier, or financial decisions? |
| Data availability | Can approved or redacted data be provided consistently? |
| Visible benefit | Can time saved or quality improvement be measured? |
| User willingness | Are business users willing to pilot it? |

Priority bands:

- `pilot-now`: score >= 28
- `validate-next`: score 22-27
- `document-first`: score <= 21

## 3. Productize The Skill

Each Skill should define:

- trigger scenario
- target users
- required inputs
- workflow steps
- output format
- human-review gates
- data boundaries
- quality checks
- success metrics

Keep Skills small. A narrowly scoped VAVE opportunity-register assistant is easier to test and trust than a broad "value engineering copilot."

## 4. Preserve Human Review

Automotive value engineering decisions affect quality, warranty, safety, supplier relationships, and financial targets.

AI output must separate:

- `Fact`: directly present in source material
- `Calculation`: derived from visible numbers and formulas
- `Hypothesis`: plausible but unverified
- `Needs confirmation`: requires human owner review

Do not fabricate missing costs, supplier quotes, feasibility conclusions, or confirmed savings.

## 5. Measure Adoption

A Skill is useful only if business users trust and reuse it.

Track:

- active users
- repeat users
- preparation time
- rework count
- field completeness
- missing confirmation questions
- user satisfaction
- issue fix rate

Use feedback to update input templates, output formats, business rules, and guardrails.

## 6. Adapt Community Patterns Responsibly

When using public Claude Code, Codex, or agent Skill examples, separate reusable structure from domain content.

Evaluate each source pattern across:

- domain fit
- workflow similarity
- customization depth
- validation strength
- attribution clarity

Only adapt patterns that can be rewritten into a specific VE workflow with license-compatible attribution, redacted examples, tests or smoke checks, and explicit human-review boundaries. Do not present renamed community material as original work.
