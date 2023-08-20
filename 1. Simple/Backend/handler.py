import json
import boto3
import uuid

def lambda_handler(event, context):
    print(json.loads(event['body']))
    print(context)
    json_body = json.loads(event['body'])
    dynamodb = boto3.client('dynamodb')
    dynamodb.put_item(TableName='a_simple_person', Item={'id':{'S': str(uuid.uuid1())},'name':{'S':json_body['name']}, 'age': {'S': json_body['age']}})
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT'
        },
        'body': json.dumps('Hello from Lambda!')
    }
