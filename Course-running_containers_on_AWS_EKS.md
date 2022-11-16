# Running Containers on Amazon Elastic Kubernetes Service (Amazon EKS)

Course objectives
In this course, you will learn to:

- Describe Kubernetes and Amazon EKS fundamentals and the impact of containers on workflows.
- Build an Amazon EKS cluster by selecting the correct compute resources to support worker nodes.
- Secure your environment with AWS Identity and Access Management (IAM) authentication and Kubernetes Role Based Access Control (RBAC) authorization.
- Deploy an application on the cluster. Publish container images to Amazon ECR and secure access via IAM policy.
- Deploy applications using automated tools and pipelines. Create a GitOps pipeline using WeaveFlux.
- Collect monitoring data through metrics, logs, and tracing with AWS X-Ray and identify metrics for performance tuning. Review scenarios where bottlenecks require the best scaling approach using horizontal or vertical scaling.
- Assess the tradeoffs between efficiency, resiliency, and cost and the impact of tuning for one over the others. Describe and outline a holistic, iterative approach to optimizing your environment. Design for cost, efficiency, and resiliency.
- Configure AWS networking services to support the cluster. Describe how Amazon Virtual Private Cloud (VPC) supports Amazon EKS clusters and simplifies inter-node communications. Describe the function of the VPC Container Network Interface (CNI). Review the benefits of a service mesh.
- Upgrade your Kubernetes, Amazon EKS, and third party tools.

## Lab 1: Building an Amazon EKS Environment
In this lab, you install the command line interface (CLI) tools that are required to deploy and interact with Amazon EKS and Kubernetes. You then deploy an Amazon EKS cluster, node group, and a sample microservices application that runs in containers on the Amazon EKS cluster.

- [Lab 1 solution](documentation_rcoaws/lab1.md)

## Lab 2: Continuous deployment with GitOps
In this lab, you will create a delivery pipeline using AWS CodePipeline. You will also manage Kubernetes manifest files stored in a second repository. Finally, you will use a GitOps approach to allow system convergence when updating or installing new applications.

- [Lab 2 solution](documentation_rcoaws/lab2.md)

## Lab 3: Log collection and analysis 
In this lab, you learn how to create a central logging solution for an application running on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster. You deploy Fluent Bit as a sidecar application into the Amazon EKS cluster worker nodes. Fluent Bit gathers application data from all sources and routes this data to its destination in an Amazon S3 bucket. The data is streamed by the Fluent Bit sidecar into Kinesis Data Firehose which delivers the log data to an Amazon S3 bucket. You then create a table from a schema in Amazon Athena. After the table is created, you use standard SQL query code to query the log data in the Amazon S3 bucket.

## Lab 4: Exploring EKS Communications

## Lab 5: Securing AWS EKS