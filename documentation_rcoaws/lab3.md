# Lab 3: Log collection and analysis 

## Task 1. Connet to the bastion host 
Connect EC2 Bastion host instance with Session Manager

## Task 2. Connect AWS Kinesis Data Firehose delivery stream and configure fluent bit daemon set

In the bastion host session create env variables with values given:

`export FIREHOSE_ROLE_ARN=arn:aws:iam::268092685442:role/firehose-delivery-role S3_BUCKET_ARN=arn:aws:s3:::labstack-deeb5f2b-4b98-4e02-86ac-f-firehosebucket-w6jzpvmvf5n6`

create a Firehose delivery stream
`aws firehose create-delivery-stream --delivery-stream-name eks-stream --delivery-stream-type DirectPut --s3-destination-configuration RoleARN=${FIREHOSE_ROLE_ARN},BucketARN=${S3_BUCKET_ARN},Prefix=eks/`

Go to Kinesis in console and check eks-stream in the delivery streams section. Yeah!
In the bastion host session, write to create a **namespace for fluent bit daemonSet**:

`kubectl create namespace fb`

and create a **kubernetes service account** for the fluent bit daemonSet in the namespace created:

`kubectl create sa fluent-bit -n fb`

Create a **ClusterRol** and **ClusterRolBinding** for fluent bit. In the yaml file.

`kubectl apply -f ~/scripts/task2/eks-fluent-bit-daemonset-rbac.yaml`

Create a **ConfigMap** to define fluent bit log parsing an route params:

`kubectl apply -f ~/scripts/task2/eks-fluent-bit-configmap.yaml`

And create a kubernets fluent bit daemonSet:
`kubectl apply -f ~/scripts/task2/eks-fluent-bit-daemonset.yaml`

and show with:

`kubectl get daemonset fluentbit -n fb`

and check it is running with the logs:
`kubectl logs ds/fluentbit -n fb`

## Taks 3. Deploy a sample application, collect log data and analyze with Athena

In the bastion host session for the nginx configuration pre.created.

`kubectl apply -f ~/scripts/task3/eks-nginx-app.yaml`

