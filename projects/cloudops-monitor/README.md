# CloudOps Monitor

**Purpose:** Monitor AWS infrastructure resources and alert teams on operational events.

**Services Used:**
- AWS CloudWatch (Metrics & Alarms)
- AWS Lambda (Automated processing)
- Amazon SNS (Notifications)
- DynamoDB (Storing monitoring data)

**Implementation Steps:**
1. Create CloudWatch metrics and alarms for EC2, RDS, and Lambda.
2. Write Lambda functions triggered by CloudWatch events.
3. Lambda publishes alerts to SNS topics for notifications.
4. Store historical alerts in DynamoDB for analysis.

**Programmatic Elements:**
- AWS SDK for Python (boto3)
- Lambda deployment via AWS CLI or CloudFormation
- Automated alarm creation scripts
