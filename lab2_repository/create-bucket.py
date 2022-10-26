import boto3, botocore, configparser

def main(s3Client):
    print('\nStart of create bucket script\n')

    print('Reading configuration file for bucket name...')
    config = readConfig()
    bucket_name = config['bucket_name']

    print('Verifying that the bucket name is valid...')
    #### Verify that the bucket exists. The script with exit 
    #### if the name is not valid for a new bucket.
    verifyBucketName(s3Client, bucket_name)
    print(bucket_name)

    #### Create the notes-bucket-
    createBucket(s3Client, bucket_name)

    ##Pause until the the bucket is in the account
    print('\nConfirm that the bucket exists...')
    verifyBucket(s3Client, bucket_name)

    print('\nEnd of create bucket script\n')

def verifyBucketName(s3Client, bucket):
    try:
        ## Start TODO 2: enter a command that will check if a bucket already exists in AWS
        ## with the name built from your ini file input.
        s3Client.head_bucket(Bucket=bucket)
        ## End TODO 2

        # If the previous command is successful, the bucket is already in your account.
        raise SystemExit('This bucket has already been created in your account, exiting because there is nothing further to do!')
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
          ## If you receive a 404 error code, a bucket with that name
          ##  does not exist anywhere in AWS.
          print('Existing Bucket Not Found, please proceed')
        if error_code == 403:
          ## If you receive a 403 error code, a bucket exists with that
          ## in another AWS account.
          raise SystemExit('This bucket has already owned by another AWS Account, change the suffix and try a new name!')

def createBucket(s3Client, name):
    session = boto3.session.Session()

    # Obtain the region from the boto3 session
    current_region = session.region_name
    print('\nCreating ' + name + ' in ' + current_region)

    # Start TODO 3: Create a new bucket in the users current region 
    # and return the response in a response variable.
    if current_region == 'us-east-1':
        response = s3Client.create_bucket(Bucket=name)
    else:
        response = s3Client.create_bucket(
            Bucket=name,
            CreateBucketConfiguration={'LocationConstraint': current_region})
    
    # End TODO 3:

    print('Success!')

def verifyBucket(s3Client, bucket):
    ## Start TODO 4: Complete the function so that it will 
    ## pause and only proceed after the bucket exists.
    waiter = s3Client.get_waiter('bucket_exists')
    waiter.wait(Bucket=bucket)

    ## End TODO 4
    print('The bucket:' + bucket + ' is now available.')

## Utility methods
def readConfig():
    config = configparser.ConfigParser()
    config.read('./labRepo/config.ini')
    
    return config['S3']

## TODO 1: Create an S3 client to interact with the service and pass 
## it to the main function that will create the buckets

s3Client = boto3.client('s3')

## End TODO 1

try:
    main(s3Client)
except botocore.exceptions.ClientError as err:
    print(err.response['Error']['Message'])
except botocore.exceptions.ParamValidationError as error:
    print(error)