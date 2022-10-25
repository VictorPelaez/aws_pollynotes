from sqlite3 import register_converter
import boto3

# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html

session = boto3.Session(profile_name='my_dev_aws_user')
client = session.client("lambda", region_name="us-east-1")

r = client.list_functions()
list_lambdas = r['Functions']
for l in list_lambdas:
    print("\n", l["FunctionName"])