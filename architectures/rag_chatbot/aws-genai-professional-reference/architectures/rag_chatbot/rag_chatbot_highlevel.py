from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import APIGateway, CloudFront
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.ml import Bedrock, SagemakerModel
from diagrams.aws.security import Cognito, IAM
from diagrams.aws.analytics import AmazonOpensearchService
from diagrams.aws.management import Cloudwatch
from diagrams.aws.integration import SQS, Eventbridge

with Diagram(
    "High-Level RAG Chatbot Architecture (AWS Managed)",
    show=False,
    direction="LR",
    filename="aws-genai-professional-reference/architectures/rag_chatbot/rag_chatbot_highlevel",
    graph_attr={"rankdir": "LR", "size": "22,14", "splines": "ortho", "nodesep": "0.8"},
):
    # ── Layer 1: User Interface ───────────────────────────────────────────────
    with Cluster("User Interface Layer"):
        cdn = CloudFront("CloudFront\n(Chat UI)")
        ui_bucket = S3("S3\n(Static Assets)")
        cdn >> Edge(style="dashed") >> ui_bucket

    # ── Layer 2: Orchestration ────────────────────────────────────────────────
    with Cluster("Orchestration Layer"):
        cognito = Cognito("Cognito\n(User Pool)")
        apigw = APIGateway("API Gateway\n(REST / WebSocket)")
        chat_lambda = Lambda("Chat\nOrchestrator")
        guardrails = Bedrock("Bedrock\nGuardrails")
        agent = Bedrock("Bedrock Agent\n(RetrieveAndGenerate)")
        session_db = Dynamodb("DynamoDB\n(Conversation\nHistory)")

    # ── Layer 3: Retrieval ────────────────────────────────────────────────────
    with Cluster("Retrieval Layer"):
        kb = Bedrock("Bedrock\nKnowledge Base")
        embeddings = SagemakerModel("Titan\nEmbeddings")
        vector_store = AmazonOpensearchService("OpenSearch\nServerless\n(Vector Index)")

    # ── Layer 4: Model / Inference ────────────────────────────────────────────
    with Cluster("Model / Inference Layer"):
        llm = Bedrock("Foundation Model\n(Claude / Titan)")

    # ── Layer 5: Data ─────────────────────────────────────────────────────────
    with Cluster("Data Layer"):
        doc_store = S3("S3\n(Source Documents)")
        event_bus = Eventbridge("EventBridge\n(S3 Trigger)")
        ingest_queue = SQS("SQS\n(Backpressure)")
        ingest_lambda = Lambda("Ingestion\nPipeline")

    # ── Cross-cutting ─────────────────────────────────────────────────────────
    logs = Cloudwatch("CloudWatch\n(Logs & Metrics)")
    iam = IAM("IAM\n(Least Privilege)")

    # ── Query Flow (numbered) ─────────────────────────────────────────────────
    cdn >> Edge(label="1. User query") >> cognito
    cognito >> Edge(label="2. JWT token") >> apigw
    apigw >> Edge(label="3. Invoke") >> chat_lambda
    chat_lambda >> Edge(label="4. Load history") >> session_db
    chat_lambda >> Edge(label="5. Apply guardrails") >> guardrails
    guardrails >> Edge(label="6. Safe prompt") >> agent
    agent >> Edge(label="7. Retrieve") >> kb
    kb >> Edge(label="8. Embed query") >> embeddings
    embeddings >> Edge(label="9. Semantic search") >> vector_store
    vector_store >> Edge(label="10. Relevant chunks") >> llm
    llm >> Edge(label="11. Generated response") >> agent
    agent >> Edge(label="12. Response") >> chat_lambda
    chat_lambda >> Edge(label="13. Save turn") >> session_db
    chat_lambda >> Edge(label="14. Return") >> apigw

    # ── Ingestion Flow (dashed) ───────────────────────────────────────────────
    doc_store >> Edge(label="Upload event", style="dashed") >> event_bus
    event_bus >> Edge(label="Trigger", style="dashed") >> ingest_queue
    ingest_queue >> Edge(label="Process", style="dashed") >> ingest_lambda
    ingest_lambda >> Edge(label="Chunk + embed", style="dashed") >> embeddings
    ingest_lambda >> Edge(label="Store vectors", style="dashed") >> vector_store

    # ── Observability ─────────────────────────────────────────────────────────
    chat_lambda >> Edge(label="Log", style="dotted") >> logs
    agent >> Edge(label="Log", style="dotted") >> logs
    ingest_lambda >> Edge(label="Log", style="dotted") >> logs
    iam >> Edge(style="dotted") >> agent
    iam >> Edge(style="dotted") >> kb
