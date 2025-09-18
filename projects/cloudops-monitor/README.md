# CloudOps Monitor

**Project Type:** AWS Infrastructure Monitoring  
**Purpose:** Monitor AWS infrastructure resources and alert teams on operational events, providing proactive visibility into the environment.

## AWS Services Used
- **CloudWatch:** Metrics & Alarms
- **AWS Lambda:** Event-driven alert processing
- **Amazon SNS:** Notifications to teams
- **DynamoDB:** Historical alert storage
- **IAM Roles:** Secure access control

## Implementation Overview

1. **Monitoring Metrics:**
   - Track EC2, RDS, and Lambda performance metrics.
   - Define thresholds for CPU utilization, memory usage, and function errors.

2. **Automated Event Processing:**
   - Lambda function triggers on CloudWatch events.
   - Processes events and formats alerts.

3. **Notification Delivery:**
   - Alerts are sent via SNS to email or Slack.
   - Ensure delivery reliability and actionable information.

4. **Data Storage:**
   - Log alerts and timestamps in DynamoDB for historical analysis.

## Programmatic Elements
- **Python (boto3)** for Lambda automation
- **CloudFormation YAML** for provisioning monitoring infrastructure
- **Bash scripts** for deployment automation

## Professional Best Practices
- Infrastructure as Code (CloudFormation)
- Event-driven, serverless architecture
- IAM roles with least privilege
- Structured and documented code for maintainability

