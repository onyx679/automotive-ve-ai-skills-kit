---
name: ve-evidence-auditor
description: Audit value-engineering AI Skill claims against concrete evidence links, review status, and honest wording boundaries. Use when preparing resumes, portfolios, project reports, best-practice documents, release notes, or management summaries that must distinguish verified work, submitted PRs, pending reviews, assumptions, and claims that should not be made.
---

# VE Evidence Auditor

Use this skill to turn project claims into an evidence-backed claim matrix before publishing them in a resume, portfolio, report, or internal best-practice document.

## Inputs

Accept any of:

- Resume bullets or project descriptions.
- GitHub repositories, releases, pull requests, issues, CI runs, or portfolio pages.
- Work logs, adoption reports, Skill outputs, SOPs, and demo artifacts.
- A CSV claim ledger with `claim`, `source_kind`, `evidence_level`, `verdict`, `evidence_status`, `evidence_url`, `resume_wording`, and `boundary`.

## Workflow

1. Break the text into atomic claims. Each claim should assert one thing only.
2. Attach a concrete evidence URL or file path to every claim.
3. Grade the source:
   - `source_kind`: `platform-record`, `repository-artifact`, `third-party`, `self-reported`, or `mixed`.
   - `evidence_level`: `L4` for directly checkable platform/repository records; `L3` for multiple independent sources; `L2` for one credible third-party source; `L1` for self-reported or weak evidence.
   - `verdict`: `confirmed`, `largely-credible`, `doubtful`, or `debunked`.
4. Mark evidence status:
   - `verified`: public link or local artifact proves the claim.
   - `open`: submitted but not merged, approved, or accepted.
   - `pending-review`: waiting for maintainer, manager, or business review.
   - `missing`: no evidence yet.
5. Classify claim level:
   - `resume-ready`: verified evidence exists and wording is not overstated.
   - `boundary-only`: evidence exists, but wording must mention open or pending status.
   - `do-not-claim`: evidence is missing, wording implies unearned completion, or the claim depends on confidential/internal facts not available.
6. Rewrite risky claims into safe wording.
7. Keep a "do not claim yet" section for tempting but unsupported statements.

## Output

Return:

```markdown
# Evidence Claim Matrix

## Summary

- Resume-ready:
- Boundary-only:
- Do-not-claim:

## Claim Review

| Claim | Source | Evidence level | Verdict | Status | Claim level | Evidence | Safe wording | Boundary |
|---|---|---|---|---|---|---|---|---|

## Do Not Claim Yet

- <claim>: <reason>
```

## Quality Checks

- Never upgrade `open` or `pending-review` PRs into merged contribution claims.
- Never claim internal deployment, supplier data handling, or business impact unless there is approved evidence.
- Prefer "submitted PR", "published demo", "verified by CI", and "review-pending" over vague prestige wording.
- Treat self-reported or marketing-only evidence as `L1` unless it is backed by a directly checkable platform record.
- If a claim has no URL, artifact, or owner-verifiable source, keep it out of the resume.
- Preserve the difference between public portfolio evidence and real enterprise work.
