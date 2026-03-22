from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.analytics import AmazonOpensearchService
from diagrams.aws.database import Dynamodb
from diagrams.aws.ml import Bedrock
from diagrams.aws.management import Cloudwatch

with Diagram("RAG Query Flow", show=False, direction="LR", graph_attr={"rankdir": "LR", "size": "14,8"}):
    
    # Input
    with Cluster("Input"):
        user = APIGateway("API Gateway\n(User Query)")
    
    # Processing
    with Cluster("Processing"):
        query_lambda = Lambda("Query\nHandler")
    
    # Retrieval
    with Cluster("Retrieval"):
        vector_db = AmazonOpensearchService("OpenSearch\n(Vector DB)")
        state = Dynamodb("DynamoDB\n(Conversation\nState)")
    
    # AI/ML
    with Cluster("AI/ML"):
        bedrock = Bedrock("Bedrock\n(LLM)")
    
    # Output
    with Cluster("Output"):
        response = APIGateway("Response\nto User")
    
    # Monitoring
    logs = Cloudwatch("CloudWatch\n(Logs)")
    
    # Query Flow with numbered steps
    user >> Edge(label="1. Submit Query") >> query_lambda
    query_lambda >> Edge(label="2. Retrieve\nVectors") >> vector_db
    query_lambda >> Edge(label="3. Get\nContext") >> state
    vector_db >> Edge(label="4. Relevant\nChunks") >> bedrock
    state >> Edge(label="5. History") >> bedrock
    bedrock >> Edge(label="6. Generated\nResponse") >> query_lambda
    query_lambda >> Edge(label="7. Update\nState") >> state
    query_lambda >> Edge(label="8. Return\nResponse") >> response
    
    # Monitoring
    query_lambda >> Edge(label="Log", style="dotted") >> logs
    bedrock >> Edge(label="Log", style="dotted") >> logs
