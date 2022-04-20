# VanityNumber Application for VoiceFoundry Assignment

This repository is created for VoiceFoundry Assignment for generation of Vanity number, There are multiple ways a Vanity number could be generated, this is a simple app which will accept input from caller and convert the last 7 digits of number into a word by looking up in a dictionary database which is created as part of this application. 

Pre-requisites
  •	AWS Account
  •	S3 bucket
  •	Amazon connect Instance Id & phone number.

Technologies used
  •	Python 
  •	CloudFormation
  •	DynamoDB
  •	AmazonConnect
  •	Lambda
  
# Deploying Vanity Number Application
Clone this project in your local machine and create similar structure on s3 bucket as created in repository.

This application can be deployed in AWS using CloudFormation templates present under CloudFormation folder. Folder contains two YAML files which are templates for stack creation. 

 **DynamoDBLoad.yaml**
    This yaml file will create and load data into a DynamoDB dictionary table(vf-dictionary). It will load data from input file present under InputFiles folder. Lambda which is deployed as part of this yaml, is event based and gets triggered when file is uploaded into s3bucket. End result of this stack is loading data into dictionary table which will be used in subsequent processing.
 
 **custom-resource.yaml**
This yaml file will create two Lambda functions one for vanity number generation and another for creation of Amazon Connect contcat flow using Custom Resource. Code supporting for this yaml file is present under LambdaCode folder which will be deployed in form of Lambda Functions.

Once both the stacks are created and all the resources are provisioned, a phone number should be attached manually to vf-Vanity-MainFlow <Check exact name in connect> for this application to work.
