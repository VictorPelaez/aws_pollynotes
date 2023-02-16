# Lab 5 - Troubleshoot Your Pipeline 3 HOURS
This lab tests your understanding of ML pipelines by allowing you to troubleshoot and fix a broken environment.
![image](f5-1.JPG)

## task resolve 1
"deployModelPipeline" in the codepipeline 
In the build stage under the  buildImage choose AWS Codebuild. Choose the build that one is fail
![image](f5-2.JPG)
Find several errors, exist status 125 and other with exit status 1. Both docker errors. Check in cloudwatch the errors.
![image](f5-3.JPG)

Problem resolution

In the left, codebuild choose build projects
Edit and select Environment in the service role choose 

Add varible environment ECR_URI and MOdel_image and Update them
![image](f5-4.JPG)
![image](f5-5.JPG)