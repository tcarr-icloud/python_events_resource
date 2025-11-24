import os

import boto3
from boto3.dynamodb.conditions import Key

ENDPOINT_URL = os.getenv('ENDPOINT_URL', 'http://localhost:8000'),
REGION_NAME = os.getenv('REGION_NAME', 'us-west-2'),
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', 'DUMMYIDEXAMPLE'),
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'DUMMYEXAMPLEKEY')


def get_dynamodb_client():
    dynamodb = boto3.client(
        'dynamodb',
        endpoint_url=ENDPOINT_URL[0],
        region_name=REGION_NAME[0],
        aws_access_key_id=AWS_ACCESS_KEY_ID[0],
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY[0]
    )
    return dynamodb


def get_dynamodb_resource():
    dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url=ENDPOINT_URL[0],
        region_name=REGION_NAME[0],
        aws_access_key_id=AWS_ACCESS_KEY_ID[0],
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY[0]
    )
    return dynamodb


def put_event(table_name, event):
    dynamodb = get_dynamodb_client()
    dynamodb.put_item(
        TableName=table_name,
        Item={
            'AggregateId': {'S': event.get('AggregateId')},
            'Timestamp': {'S': event.get('Timestamp')},
            'Type': {'S': event.get('Type')},
            "Data": {'S': event.get('Data')}
        }
    )
    return


def get_event_by_pk_and_sk(table_name, aggregate_id, timestamp):
    dynamodb = get_dynamodb_client()
    response = dynamodb.get_item(TableName=table_name,
                                 Key={'AggregateId': {'S': aggregate_id}, 'Timestamp': {'S': timestamp}})
    if 'Item' in response:
        return response['Item']
    else:
        return None


def get_event_by_pk(table_name, aggregate_id):
    dynamodb = get_dynamodb_resource()
    table = dynamodb.Table(table_name)
    response = table.query(
        KeyConditionExpression=Key('AggregateId').eq(aggregate_id),
    )
    if 'Items' in response:
        return response['Items']
    else:
        return None
