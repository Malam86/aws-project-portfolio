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

# 📡 CloudOps Monitor

## Project Type
AWS Infrastructure Monitoring  

## Purpose
Monitor AWS infrastructure resources and alert teams on operational events, providing proactive visibility into the environment.

---

## 🛠️ AWS Services Used
- **CloudWatch**: Metrics & Alarms  
- **AWS Lambda**: Event-driven alert processing  
- **Amazon SNS**: Notifications to teams  
- **DynamoDB**: Historical alert storage  
- **IAM Roles**: Secure access control  

---

## 📊 Implementation Overview

### Monitoring Metrics
- Track **EC2, RDS, and Lambda** performance metrics.  
- Define thresholds for **CPU utilization, memory usage, and function errors**.  

### Automated Event Processing
- **Lambda function** triggers on CloudWatch events.  
- Processes events and formats alerts.  

### Notification Delivery
- Alerts are sent via **SNS** to email or Slack.  
- Ensures reliable delivery and actionable information.  

### Data Storage
- Log alerts and timestamps in **DynamoDB** for historical analysis.  

---

## 💻 Programmatic Elements
- **Python (boto3)** for Lambda automation  
- **CloudFormation YAML** for provisioning monitoring infrastructure  
- **Bash/PowerShell scripts** for deployment automation  

---

## ✅ Professional Best Practices
- Infrastructure as Code (**CloudFormation**)  
- Event-driven, **serverless architecture**  
- IAM roles with **least privilege**  
- Structured and documented code for **maintainability**  

---

# 🚀 Deployment & Operations Guide

## 📦 Deployment Steps

### 1. Package the Lambda function
From the `lambda/` folder:

`powershell
Compress-Archive -Path alert_handler.py -DestinationPath alert_handler.zip -Force

This creates alert_handler.zip.

2. Upload the package to S3
aws s3 cp alert_handler.zip s3://<your-s3-bucket-name>/alert_handler.zip --region us-east-2

3. Deploy the CloudFormation stack
aws cloudformation deploy `
  --template-file cloudops-monitor.yml `
  --stack-name CloudOpsMonitoringStack `
  --capabilities CAPABILITY_NAMED_IAM `
  --region us-east-2 `
  --parameter-overrides \
      Environment=prod \
      LambdaS3Bucket=<your-s3-bucket-name> \
      LambdaS3Key=alert_handler.zip \
  --tags Project=CloudOpsMonitoring Environment=prod

🌍 CloudFormation Parameters

Environment

Accepted values: test or prod.

Controls resource naming and notification behavior.

LambdaS3Bucket

The S3 bucket where your Lambda code (alert_handler.zip) is stored.

LambdaS3Key

The key (object path) in S3 for the Lambda code.

📡 Architecture Overview

CloudWatch Alarms trigger on defined metrics (e.g., EC2 CPU, Errors).

Alarms publish events to an SNS Topic.

The Lambda Function (alert_handler.py) receives SNS messages and:

Parses alert details.

Stores them in DynamoDB.

Forwards notifications as email via SNS subscription.

DynamoDB acts as a historical store of alerts for querying/troubleshooting.

Flow:
CloudWatch → SNS → Lambda → DynamoDB → Email

🏷️ Tagging Resources

Tags should be applied during deployment:

--tags Project=CloudOpsMonitoring Environment=prod


These tags will show up on Lambda, SNS, DynamoDB, and CloudWatch resources.

🧪 Test vs. Prod

Test Environment

Uses CloudOpsAlertTopic-test SNS topic.

Safe for validating flows without spamming production email lists.

Production Environment

Uses CloudOpsAlertTopic SNS topic.

Sends real alerts to operational email/SMS subscribers.

🧹 Cleanup

To avoid charges, delete test resources when done:

aws cloudformation delete-stack --stack-name CloudOpsMonitoringStack --region us-east-2


Also remove:

Old Lambda zips from S3.

Test SNS topics, DynamoDB tables, and Lambdas not in use.

🔐 IAM Security Review

Lambda execution role only has:

DynamoDB:PutItem (to write alerts).

SNS:Publish (to send notifications).

CloudWatch Logs (for function logs).

No broad * permissions are used.

Adjust policies as needed per least-privilege best practices.

✅ Verification

After deployment, test with:

aws sns publish `
  --topic-arn arn:aws:sns:us-east-2:<account-id>:CloudOpsAlertTopic `
  --message "Test alert from CLI" `
  --region us-east-2


You should receive an email, and the message should appear in DynamoDB.
