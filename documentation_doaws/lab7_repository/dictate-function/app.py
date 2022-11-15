# PollyNotes-DictateFunction
#
# This lambda function uses Polly to convert a note to speech, uploads the mp3 file to S3, and returns a signed URL.
# This lambda function is integrated with the following API methods:
# /notes/{id}/POST

from __future__ import print_function
import boto3
import json
import os
from contextlib import closing
import logging
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

logger = logging.getLogger()
logger.setLevel(logging.INFO)
patch_all()

dynamodb = boto3.resource('dynamodb')
polly = boto3.client('polly')
s3 = boto3.client('s3')


def add_annotation(UserId, NoteId, VoiceId):
    xray_recorder.begin_subsegment('Dictate a note')
    xray_recorder.put_annotation("UserId", UserId)
    xray_recorder.put_annotation("VoiceId", VoiceId)
    xray_recorder.end_subsegment()


def extractParams(event):
    UserId = event["requestContext"]["authorizer"]["claims"]["cognito:username"]
    NoteId = event["pathParameters"]["id"]
    VoiceId = json.loads(event['body'])['VoiceId']

    return {
        'UserId': UserId,
        'NoteId': NoteId,
        'VoiceId': VoiceId,
        'mp3Bucket': os.environ['MP3_BUCKET_NAME'],
        'dbName': os.environ['TABLE_NAME']
    }


def getNoteText(params):
    # Create your DynamoDB resource using your Environment Variable for table name
    table = dynamodb.Table(params['dbName'])

    # Get the note from DynamoDB from the event parameters
    records = table.get_item(
        Key={
            'UserId': params['UserId'],
            'NoteId': int(params['NoteId'])
        }
    )
    return records['Item']['Note']


def convertToSpeech(text, params):
    # Invoke Polly API, which will transform text into audio
    pollyResponse = polly.synthesize_speech(
        OutputFormat='mp3',
        Text=text,
        VoiceId=params['VoiceId']
    )
    # Save the audio stream returned by Amazon Polly on Lambda's temp
    # directory '/tmp'
    if "AudioStream" in pollyResponse:
        with closing(pollyResponse["AudioStream"]) as stream:
            output = os.path.join("/tmp/", params['NoteId'])
            with open(output, "wb") as file:
                file.write(stream.read())


def uploadFileToS3(params):
    # Upload file
    s3.upload_file(
        '/tmp/' + params['NoteId'],
        params['mp3Bucket'],
        params['UserId']+'/'+params['NoteId']+'.mp3'
    )
    # Generate a pre-signed URL
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': params['mp3Bucket'],
            'Key': params['UserId'] + '/' + params['NoteId'] + '.mp3'
        }
    )
    return url


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
        add_annotation(params['UserId'], params['NoteId'], params['VoiceId'])

        # Get the note text from the DynamoDB table
        noteText = getNoteText(params)

        # Use polly to convert the text to speech and save the file in the /tmp folder
        convertToSpeech(noteText, params)

        # Upload the generated file to S3 and gererate a signed URL to access it
        url = uploadFileToS3(params)
    except Exception as e:
        print(e)
        response['body'] = e
        return response

    # If there are no errors, set a success status code and return the signed URL in the function response
    response['statusCode'] = 200
    response['body'] = json.dumps(url)
    return response
