import json
import boto3
import os

def handler(event, context):
    secret_name = os.environ['SECRET_NAME']
    region_name = os.environ['AWS_REGION']
    
    # Create a Secrets Manager client
    client = boto3.client('secretsmanager', region_name=region_name)
    
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except Exception as e:
        print(f"Error retrieving secret: {str(e)}")
        raise e

    if 'SecretString' in get_secret_value_response:
        secret = get_secret_value_response['SecretString']
    else:
        secret = base64.b64decode(get_secret_value_response['SecretBinary'])
    
    return {
        'statusCode': 200,
        'body': json.dumps(secret)
    }