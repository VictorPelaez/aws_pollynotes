# PollyNotes-CreateUpdateFunction
# This function allows us to create and update items in DynamoDB
#
# This lambda function is integrated with the following API method:
# /notes POST (create or update a note)

from __future__ import print_function
import boto3
import os
import json
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import logging
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

logger = logging.getLogger()
logger.setLevel(logging.INFO)
patch_all()

dynamodb = boto3.resource('dynamodb')


def add_annotation(UserId, NoteId):
    xray_recorder.begin_subsegment('Put a note')
    xray_recorder.put_annotation("UserId", UserId)
    xray_recorder.put_annotation("NoteId", NoteId)
    xray_recorder.end_subsegment()


def extractParams(event):
    UserId = event["requestContext"]["authorizer"]["claims"]["cognito:username"]
    note = json.loads(event['body'])
    dbName = os.environ['TABLE_NAME']
    return {
        'UserId': UserId,
        'note': note,
        'dbName': dbName
    }


def putNote(params):
    table = dynamodb.Table(params['dbName'])
    table.put_item(
        Item={
            'UserId': params['UserId'],
            'NoteId': int(params['note']["NoteId"]),
            'Note': params['note']["Note"]
        }
    )


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
        add_annotation(params['UserId'], params['note']["NoteId"])

        # DynamoDB 'put_item' to add or update a note
        putNote(params)

    except Exception as e:
        print(e)
        response['body'] = e
        return response

    response['statusCode'] = 200
    response['body'] = str(params['note']["NoteId"])
    return response
