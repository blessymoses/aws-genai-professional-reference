from diagrams import Diagram, Cluster, Edge
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import SQS, Eventbridge
from diagrams.aws.ml import Transcribe, Bedrock
from diagrams.aws.database import Redshift
from diagrams.aws.management import Cloudwatch
from diagrams.aws.general import General

with Diagram(
    "Audio Analysis Solution using AWS Transcribe",
    show=False,
    direction="LR",
    filename="audio_analysis_architecture",
    graph_attr={"rankdir": "LR", "size": "18,10"},
):

    # External source
    nas = General("NAS Folder\n(On-Prem)")

    with Cluster("File Ingestion"):
        s3_raw = S3("S3\n(Raw Audio)")
        ingest_lambda = Lambda("Move File\nfor Processing")
        s3_curated = S3("S3\n(Curated)")

    with Cluster("Speech To Text\n(SQS-controlled concurrency ≤150)"):
        sqs_transcribe = SQS("SQS\n(Transcribe Queue)")
        transcribe_lambda = Lambda("Invoke\nTranscribe")
        transcribe = Transcribe("AWS\nTranscribe")
        s3_transcribed = S3("S3\n(Transcribed)")

    with Cluster("Evaluation\n(SQS rate-limited → Bedrock Batch)"):
        sqs_eval = SQS("SQS\n(Eval Queue)")
        eval_lambda = Lambda("Invoke\nLLM")
        bedrock = Bedrock("Bedrock\nBatch API")
        s3_output = S3("S3\n(Output)")

    with Cluster("Serving"):
        redshift = Redshift("Redshift")

    # Monitoring
    cw = Cloudwatch("CloudWatch\n(Logs & Alarms)")

    # Flow
    nas >> Edge(label="SFTP") >> s3_raw
    s3_raw >> ingest_lambda >> s3_curated

    s3_curated >> Edge(label="S3 Event") >> sqs_transcribe
    sqs_transcribe >> Edge(label="MaxConcurrency=150") >> transcribe_lambda
    transcribe_lambda >> transcribe
    transcribe >> Edge(label="Transcript") >> s3_transcribed

    s3_transcribed >> Edge(label="S3 Event") >> sqs_eval
    sqs_eval >> Edge(label="Rate-limited") >> eval_lambda
    eval_lambda >> Edge(label="Batch Job") >> bedrock
    bedrock >> Edge(label="Results") >> s3_output

    s3_output >> redshift

    # Monitoring
    transcribe_lambda >> Edge(style="dotted", label="Log") >> cw
    eval_lambda >> Edge(style="dotted", label="Log") >> cw
    sqs_transcribe >> Edge(style="dotted", label="Queue Depth") >> cw
    sqs_eval >> Edge(style="dotted", label="Queue Depth") >> cw
