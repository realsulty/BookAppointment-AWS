import json
import boto3
from botocore.exceptions import ClientError

# Initialize the DynamoDB and SNS clients
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ServiceBooking')
sns = boto3.client('sns')

# Define the SNS topic ARN (replace with your actual SNS topic ARN)
SNS_TOPIC_ARN = 'arn:aws:sns:us-west-2:637423256293:MyFinalProject'

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        if 'serviceName' not in body or 'date' not in body:
            raise KeyError('Missing date or service')
        
        service_name = body['serviceName']
        date = body['date']
        
        # Insert item into DynamoDB
        response = table.put_item(
            Item={
                'serviceName': service_name,
                'date': date
            }
        )
        
        # Prepare the message for SNS
        message = f"A new Appointment has been booked: {date} for service: {service_name}"
        
        # Publish the message to SNS
        sns_response = sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject="New Appointment Booking"
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Date booked successfully and notification sent!')
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {e.response["Error"]["Message"]}')
        }
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Missing or invalid {str(e)} in request body')
        }
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid JSON format')
        }