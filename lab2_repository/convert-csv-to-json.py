import boto3, botocore, json, csv, io, configparser

def main(s3Client):
    print('\nStart of convert object script\n')

    ## Initialize variables for object creation
    print('Reading configuration file for bucket name...')
    config = readConfig()
    bucket_name = config['bucket_name']
    source_file_name = config['object_name'] + config['source_file_extension']
    key_name = config['key_name']+ config['source_file_extension']
    processed_file_name = config['key_name'] + config['processed_file_extension']
    contentType = config['processed_content_type']
    metaData_key = config['metaData_key']
    metaData_value = config['metaData_value']

    #### Get the object from S3
    print('\nGetting the CSV object from S3 bucket')
    csvStr = getCSVFile(s3Client, bucket_name, key_name)
    
    ## Convert the object to the new format
    print('\nConverting CSV string to JSON...')
    jsonStr = convertToJSON(csvStr)
    
    ## Uploaded the converted object to S3
    print('Creating the new JSON object on S3')
    print(createObject(s3Client, bucket_name, processed_file_name, jsonStr, contentType, {metaData_key: metaData_value}))

    print('\nEnd of convert object script\n')

def getCSVFile(s3Client, bucket, key):
    bytes_buffer = io.BytesIO()
    
    ## Start TODO 6: Download the file contents to the 
    ## bytes_buffer object so that it can be decoded to a string.
    
    

    ## End TODO 6

    byte_value = bytes_buffer.getvalue()
    return byte_value.decode('utf-8')

def createObject(s3Client, bucket, key, data, contentType, metadata={}):
    ## Start TODO 7: Create an S3 object with the converted data
    
    

    ## End TODO 7
    
    return 'Successfully Created Object\n'

def convertToJSON(input):
    jsonList = []
    keys = []
    
    csvReader = csv.reader(input.split('\n'), delimiter=",")

    for i, row in enumerate(csvReader):
        if i == 0:
            keys = row
        else:
            obj = {}
            for x, val in enumerate(keys):
                obj[val] = row[x]
            jsonList.append(obj)
    return json.dumps(jsonList, indent=4)

def readConfig():
    config = configparser.ConfigParser()
    config.read('./labRepo/config.ini')
    
    return config['S3']

# Create an S3 client to interact with the service and pass 
# it to the main function that will create the buckets
client = boto3.client('s3')
try:
    main(client)
except botocore.exceptions.ClientError as err:
    print(err.response['Error']['Message'])
except botocore.exceptions.ParamValidationError as error:
    print(error)