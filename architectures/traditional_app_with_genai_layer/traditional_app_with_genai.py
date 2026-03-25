from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import ALB
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.analytics import AmazonOpensearchService
from diagrams.aws.ml import Bedrock
from diagrams.aws.compute import Lambda
from diagrams.onprem.client import User

with Diagram(
    "Traditional Application Extended by GenAI Layer",
    show=False,
    direction="LR",
    graph_attr={"rankdir": "LR", "size": "18,8", "splines": "ortho"},
    filename="aws-genai-professional-reference/architectures/traditional_app_with_genai_layer/traditional_app_with_genai",
):
    user = User("User")

    # Traditional application tier
    with Cluster("Traditional Application"):
        alb = ALB("Load Balancer\n(ALB)")
        app_server = EC2("App Server")
        db = RDS("Traditional\nDatabase")

    # GenAI extension tier
    with Cluster("New GenAI Components"):
        orchestrator = Lambda("Context\nOrchestrator")

        with Cluster("Retrieval"):
            vector_db = AmazonOpensearchService("Vector Database\n(OpenSearch)")

        with Cluster("Inference"):
            model = Bedrock("Model Layer\n(Bedrock)")

    # Traditional flow
    user >> Edge(label="Request") >> alb
    alb >> Edge(label="Route traffic") >> app_server
    app_server >> Edge(label="Read/write data") >> db

    # GenAI extension
    db >> Edge(label="Prompt request", style="dashed") >> orchestrator
    orchestrator >> Edge(label="Semantic search", style="dashed") >> vector_db
    orchestrator >> Edge(label="Inference", style="dashed") >> model
