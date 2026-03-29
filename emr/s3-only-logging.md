# S3-Only Logging Configuration for Glue and EMR Jobs

How to route all Spark/EMR logs to S3 and disable CloudWatch log streaming.

---

## AWS Glue (PySpark) — S3-Only Logging

### What to remove

```json
"--enable-continuous-cloudwatch-log": "true"
```

This is the only parameter that streams real-time driver/executor logs to CloudWatch log groups. Removing it stops log storage in CloudWatch entirely.

### Final configuration

```json
{
  "DefaultArguments": {
    "--enable-spark-ui": "true",
    "--spark-event-logs-path": "s3://aws-glue-assets-264373394510-ap-southeast-1/sparkHistoryLogs/",
    "--enable-metrics": "true"
  }
}
```

### What each parameter does

| Parameter | Purpose | CloudWatch? |
|---|---|---|
| `--enable-spark-ui` | Enables Spark UI monitoring | No |
| `--spark-event-logs-path` | Writes Spark event logs to S3 every 30s | No — S3 only |
| `--enable-metrics` | Sends job profiling **metrics** to CloudWatch | Yes (metrics only, not logs) |

### Notes

- `--enable-spark-ui` + `--spark-event-logs-path` together give you full Spark History Server access — stage timelines, task metrics, executor logs — all from S3.
- `--enable-metrics` pushes metrics (not logs) to CloudWatch. Remove it too if you want zero CloudWatch interaction. Keep it if you want job profiling dashboards without log storage costs.
- `--enable-job-insights` defaults to `true` in Glue 2.0/3.0 and also writes to CloudWatch. Explicitly disable it for full control:

```json
"--enable-job-insights": "false"
```

### Job details reference (Glue 4.0, G.2X, 2 workers)

```json
{
  "GlueVersion": "4.0",
  "WorkerType": "G.2X",
  "NumberOfWorkers": 2,
  "DefaultArguments": {
    "--enable-spark-ui": "true",
    "--spark-event-logs-path": "s3://aws-glue-assets-264373394510-ap-southeast-1/sparkHistoryLogs/",
    "--enable-metrics": "true",
    "--enable-job-insights": "false"
  }
}
```

---

## EMR Serverless — S3-Only Logging

### Minimal config (S3 + disable managed persistence)

```json
{
  "monitoringConfiguration": {
    "s3MonitoringConfiguration": {
      "logUri": "s3://your-bucket/emr/logs/"
    },
    "managedPersistenceMonitoringConfiguration": {
      "enabled": false
    }
  }
}
```

### Explicit config (also disables CloudWatch if previously enabled)

```json
{
  "monitoringConfiguration": {
    "s3MonitoringConfiguration": {
      "logUri": "s3://your-bucket/emr/logs/"
    },
    "cloudWatchLoggingConfiguration": {
      "enabled": false
    },
    "managedPersistenceMonitoringConfiguration": {
      "enabled": false
    }
  }
}
```

### What each block does

| Block | Purpose |
|---|---|
| `s3MonitoringConfiguration.logUri` | Routes all job logs to S3 |
| `cloudWatchLoggingConfiguration.enabled: false` | Explicitly disables CloudWatch log streaming |
| `managedPersistenceMonitoringConfiguration.enabled: false` | Disables EMR's own managed log persistence (separate from CloudWatch) |

### Setting at application level vs job level

You can set `monitoringConfiguration` at **application creation** (applies to all jobs) or override it per **job run**:

```bash
# Application level
aws emr-serverless create-application \
  --release-label emr-6.x.x \
  --type SPARK \
  --monitoring-configuration '{
    "s3MonitoringConfiguration": {
      "logUri": "s3://your-bucket/emr/logs/"
    },
    "cloudWatchLoggingConfiguration": {
      "enabled": false
    },
    "managedPersistenceMonitoringConfiguration": {
      "enabled": false
    }
  }'

# Job run level override
aws emr-serverless start-job-run \
  --application-id <APP_ID> \
  --execution-role-arn <ROLE_ARN> \
  --configuration-overrides '{
    "monitoringConfiguration": {
      "s3MonitoringConfiguration": {
        "logUri": "s3://your-bucket/emr/logs/"
      },
      "cloudWatchLoggingConfiguration": {
        "enabled": false
      }
    }
  }' \
  --job-driver '{ ... }'
```

Job-level config takes priority over application-level config.

---

## EMR on EC2 — S3-Only Logging

Remove the `cloudWatchMonitoringConfiguration` block entirely from `monitoringConfiguration`:

```json
{
  "monitoringConfiguration": {
    "s3MonitoringConfiguration": {
      "logUri": "s3://your-bucket/emr/logs/"
    }
  }
}
```

For EMR on EKS, same pattern applies — include only `s3MonitoringConfiguration` and omit `cloudWatchMonitoringConfiguration`.

---

## Key Principle

CloudWatch logging is **opt-in** for both Glue and EMR. Removing or disabling the relevant flags/config blocks routes everything to S3. Spark event logs in S3 provide full observability via Spark History Server without CloudWatch costs.
