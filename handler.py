import requests
import boto3
import json
import os

def check_endpoint(event, context):
    try:
        requests.head(event['endpoint_url'], timeout=10)
    except requests.ConnectionError:
        message = {"not_reachable": event['endpoint_url']}
        client = boto3.client('sns')
        response = client.publish(
                TargetArn=event['sns_arn'],
                Message=json.dumps({'default': json.dumps(message)}),
                MessageStructure='json'
                )
        print("failed to connect")
