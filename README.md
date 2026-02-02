# AWS Certified Generative AI – Professional  
## Study Priority Checklist

> This checklist is ordered by **exam domain weightage and real question frequency**.  
> If time is limited, complete **Tier 0 → Tier 1 first**.

---

## Tier 0 — MUST MASTER (Non‑Negotiable)

### Amazon Bedrock (Core)
- [ ] On‑demand vs Provisioned Throughput
- [ ] Cross‑Region inference vs Provisioned throughput trade‑offs
- [ ] Streaming vs non‑streaming inference
- [ ] Inference parameters (temperature, top‑k, stop sequences)
- [ ] Invocation logging vs guardrail tracing
- [ ] IAM enforcement (InvokeModel, Converse, Guardrails)

### Amazon Bedrock Advanced Features
- [ ] Bedrock AgentCore (agent runtime, tool orchestration)
- [ ] Prompt Management (versioning, reuse, governance)
- [ ] Prompt Flows (prompt chaining, controlled execution)
- [ ] Amazon Titan models (native FM trade-offs)

### Amazon Bedrock Knowledge Bases
- [ ] RAG architecture (S3 → chunking → embeddings → vector store)
- [ ] Event‑driven vs scheduled ingestion
- [ ] Ingest vs delete APIs
- [ ] Hybrid search vs vector‑only search
- [ ] Reranking vs retrieval
- [ ] Why Knowledge Bases ≠ ETL

### AWS Lambda
- [ ] Pre/post‑processing glue for GenAI
- [ ] Stateless vs stateful (DynamoDB)
- [ ] Event‑driven vs synchronous invocation
- [ ] Why Lambda > EC2 for GenAI glue logic

### Amazon EventBridge
- [ ] Near real‑time = event‑driven (not scheduled)
- [ ] Fan‑out without code changes
- [ ] EventBridge vs SQS (routing vs buffering)
- [ ] Webhook ingestion patterns
- [ ] Least‑ops integration scenarios

### Amazon SQS
- [ ] Buffering and decoupling for asynchronous GenAI workflows
- [ ] Backpressure handling for inference pipelines
- [ ] SQS vs EventBridge (buffering vs routing)
- [ ] When SQS is preferred over SNS or direct Lambda invocation

### AWS Step Functions
- [ ] Orchestrator vs worker pattern
- [ ] Sequential validation & ordering questions
- [ ] Human approval & quality gates
- [ ] Agent workflows & governance flows

---

## Tier 1 — VERY HIGH PRIORITY

### Amazon OpenSearch Service
- [ ] Vector search fundamentals
- [ ] Hybrid (keyword + vector) search
- [ ] Reranking use cases
- [ ] OpenSearch vs pgvector vs Kendra

### Amazon SageMaker AI
- [ ] Real‑time vs async vs batch inference
- [ ] Async inference (large payloads, long runtime)
- [ ] JumpStart vs custom models
- [ ] Why SageMaker ≠ default when Bedrock exists

### Bedrock Guardrails
- [ ] Input vs output guardrails
- [ ] Guardrail tracing (why content was blocked)
- [ ] GuardrailPolicyType metrics
- [ ] Guardrails vs prompts (exam trap)

### Amazon Kendra
- [ ] Enterprise search vs vector DBs
- [ ] Regulated / compliance‑heavy workloads
- [ ] When Kendra > OpenSearch

### Amazon Augmented AI (A2I)
- [ ] Human-in-the-loop review for low-confidence or high-risk AI outputs
- [ ] Integration with Bedrock / SageMaker for compliance workflows
- [ ] Approval gates vs fully automated pipelines
- [ ] When A2I is required for regulatory or safety reasons

### Amazon Comprehend
- [ ] PII detection vs redaction
- [ ] Comprehend vs Macie (common trap)
- [ ] Pre‑processing before LLM calls

### Amazon S3
- [ ] Event notifications vs lifecycle rules
- [ ] Metadata vs tags vs object attributes
- [ ] Near real‑time ingestion patterns
- [ ] Why lifecycle ≠ real‑time

### Amazon DynamoDB (+ Streams)
- [ ] Conversation state storage
- [ ] Agent memory
- [ ] Event‑driven updates with Streams

### Amazon CloudWatch & Logs
- [ ] Knowledge Base ingestion logs
- [ ] Guardrail metrics vs invocation logs
- [ ] What CloudTrail does NOT show

### Amazon Q Developer
- [ ] Code generation & refactoring
- [ ] CI/CD integration
- [ ] Why manual review workflows are incorrect

### Amazon Q Business
- [ ] Enterprise knowledge access and permissions
- [ ] Q Business vs custom RAG with Bedrock
- [ ] Q Business Apps use cases

### Amazon Lex
- [ ] Conversational interfaces with LLM backends
- [ ] Lex vs Bedrock Agents

---

## Tier 2 — MEDIUM PRIORITY (Know When NOT to Choose)

- [ ] AWS X-Ray
- [ ] Amazon QuickSight
- [ ] Amazon Neptune
- [ ] Amazon SNS
- [ ] AWS Glue (deterministic ETL)
- [ ] Amazon Athena (analytics, not inference)
- [ ] Amazon Transcribe (audio → text)
- [ ] Amazon Textract (documents → text)
- [ ] Amazon Rekognition (vision)
- [ ] Amazon MSK / Kinesis (streaming vs EventBridge)
- [ ] Aurora / RDS / pgvector (DIY RAG traps)
- [ ] Amazon ElastiCache (semantic caching)
- [ ] AWS AppConfig (runtime config)
- [ ] ECS / EKS / Fargate (deployment context)
- [ ] Amazon AppFlow (SaaS ingestion into GenAI pipelines)
- [ ] Amazon EMR (large-scale batch processing, not real-time GenAI)
- [ ] AWS App Runner (simple container hosting)
- [ ] AWS Lambda@Edge (latency-sensitive edge inference)
- [ ] AWS Outposts (on-prem constraints)
- [ ] AWS Wavelength (edge / telco scenarios)
- [ ] AWS Fargate (serverless containers)
- [ ] AWS CodeBuild (build automation for GenAI pipelines)
- [ ] AWS CodeDeploy (deployment automation, not GenAI-specific)
- [ ] AWS CodePipeline (CI/CD orchestration context)
- [ ] Amazon SageMaker Model Monitor (model drift and data quality monitoring)
- [ ] Amazon SageMaker JumpStart (prebuilt models and solutions)

---

## Tier 3 — LOW PRIORITY

- [ ] Amazon Connect
- [ ] SageMaker Clarify
- [ ] SageMaker Neo
- [ ] SageMaker Ground Truth
- [ ] AWS CDK / CloudFormation
- [ ] Amazon SageMaker Data Wrangler
- [ ] Amazon SageMaker Model Registry
- [ ] Amazon SageMaker Processing
- [ ] Amazon SageMaker Unified Studio
- [ ] AWS Auto Scaling
- [ ] AWS Chatbot
- [ ] AWS Amplify
- [ ] AWS CodeArtifact
- [ ] AWS Tools and SDKs
- [ ] Amazon EC2 (custom hosting, higher ops)
- [ ] Amazon ECR (container registry)
- [ ] Amazon ECS (container orchestration)
- [ ] Amazon EKS (Kubernetes-based platforms)

---