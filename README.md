# Automotive VE AI Skills Kit

AI Skill templates and lightweight workflow tools for automotive value engineering (VE/VAVE) productivity scenarios.

This repository is a portfolio-grade, non-confidential demo. It does not contain proprietary data from Seres, suppliers, or any vehicle program.

## Why This Exists

Automotive value engineering teams handle repeated, document-heavy workflows:

- BOM and quotation normalization
- VAVE opportunity register drafting
- cost review meeting notes
- SOP and best-practice documentation
- AI Skill adoption feedback

This kit shows how those workflows can be converted into reusable AI agent Skills while keeping engineering, quality, supplier, and cost decisions under human review.

## Contents

```text
automotive-ve-ai-skills-kit/
  skills/
    ve-scenario-miner/
    vave-cost-opportunity/
    ve-manual-writer/
    skill-adoption-feedback/
  src/ve_ai_skills_kit/
    scoring.py
    adoption.py
  scripts/
    score_skill_candidates.py
    generate_adoption_report.py
  examples/
    scenario_candidates.csv
    adoption_metrics.csv
  tests/
```

## Skills

| Skill | Purpose |
|---|---|
| `ve-scenario-miner` | Extract high-frequency VE tasks and Skill candidates from interviews or meeting notes. |
| `vave-cost-opportunity` | Structure BOM, quotation, benchmarking, and meeting data into a VAVE opportunity register draft. |
| `ve-manual-writer` | Convert workflow notes into SOPs, FAQs, checklists, and best-practice documents. |
| `skill-adoption-feedback` | Analyze Skill usage, user feedback, productivity impact, and iteration priorities. |

## Scripts

Score candidate workflows:

```bash
python scripts/score_skill_candidates.py examples/scenario_candidates.csv
```

Generate an adoption report:

```bash
python scripts/generate_adoption_report.py examples/adoption_metrics.csv
```

Run tests:

```bash
python -m unittest discover -s tests
```

## Evidence Types

For cost and supplier-sensitive workflows, this kit separates conclusions into:

- `Fact`: directly present in the source material
- `Calculation`: derived from stated numbers and a visible formula
- `Hypothesis`: plausible but not verified
- `Needs confirmation`: requires human review

The AI assistant should never fabricate cost, supplier, quality, or engineering feasibility conclusions.

## Portfolio Positioning

This project supports a candidate profile such as:

> AI productivity BP / Skill product manager for automotive value engineering teams.

It demonstrates business process analysis, AI Skill design, VAVE workflow understanding, documentation discipline, and adoption measurement.

## License

MIT

