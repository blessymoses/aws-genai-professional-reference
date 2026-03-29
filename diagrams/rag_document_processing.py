from diagrams import Diagram, Cluster, Edge
from diagrams.aws.storage import S3
from diagrams.aws.integration import Eventbridge, SQS
from diagrams.aws.compute import Lambda
from diagrams.aws.analytics import AmazonOpensearchService
from diagrams.aws.management import Cloudwatch

with Diagram("RAG Document Processing Flow", show=False, direction="LR", graph_attr={"rankdir": "LR", "size": "14,8"}):
    
    # Input
    with Cluster("Input"):
        documents = S3("S3\n(Document\nUpload)")
    
    # Triggering
    with Cluster("Triggering"):
        event_bridge = Eventbridge("EventBridge\n(S3 Event)")
    
    # Processing
    with Cluster("Processing"):
        ingest_lambda = Lambda("Document\nIngestion")
    
    # Storage
    with Cluster("Storage"):
        vector_db = AmazonOpensearchService("OpenSearch\n(Vector DB)")
        queue = SQS("SQS\n(Processing\nQueue)")
    
    # Monitoring
    logs = Cloudwatch("CloudWatch\n(Logs)")
    
    # Document Processing Flow with numbered steps
    documents >> Edge(label="1. New\nDocument") >> event_bridge
    event_bridge >> Edge(label="2. Trigger\nEvent") >> ingest_lambda
    ingest_lambda >> Edge(label="3. Extract\nText") >> ingest_lambda
    ingest_lambda >> Edge(label="4. Chunk\nDocument") >> ingest_lambda
    ingest_lambda >> Edge(label="5. Generate\nEmbeddings") >> ingest_lambda
    ingest_lambda >> Edge(label="6. Store\nVectors") >> vector_db
    ingest_lambda >> Edge(label="7. Queue\nMetadata") >> queue
    
    # Monitoring
    ingest_lambda >> Edge(label="Log", style="dotted") >> logs
    event_bridge >> Edge(label="Log", style="dotted") >> logs
