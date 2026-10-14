"""Step 3 architecture diagram for nordic-foods (source: 02-architecture-assessment.md)."""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / ".github/skills/apex-python-diagrams/scripts"))

from diagram_io import diagram_kwargs, embed_svg_images  # noqa: E402
from diagrams import Cluster, Diagram, Edge  # noqa: E402
from diagrams.azure.compute import AppServices, ContainerRegistries  # noqa: E402
from diagrams.azure.database import SQLDatabases  # noqa: E402
from diagrams.azure.devops import Pipelines  # noqa: E402
from diagrams.azure.identity import ActiveDirectory  # noqa: E402
from diagrams.azure.monitor import ApplicationInsights, LogAnalyticsWorkspaces  # noqa: E402
from diagrams.azure.network import DNSPrivateZones, PrivateEndpoint  # noqa: E402
from diagrams.azure.security import KeyVaults  # noqa: E402
from diagrams.azure.storage import StorageAccounts  # noqa: E402
from diagrams.onprem.client import Users  # noqa: E402

OUTPUT = HERE / "03-des-diagram"

graph_attr = {
    "bgcolor": "white",
    "pad": "0.8",
    "nodesep": "0.7",
    "ranksep": "1.0",
    "splines": "spline",
    "fontname": "Arial Bold",
    "fontsize": "16",
    "dpi": "150",
    "labelloc": "t",
}
node_attr = {"fontname": "Arial Bold", "fontsize": "11", "labelloc": "t"}
cluster_style = {"margin": "30", "fontname": "Arial Bold", "fontsize": "14"}

with Diagram(
    "nordic-foods - FreshConnect MVP (swedencentral, Prod detail; Dev mirrors Prod)",
    **diagram_kwargs(OUTPUT, direction="TB", graph_attr=graph_attr, node_attr=node_attr),
):
    users = Users("Consumers and\nrestaurants\n(HTTPS)")
    entra = ActiveDirectory("Entra External ID\n(customer sign-in)")

    with Cluster("VNet 10.0.0.0/16 (NSG per subnet)", graph_attr=cluster_style):
        with Cluster("snet app-integration-prod 10.0.0.0/26", graph_attr=cluster_style):
            portal = AppServices("Portal app\nP0v3 x1\npublic HTTPS")
            api = AppServices("API app\nsame plan\nprivate only")

        with Cluster("snet private-endpoints-prod-shared 10.0.0.128/27", graph_attr=cluster_style):
            pe_api = PrivateEndpoint("PE: API")
            pe_sql = PrivateEndpoint("PE: SQL")
            pe_blob = PrivateEndpoint("PE: Blob")
            pe_kv = PrivateEndpoint("PE: Key Vault")
            pe_acr = PrivateEndpoint("PE: Container\nRegistry (shared)")
            pe_state = PrivateEndpoint("PE: Terraform\nstate (shared)")

        with Cluster("snet github-runner 10.0.0.192/27", graph_attr=cluster_style):
            runner = Pipelines("GitHub-hosted runner\n(OIDC, VNet-delegated)")

        dev = AppServices("Dev: apps on P0v3 x1\n10.0.0.64/26 + 10.0.0.160/27\nSQL S0, Blob, Key Vault via 4 PEs")
        dns = DNSPrivateZones("5 private DNS zones\nlinked to the VNet")

    with Cluster("Data and platform services (public access disabled)", graph_attr=cluster_style):
        sql = SQLDatabases("Azure SQL DTU S2\nEntra-only, Local backup")
        blob = StorageAccounts("Blob Standard_LRS\n(user pin)")
        kv = KeyVaults("Key Vault Standard")
        acr = ContainerRegistries("Container Registry\nPremium, admin off")
        state = StorageAccounts("Terraform state\nStandard_LRS")

    with Cluster("Monitoring (30-day retention)", graph_attr=cluster_style):
        insights = ApplicationInsights("Application Insights\n(workspace-based)")
        workspace = LogAnalyticsWorkspaces("Log Analytics")

    users >> Edge(label="HTTPS") >> portal
    entra >> Edge(style="dashed", label="sign-in") >> portal
    portal >> Edge(label="server-side via\nVNet integration") >> pe_api >> api
    api >> pe_sql >> sql
    api >> pe_blob >> blob
    api >> pe_kv >> kv
    runner >> Edge(label="push image") >> pe_acr >> acr
    runner >> Edge(label="state backend") >> pe_state >> state
    acr >> Edge(style="dashed", label="VNet image pull\n(AcrPull)") >> portal
    portal >> insights
    api >> insights
    insights >> workspace

embed_svg_images(OUTPUT.with_suffix(".svg"))
