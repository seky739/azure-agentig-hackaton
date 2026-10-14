# nordic-foods — Handoff (Step 3.5 complete; ready for Step 4 IaC Planning)
Updated: 2026-10-14 | IaC: Terraform | Branch: n/a

## Completed Steps
- [x] Step 1 → agent-output/nordic-foods/01-requirements.md (review approved; Gate 1 approved)
- [x] Step 2 → agent-output/nordic-foods/02-architecture-assessment.md and 03-des-cost-estimate.md (architecture and cost-feasibility reviews APPROVED; human approval 2026-10-14)
- [x] Step 3 → agent-output/nordic-foods/03-des-diagram.py/.png/.svg and 03-des-adr-0001 to 0005 (diagram and five ADRs; no ADR review run, review_depth not deep)
- [x] Step 3.5 → agent-output/nordic-foods/04-governance-constraints.md/.json (discovery COMPLETE, schema valid; completed 2026-10-14 using pass-2 review via `--governance-review`)

## Key Decisions
- Region: swedencentral; GDPR, customer PII stays in the EU
- Budget: ~EUR 500/month across Dev + Prod (EUR 700 later); escalate to CTO/CFO if exceeded
- IaC tool: Terraform
- Pattern: N-Tier; containerized App Service, Azure SQL Database, Blob (LRS pinned), Key Vault, Container Registry
- Network: public web portal, private API (inbound private endpoint, public access disabled) and private data services; private DNS mandatory for every private endpoint; GitHub-hosted VNet runner with OIDC
- Availability: single-zone Prod accepted, but the 99.9% target is not waived; if unachievable, present availability/cost trade-off for sponsor approval
- GDPR: backups, logs and derived copies capped at 30 days; orders, invoices and receipts are a minimized 7-year exception
- Step 2: $348.77/month estimated (Azure-only for runner charges); WAF 7/5/6/8/6; Prod P0v3 x1 and SQL DTU S2, Dev P0v3 and S0 (repo feature floors); single instance is capacity-limited and not shown zone redundant
- Step 2: GDPR erasure and retention owner is Michal Sakac (field-mapping acceptance pending)

## Open Challenger Findings (must_fix only)
- No must_fix. Latest review: agent-output/nordic-foods/challenge-findings-governance-constraints-pass2.json (APPROVED, 0 findings; `--verify-cache` OK; sha256 a15afdc3…).
- should_fix f9bdb1b4 and e5f1c872 (pass 1) are closed by pass 2, severity unchanged; pass-1 sidecar stays stale and is not the selected review.

## Context for Next Step
- Open items carried forward (not closed by approval): sponsor decision on the 99.9% target; priced zone-redundant SKU from the repo matrix; Michal Sakac's acceptance of the GDPR field mapping; numeric SLAs and a timed SQL restore; maximum concurrent runners against 10.0.0.192/27; private DNS zone ownership against policy.
- Step 4 must include: App Service VNet image pull and AcrPull for ACR, a separate Terraform state bootstrap phase, application alert thresholds, diagnostics for ACR and network resources.
- Step 3 ADRs are Proposed and record approved decisions only; ADR-0004 documents the single-zone posture and leaves the 99.9% sponsor decision open.
- Next human handoff: `01-Orchestrator` (`resume nordic-foods`) to continue to Step 4 with `05-IaC Planner`. Completion used a separately authorized pass 2; the one-pass cap was not reset.
- Step 3.5 facts: subscription 7a2e8db9-42a4-4143-a9b5-c74fba49da74; 13 MG-inherited assignments; 4 Deny (3 AKS, NIC IP forwarding, none applicable); 72 DINE; 3 audit; 0 exemptions. No policy-enforced tags, locations or same-region rule (project choices only).
- Step 4 must verify: DINE `logAnalytics` is a literal all-zero GUID that does not resolve (real workspace, EU region, 30-day retention, duplicate-setting ownership); SQL auditing as best effort.
- discover.py now treats `AuditAction` as audit-class (test added; 110 tests pass). This tooling change is uncommitted and not yet signed off.
- 1-year reservation scope is left for Step 2. Peak duration, data growth, storage/log volumes are confirmed unknown; the Architect proposes the EUR/USD planning rate and sizing assumptions.

## Skill Context
- .github/skills/apex-azure-defaults/SKILL.md
- .github/instructions/references/iac-security-baseline.md

## Artifacts
- agent-output/nordic-foods/01-requirements.md
- agent-output/nordic-foods/sku-manifest.json
- agent-output/nordic-foods/sku-manifest.md
- agent-output/nordic-foods/challenge-findings-requirements.json
- agent-output/nordic-foods/challenge-findings-requirements-decisions.json
- agent-output/nordic-foods/02-architecture-assessment.md
- agent-output/nordic-foods/03-des-cost-estimate.md
- agent-output/nordic-foods/03-des-diagram.py
- agent-output/nordic-foods/03-des-diagram.png
- agent-output/nordic-foods/03-des-diagram.svg
- agent-output/nordic-foods/03-des-adr-0001 to 0005 (five ADR files)
- agent-output/nordic-foods/04-governance-constraints.md
- agent-output/nordic-foods/04-governance-constraints.json
- agent-output/nordic-foods/challenge-findings-governance-constraints-pass1.json
- agent-output/nordic-foods/challenge-findings-governance-constraints-decisions.json
- agent-output/nordic-foods/challenge-findings-architecture.json
- agent-output/nordic-foods/challenge-findings-cost-estimate.json
- agent-output/nordic-foods/README.md
