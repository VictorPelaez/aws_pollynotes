aws configure
aws sts get-caller-identity

## Run AWS CLI to list buckets
aws s3 ls

## Run AWS CLI to delete a bucket.
bucketToDelete=$(aws s3api list-buckets --output text --query 'Buckets[?contains(Name, `deletemebucket`) == `true`] | [0].Name')
aws s3 rb s3://$bucketToDelete

## same with debug option
aws s3 rb s3://$bucketToDelete --debug

## Review the iam policy
policyArn=$(aws iam list-policies --output text --query 'Policies[?PolicyName == `S3-Delete-Bucket-Policy`].Arn')
aws iam get-policy-version --policy-arn $policyArn --version-id v1

## Attach the iam policy to the rol "notes-application-role"
aws iam attach-role-policy --policy-arn $policyArn --role-name notes-application-role

## Task 4 verify again with the role and policy