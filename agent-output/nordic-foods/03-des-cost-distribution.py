"""Monthly cost distribution donut for nordic-foods (Step 2).

Category values are sums of cost-estimate-subagent line items from
02-cost-estimate-v3.json and 02-cost-estimate-ancillary-v2.json (USD/month).
"""

import sys
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = REPO_ROOT / ".github/skills/apex-python-diagrams/scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
from diagram_io import save_figure  # noqa: E402

# App Service 64.97 + 64.97; SQL 73.60833 + 14.71863 + Blob 2.7 + 0.227 + tfstate 0.027;
# Private endpoints 73.00 + 0.60 data + DNS 2.50 + 0.40; ACR 50.69242 + Key Vault 0.36 + Log Analytics 0.
CATEGORIES = {
    "Compute (App Service)": 129.94,
    "Data services (SQL, Blob)": 91.2810,
    "Networking (private endpoints, DNS)": 76.50,
    "Platform (Registry, Key Vault, Logs)": 51.0524,
}
TOTAL = 348.7734


def main() -> None:
    palette = ["#0078D4", "#50E6FF", "#1490DF", "#773ADC"]
    labels = list(CATEGORIES)
    values = list(CATEGORIES.values())
    pcts = [v / sum(values) * 100 for v in values]

    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor("#F8F9FA")
    ax.set_facecolor("#F8F9FA")

    ax.pie(values, colors=palette, wedgeprops={"linewidth": 2, "edgecolor": "#F8F9FA"}, startangle=140)
    ax.add_patch(plt.Circle((0, 0), 0.60, fc="#F8F9FA"))
    ax.text(0, 0.07, f"${TOTAL:,.2f}", ha="center", va="center", fontsize=17, fontweight="bold", color="#1A1A2E")
    ax.text(0, -0.17, "/ month (Dev + Prod + shared)", ha="center", va="center", fontsize=9, color="#666")

    legend = [f"{lbl}  ${val:,.2f}  ({pct:.0f}%)" for lbl, val, pct in zip(labels, values, pcts)]
    handles = [mpatches.Patch(color=c, label=l) for c, l in zip(palette, legend)]
    ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, -0.18), ncol=1, fontsize=9, framealpha=0.0)
    ax.set_title("nordic-foods: Monthly Cost Distribution (USD)", fontsize=13, fontweight="bold", color="#1A1A2E", pad=10)

    plt.tight_layout(pad=1.4)
    out = Path(__file__).resolve().parent / "03-des-cost-distribution"
    save_figure(fig, str(out), bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()
    print(f"Generated: {out}.png (+ .svg sibling)")


if __name__ == "__main__":
    main()
