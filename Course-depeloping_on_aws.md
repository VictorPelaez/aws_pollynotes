# aws_pollynotes
Application notes in AWS with lambda, polly 

# Developing on AWS. Virtual class
## Course objectives

In this course, you will learn to:

1. Build a simple end-to-end cloud application using AWS Software Development Kits (AWS SDKs),Command Line Interface (AWS CLI), and IDEs.
2. Configure AWS Identity and Access Management (IAM) permissions to support a development environment.

3. Use multiple programming patterns in your applications to access AWS services.

4. Use AWS SDKs to perform CRUD (create, read, update, delete) operations on Amazon Simple Storage Service (Amazon S3) and Amazon DynamoDB resources.

5. Build AWS Lambda functions with other service integrations for your web applications.

6. Understand the benefits of microservices architectures and serverless applications to design.

7. Develop API Gateway components and integrate with other AWS services.

8. Explain how Amazon Cognito controls user access to AWS resources.

9. Build a web application using Cognito to provide and control user access.

10. Use DevOps methodology to reduce the risks associated with traditional application releases and identify AWS services that help in implementing DevOps practices.

11. Use AWS Serverless Application Model (AWS SAM) to deploy an application.

12. Observe your application build using Amazon X-Ray.

## Labs

**Lab 1 - Configure the Development Environment**
In this lab the student verifies the specific IDE is installed and configured to access AWS Services. They also use IAM to understand how permissions work.

- [Lab 1 solution](documentation_doaws/lab1.md)

**Lab 2 - Develop Solutions Using Amazon S3**
In this lab, students will develop a portion of the application using Amazon S3 to store files and configure a static website.

- [Lab 2 solution](documentation_doaws/lab2.md)

**Lab 3 - Develop Solutions Using Amazon DynamoDB**
In this lab, students will develop programs to create an Amazon DynamoDB table to store notes for the lab application and perform CRUD operation on the table.

- [Lab 3 solution](documentation_doaws/lab3.md)

**Lab 4 - Develop Solutions Using AWS Lambda**
In this lab, students will create the backend logic for the application by deploying their code with AWS Lambda functions.

- [Lab 4 solution](documentation_doaws/lab4.md)


**Lab 5 - Develop Solutions Using Amazon API Gateway**
In this lab, you will create an Amazon API Gateway resource for your application.

- [Lab 5 solution](documentation_doaws/lab5.md)

**Lab 6 - Capstone - Complete the Application Build**
In this lab, you will learn how to set up Amazon Cognito to authenticate and authorize users to use your API.

- [Lab 6 solution](documentation_doaws/lab6.md)

**Lab 7 - Observe the Application Using AWS X-Ray**
The application that you have built in previous labs has been re-deployed with AWS SAM. You will instrument the application code with AWS X-Ray to observe the operational state of the application.

- [Lab 7 solution](documentation_doaws/lab7.md)