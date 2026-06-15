# Contributing

Thank you for considering a contribution to Automotive VE AI Skills Kit.

This project focuses on safe, practical AI Skill workflows for automotive value engineering and VAVE teams.

## Good Contributions

- Improve or add AI Skill templates for value engineering workflows.
- Add synthetic examples for BOM, quotation, VAVE meeting, SOP, or adoption-review scenarios.
- Improve scoring logic, adoption metrics, or report formatting.
- Add tests for workflow scoring or adoption-report behavior.
- Improve documentation, especially around human-review guardrails.

## Guardrails

Do not submit proprietary vehicle, supplier, cost, drawing, warranty, quality, or program data.

Use only:

- synthetic examples
- public examples
- redacted examples with permission

AI outputs in this project must preserve human review for:

- supplier decisions
- confirmed savings
- engineering feasibility
- quality and safety risks
- warranty or regulatory impact
- financial approval

## Local Validation

Run unit tests:

```bash
python -m unittest discover -s tests
```

Run example scripts:

```bash
python scripts/score_skill_candidates.py examples/scenario_candidates.csv
python scripts/generate_adoption_report.py examples/adoption_metrics.csv
```

Validate Skill frontmatter with a compatible Claude/Codex skill validator when available.

## Pull Request Checklist

- [ ] Uses synthetic or approved public data only.
- [ ] Adds or updates tests when behavior changes.
- [ ] Updates README or docs when workflow behavior changes.
- [ ] Keeps cost, supplier, quality, and engineering conclusions under human review.
- [ ] Avoids broad "do everything" assistant behavior; prefer narrow, testable Skills.

