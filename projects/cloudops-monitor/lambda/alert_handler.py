import json
import boto3
import os
from datetime import datetime

# AWS clients
sns_client = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')

# Environment variables (set in Lambda config)
ALERT_TABLE = os.environ.get('ALERT_TABLE')
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')

# Connect to DynamoDB table
table = dynamodb.Table(ALERT_TABLE)

def lambda_handler(event, context):
    """
    Processes CloudWatch alarms, stores in DynamoDB, and sends SNS notification.
    """
    # Extract alarm information
    alarm_name = event['detail']['alarmName']
    state = event['detail']['state']['value']
    timestamp = datetime.utcnow().isoformat()

    # Log to DynamoDB
    table.put_item(
        Item={
            'AlarmName': alarm_name,
            'State': state,
            'Timestamp': timestamp
        }
    )

    # Send SNS notification
    message = f"CloudWatch Alert\nAlarm: {alarm_name}\nState: {state}\nTime: {timestamp}"
    sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject=f"CloudOps Alert: {alarm_name}"
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Alert processed successfully')
    }
