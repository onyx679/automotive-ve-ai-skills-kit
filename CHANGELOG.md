# Changelog

## v0.4.2 - 2026-06-16

- Default the GitHub Pages portfolio page to English while keeping Chinese available through the language switcher.
- Add page-level tests that verify the default language and Chinese option are present.
- Update verification links to the current main and ecommerce portfolio releases.

## v0.4.1 - 2026-06-16

- Add a reviewer-facing case study that explains the workflow-notes-to-AI-Skills conversion method.
- Add case study links to the portfolio page, verification section, and bilingual README files.
- Keep the case study scoped to public simulated examples and explicit human-review boundaries.

## v0.4.0 - 2026-06-16

- Add `ve-skill-benchmark-adapter` for turning community Skill patterns into properly attributed automotive VE/VAVE Skill designs.
- Add `scripts/adapt_skill_benchmarks.py`, sample benchmark data, generated Markdown output, and unit tests for adaptation recommendations.

## v0.3.0 - 2026-06-16

- Add `ve-evidence-auditor` for checking resume, portfolio, release, and report claims against evidence links, evidence levels, verdicts, and honest wording boundaries.
- Add `scripts/generate_evidence_matrix.py`, sample claim ledger data, generated Markdown output, and unit tests for claim-level classification.

## v0.2.0 - 2026-06-15

- Add a BOM and quotation readiness gate for checking whether rows are safe to use in AI-assisted VAVE drafting.
- Add `scripts/check_bom_quote_readiness.py`, sample CSV data, generated Markdown output, and unit tests for readiness classification.
