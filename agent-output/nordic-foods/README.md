<a id="readme-top"></a>

<div align="center">

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge)

![Step](https://img.shields.io/badge/Step-2%20of%207-blue?style=for-the-badge)

# 🏗️ nordic-foods

**FreshConnect MVP infrastructure for Nordic Fresh Foods, a farm-to-table delivery platform**

[View Architecture](#️-architecture) · [View Artifacts](#-generated-artifacts) · [View Progress](#-workflow-progress)

</div>

---

## 📋 Project Summary

| Property           | Value                                     |
| ------------------ | ----------------------------------------- |
| **Created**        | 2026-10-14                                |
| **Last Updated**   | 2026-10-14                                |
| **Region**         | swedencentral                             |
| **Environment**    | Dev + Production                          |
| **Estimated Cost** | ~$348.77/month (about EUR 317; budget ~EUR 500/month), approved |
| **AVM Coverage**   | Not yet assessed                          |

---

## ✅ Workflow Progress

```text
[██████░░░░░░░░░░░░░░] 30% Complete
```

| Step | Phase          |                                    Status                                     | Artifact                                   |
| :--: | -------------- | :---------------------------------------------------------------------------: | ------------------------------------------ |
|  1   | Requirements   |     ![Done](https://img.shields.io/badge/-Done-success?style=flat-square)     | [01-requirements.md](./01-requirements.md) |
|  2   | Architecture   |     ![Done](https://img.shields.io/badge/-Done-success?style=flat-square)     | [02-architecture-assessment.md](./02-architecture-assessment.md) |
|  3   | Design         | ![Pending](https://img.shields.io/badge/-Pending-lightgrey?style=flat-square) | 03-des-\*.md                               |
| 3.5  | Governance     | ![Pending](https://img.shields.io/badge/-Pending-lightgrey?style=flat-square) | 04-governance-constraints.md               |
|  4   | Planning       | ![Pending](https://img.shields.io/badge/-Pending-lightgrey?style=flat-square) | 04-implementation-plan.md                  |
|  5   | Implementation | ![Pending](https://img.shields.io/badge/-Pending-lightgrey?style=flat-square) | 05-implementation-reference.md            |
|  6   | Deployment     | ![Pending](https://img.shields.io/badge/-Pending-lightgrey?style=flat-square) | 06-deployment-summary.md                   |
|  7   | Documentation  | ![Pending](https://img.shields.io/badge/-Pending-lightgrey?style=flat-square) | 07-documentation-index.md                  |

> **Legend**:
> ![Done](https://img.shields.io/badge/-Done-success?style=flat-square) Complete
> | ![WIP](https://img.shields.io/badge/-WIP-yellow?style=flat-square) In Progress
> | ![Pending](https://img.shields.io/badge/-Pending-lightgrey?style=flat-square) Pending
> | ![Skip](https://img.shields.io/badge/-Skipped-blue?style=flat-square) Skipped

---

## 🏛️ Architecture

Architecture assessment and cost estimate approved on 2026-10-14 after current clean architecture and cost-feasibility reviews. Open items carried forward: the 99.9% sponsor decision, a priced zone-redundant SKU, GDPR field-mapping acceptance, numeric SLAs and a timed restore.

### Key Resources

| Resource                | Type                | SKU                         | Purpose                                              |
| ----------------------- | ------------------- | --------------------------- | ---------------------------------------------------- |
| app-plan-web            | App Service Plan    | Linux P0v3 Prod and Dev     | Public portal and private API apps                   |
| sql-db-core             | SQL Database        | DTU S2 Prod, S0 Dev         | Orders, customers, inventory, delivery schedules     |
| storage-data            | Storage Account     | Standard_LRS (user pin)     | Product images, invoices, delivery receipts          |

---

## 📄 Generated Artifacts

<details>
<summary><strong>📁 Step 1-3: Requirements, Architecture & Design</strong></summary>

| File                                      | Description                       |                                Status                                 | Created    |
| ----------------------------------------- | --------------------------------- | :-------------------------------------------------------------------: | ---------- |
| [01-requirements.md](./01-requirements.md) | Project requirements with NFRs    | ![Done](https://img.shields.io/badge/-Done-success?style=flat-square) | 2026-10-14 |
| [sku-manifest.md](./sku-manifest.md)       | SKU manifest (rendered from JSON) | ![Done](https://img.shields.io/badge/-Done-success?style=flat-square) | 2026-10-14 |
| [02-architecture-assessment.md](./02-architecture-assessment.md) | WAF assessment, SKU recommendations | ![Done](https://img.shields.io/badge/-Done-success?style=flat-square) | 2026-10-14 |
| [03-des-cost-estimate.md](./03-des-cost-estimate.md) | Worker-verified cost estimate | ![WIP](https://img.shields.io/badge/-WIP-yellow?style=flat-square) | 2026-10-14 |
| [02-waf-scores.png](./02-waf-scores.png) | WAF pillar score chart (SVG sibling) | ![WIP](https://img.shields.io/badge/-WIP-yellow?style=flat-square) | 2026-10-14 |
| [03-des-cost-distribution.png](./03-des-cost-distribution.png) | Cost distribution chart (SVG sibling) | ![WIP](https://img.shields.io/badge/-WIP-yellow?style=flat-square) | 2026-10-14 |
| [03-des-cost-projection.png](./03-des-cost-projection.png) | Cost projection chart (SVG sibling) | ![WIP](https://img.shields.io/badge/-WIP-yellow?style=flat-square) | 2026-10-14 |
| [03-des-sku-comparison.md](./03-des-sku-comparison.md) | SKU trade-off comparison (draft, unpriced; superseded by 02-sku-candidates.json prices) | ![WIP](https://img.shields.io/badge/-WIP-yellow?style=flat-square) | 2026-10-14 |
| [02-cost-estimate-v3.json](./02-cost-estimate-v3.json) | Worker pricing (manifest rev 3): services, endpoints, DNS | ![Done](https://img.shields.io/badge/-Done-success?style=flat-square) | 2026-10-14 |
| [02-cost-estimate-v2.json](./02-cost-estimate-v2.json) | Worker pricing (manifest rev 2, superseded by v3) | ![Skip](https://img.shields.io/badge/-Skipped-blue?style=flat-square) | 2026-10-14 |
| [02-cost-estimate-ancillary-v2.json](./02-cost-estimate-ancillary-v2.json) | Worker pricing: registry, Key Vault, logs, state storage | ![Done](https://img.shields.io/badge/-Done-success?style=flat-square) | 2026-10-14 |
| [02-sku-candidates.json](./02-sku-candidates.json) | Comparison-only candidate prices (worker FAILED status, partial) | ![WIP](https://img.shields.io/badge/-WIP-yellow?style=flat-square) | 2026-10-14 |

</details>

---

## 🔗 Related Resources

| Resource                | Path                                                                           |
| ----------------------- | ------------------------------------------------------------------------------ |
| **Terraform Templates** | [`infra/terraform/nordic-foods/`](../../infra/terraform/nordic-foods/)         |
| **Workflow Docs**       | [Published workflow guide](https://apexops.pro/concepts/workflow/)             |
| **Troubleshooting**     | [Published troubleshooting guide](https://apexops.pro/guides/troubleshooting/) |

---

<div align="center">

**Generated by [APEX](../../README.md)** · [Report Issue](https://github.com/jonathan-vella/apex/issues/new)

<a href="#readme-top">⬆️ Back to Top</a>

</div>
