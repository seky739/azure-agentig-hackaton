# 📦 SKU Manifest - nordic-foods

![Artifact](https://img.shields.io/badge/Artifact-SKU%20Manifest-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Draft-orange?style=for-the-badge)
![Schema](https://img.shields.io/badge/Schema-sku--manifest--v1-purple?style=for-the-badge)

<details open>
<summary><strong>📑 Manifest Contents</strong></summary>

- [Overview](#overview)
- [Environments](#environments)
- [Services](#services)
- [Revision History](#revision-history)
- [Open Substitutions](#open-substitutions)

</details>

> Rendered from `sku-manifest.json` (rev 3) by `tools/scripts/render-sku-manifest-md.mjs`.
>
> **Do not hand-edit this file.** Mutate `sku-manifest.json` and re-run
> the renderer (wired into lefthook + CI). Authoring rules:
> [`.github/instructions/sku-manifest.instructions.md`](../../.github/instructions/sku-manifest.instructions.md).

## Overview

| Field            | Value                                                      |
| ---------------- | ---------------------------------------------------------- |
| Project          | `nordic-foods`                                        |
| Default region   | `swedencentral` (per-service `regions[]` inherits this) |
| Schema version   | `sku-manifest-v1`                                          |
| Current revision | `3`                               |
| Last updated     | `2026-10-14T12:45:00Z`                                     |
| Environments     | `dev, prod` (comma-separated)                              |
| Service count    | `3`                                        |

**Scope**: creative SKU decisions only — App Service plans, VMs/VMSS, SQL,
Cosmos, AKS pools, Redis, APIM, App Gateway, Storage replication tiers.

**Out of scope** (do not add to `services[]`): bandwidth, Log Analytics,
vnet, subnet, NSG, route table, public IP, diagnostics. See
[`.github/instructions/sku-manifest.instructions.md`](../../.github/instructions/sku-manifest.instructions.md).

## Environments

| Environment | In scope | Notes |
| ----------- | -------- | ----- |
| `dev` | ✅ | — |
| `prod` | ✅ | — |

## Services

> Rendered from `sku-manifest.json` `services[]`. Per-environment values
> reflect `environment_overrides` on top of the base entry.

| `id` | Service | Size (base) | Capacity | Zonal | Regions | SLA target / achieved | Commitment | Source | Rev |
| ---- | ------- | ----------- | -------- | ----- | ------- | --------------------- | ---------- | ------ | --- |
| `app-plan-web` | App Service Plan | `P0v3` | `fixed (default 1)` | ❌ | `swedencentral` | `99.9%` / `—` | `on-demand` | `architect-derived` | `3` |
| `sql-db-core` | SQL Database | `S2` | `fixed (default 1)` | ❌ | `swedencentral` | `99.9%` / `—` | `on-demand` | `architect-derived` | `3` |
| `storage-data` | Storage Account | `Standard_LRS` | `fixed (default 1)` | ❌ | `swedencentral` | `99.9%` / `—` | `on-demand` | `user-pin` | `1` |

### Per-environment overrides

Only services with non-empty `environment_overrides` appear below.

| `id` | Env | Size | Capacity | Zonal | Regions | Commitment | Notes |
| ---- | --- | ---- | -------- | ----- | ------- | ---------- | ----- |
| `sql-db-core` | `dev` | `S0` | `fixed (default 1)` | ❌ | `swedencentral` | `on-demand` | — |

### Feature requirements

| `id` | `requires[]` | Verified at Step 4 |
| ---- | ------------ | ------------------ |
| `app-plan-web` | `vnet-integration`, `private-endpoints`, `managed-identity` | ✅ / ❌ |
| `sql-db-core` | `private-endpoints`, `managed-identity` | ✅ / ❌ |
| `storage-data` | `private-endpoints` | ✅ / ❌ |

### Cost estimate (USD/month)

> Populated by `cost-estimate-subagent` via `manifest_writeback[]` —
> Architect never types prices from parametric knowledge.

| `id` | `cost_estimate_monthly_usd` | Confidence |
| ---- | --------------------------- | ---------- |
| `app-plan-web` | `$129.94` | `—` |
| `sql-db-core` | `$88.33` | `—` |
| `storage-data` | `$2.93` | `—` |

## Revision History

> Append-only. Each row is metadata about a git commit / apex-recall checkpoint.

| `rev` | Step | Agent | Created (UTC) | Summary | Changed `id`s | Commit | Checkpoint |
| ----- | ---- | ----- | ------------- | ------- | ------------- | ------ | ---------- |
| `1` | `1` | `02-Requirements` | `2026-10-14T08:55:00Z` | Initial user pins: Storage Account replication pinned to LRS; no other SKU preferences. | `storage-data` | — | `nordic-foods:1:phase_5_artifact` |
| `2` | `2` | `03-Architect` | `2026-10-14T11:40:00Z` | Architect-derived App Service plan (P0v3 Prod, B1 Dev) and SQL Database (DTU S2 Prod, Basic Dev), approved at the SKU confirmation gate; storage-data pin preserved. | `app-plan-web`, `sql-db-core` | — | `nordic-foods:2:phase_4_sku_authoring` |
| `3` | `2` | `03-Architect` | `2026-10-14T12:45:00Z` | Accepted must-fix 4ba8c7d4: Dev App Service plan moves from B1 to P0v3 and Dev SQL from Basic to DTU S0 so the vnet-integration and private-endpoints feature floors hold; re-confirmed at the SKU gate. | `app-plan-web`, `sql-db-core` | — | `nordic-foods:2:phase_6_challenger_pass1` |

## Open Substitutions

> Captured at Step 6 (Deploy) when a planned SKU is unavailable due to
> quota / region capacity. Mirrors `decisions.sku_overrides[]` in
> `00-session-state.json`.

> **None open** — all SKUs deployed as planned.

---

## References

- Schema: [`tools/schemas/sku-manifest.schema.json`](../../tools/schemas/sku-manifest.schema.json)
- Authoring rules: [`.github/instructions/sku-manifest.instructions.md`](../../.github/instructions/sku-manifest.instructions.md)
- Renderer: `node tools/scripts/render-sku-manifest-md.mjs <project>`
- Validators: `npm run validate:sku-manifest` + `npm run validate:sku-iac-coverage`
