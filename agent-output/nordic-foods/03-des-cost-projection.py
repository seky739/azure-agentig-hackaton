"""Six-month cost projection for nordic-foods (Step 2).

Flat run-rate: every Dev, Prod and shared resource is on a fixed-price SKU or tiny
usage meter, so no month-to-month growth is priced. The 3x seasonal peak is a
load-test question, not a priced scale-up. The Prod go-live month is not yet known,
so every month shows the full steady-state total as an upper bound.
"""

import sys
from pathlib import Path

import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = REPO_ROOT / ".github/skills/apex-python-diagrams/scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
from diagram_io import save_figure  # noqa: E402

MONTHS = ["Nov 2026", "Dec 2026", "Jan 2027", "Feb 2027", "Mar 2027", "Apr 2027"]
RUN_RATE = 348.7734  # cost-estimate-subagent totals: 297.6940 + 51.0794
WITH_RESERVATION = 326.1367  # RUN_RATE minus the worker-quantified Prod P0v3 1-year monthly saving 22.6367
BUDGET_INITIAL = 550.0  # EUR 500 at the approved 1.10 USD per EUR planning rate
BUDGET_LATER = 770.0  # EUR 700 at the same rate


def main() -> None:
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor("#F8F9FA")
    ax.set_facecolor("#F8F9FA")

    bars = ax.bar(MONTHS, [RUN_RATE] * len(MONTHS), color="#0078D4", width=0.55, label="Pay-as-you-go run-rate")
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, RUN_RATE + 8, f"${RUN_RATE:,.2f}", ha="center", fontsize=9, color="#1A1A2E")

    ax.plot(MONTHS, [WITH_RESERVATION] * len(MONTHS), color="#107C10", linewidth=2, marker="o", label=f"With 1-year P0v3 reservation (${WITH_RESERVATION:,.2f})")
    ax.axhline(BUDGET_INITIAL, color="#DC3545", linewidth=1.2, linestyle="--", label=f"Budget EUR 500 (about ${BUDGET_INITIAL:,.0f})")
    ax.axhline(BUDGET_LATER, color="#FFB900", linewidth=1.2, linestyle=":", label=f"Later budget EUR 700 (about ${BUDGET_LATER:,.0f})")

    ax.set_ylim(0, 850)
    ax.set_ylabel("USD per month", fontsize=10, color="#555")
    ax.set_title("nordic-foods: Six-Month Cost Projection (flat run-rate)", fontsize=13, fontweight="bold", color="#1A1A2E", pad=14)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#E0E0E0", linewidth=0.8, alpha=0.7)
    ax.legend(fontsize=9, loc="upper left", framealpha=0.9, edgecolor="#CCC")

    plt.tight_layout(pad=1.4)
    out = Path(__file__).resolve().parent / "03-des-cost-projection"
    save_figure(fig, str(out), bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()
    print(f"Generated: {out}.png (+ .svg sibling)")


if __name__ == "__main__":
    main()
