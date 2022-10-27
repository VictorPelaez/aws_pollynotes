# PollyNotes-ListFunction
#
# This lambda function is integrated with the following API methods:
# /notes GET (list operation)
#
# Its purpose is to get notes from our DynamoDB table

from __future__ import print_function
import boto3
import os
import json
import decimal
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
import logging
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

logger = logging.getLogger()
logger.setLevel(logging.INFO)
patch_all()

dynamodb = boto3.resource('dynamodb')

# Helper class to convert a DynamoDB item to JSON.


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        if isinstance(o, set):  # <---resolving sets as lists
            return list(o)
        return super(DecimalEncoder, self).default(o)


def add_annotation(UserId):
    xray_recorder.begin_subsegment('List all notes')
    xray_recorder.put_annotation("UserId", UserId)
    xray_recorder.end_subsegment()


def extractParams(event):
    UserId = event["requestContext"]["authorizer"]["claims"]["cognito:username"]
    dbName = os.environ['TABLE_NAME']

    return {
        'UserId': UserId,
        'dbName': dbName
    }


def getDynamoDBItems(params):
    table = dynamodb.Table(params['dbName'])

    # Get all results in the table that are owned by the authenticated user
    return table.query(KeyConditionExpression=Key("UserId").eq(params['UserId']))


def lambda_handler(event, context):

    # Log debug information
    print(event)

    # create the response object, the error code is 500 unless manually set to a success
    response = {
        'isBase64Encoded': False,
        'statusCode': 500,
        'body': '',
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

    try:
        # Extracting the user parameters from the event and environment
        params = extractParams(event)

        # Add X-Ray annotations to the trace
        add_annotation(params['UserId'])

        # Query the table for all items with the UserId
        records = getDynamoDBItems(params)

    except Exception as e:
        print(e)
        response['body'] = e
        return response

    response['statusCode'] = 200
    response['body'] = json.dumps(records["Items"], cls=DecimalEncoder)
    return response
