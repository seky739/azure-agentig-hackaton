# nordic-foods — Handoff (Step 2 complete; ready for Step 3 or 3.5)
Updated: 2026-10-14 | IaC: Terraform | Branch: n/a

## Completed Steps
- [x] Step 1 → agent-output/nordic-foods/01-requirements.md (review approved; Gate 1 approved)
- [x] Step 2 → agent-output/nordic-foods/02-architecture-assessment.md and 03-des-cost-estimate.md (architecture and cost-feasibility reviews APPROVED; human approval 2026-10-14)

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
- None

## Context for Next Step
- Open items carried forward (not closed by approval): sponsor decision on the 99.9% target; priced zone-redundant SKU from the repo matrix; Michal Sakac's acceptance of the GDPR field mapping; numeric SLAs and a timed SQL restore; maximum concurrent runners against 10.0.0.192/27; private DNS zone ownership against policy.
- Step 4 must include: App Service VNet image pull and AcrPull for ACR, a separate Terraform state bootstrap phase, application alert thresholds, diagnostics for ACR and network resources.
- Next human handoff: Design (Step 3) when not skipped, then Governance Discovery (Step 3.5).
- Run the Step 2 architecture assessment and the independent cost-feasibility review against the EUR 500 budget and the private-endpoint baseline (done).
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
- agent-output/nordic-foods/challenge-findings-architecture.json
- agent-output/nordic-foods/challenge-findings-cost-estimate.json
- agent-output/nordic-foods/README.md
