# Guidance for Integrated scalable search for Amazon DocumentDB with Amazon OpenSearch


## Table of Content (required)


### Required

1. [Overview](#Overview)
    - [Cost](#cost)
2. [Prerequisites](#prerequisites-required)
    - [Operating System](#operating-system-required)
3. [Deployment Steps](#deployment-steps-required)
4. [Deployment Validation](#deployment-validation-required)
5. [Running the Guidance](#running-the-guidance-required)
6. [Next Steps](#next-steps-required)
7. [Cleanup](#cleanup-required)
8. [Authors](#authors-optional)

## Overview


Amazon DocumentDB provides native text search and vector search capabilities. With Amazon OpenSearch Service you can run advance search and analytics  such as fuzzy search, synonym search, cross-collection search, and multilingual search on Amazon DocumentDB data. 

This guidance demonstrates way to run advance search and analytics on Amazon DocumentDB data using Amazon OpenSearch Service.

![Reference Architecture](assets/referecearchitecture.jpg)

1. The application reads data from and writes to Amazon DocumentDB.
2. AWS Lambda Event Source Mapping (ESM) gets invoked in near real-time with the inserts and updates recorded Amazon DocumentDB change streams. Amazon DocumentDB change streams provide a time-ordered sequence of change events that occur within your collections.
3. AWS Lambda fetches credentials from AWS Secrets Manager to read from Amazon DocumentDB change streams. 
4. AWS Lambda streams the updates from Amazon DocumentDB change streams to the Amazon OpenSearch Service in near real-time.
5. Analytics or reporting tools fetch the data from the Amazon OpenSearch service for reporting. 


### Cost 

_You are responsible for the cost of the AWS services used while running this Guidance. As of June 2024, the cost for running this Guidance with the default settings in the <Default AWS Region (Most likely will be US East (N. Virginia)) > is approximately $<n.nn> per month for processing ( <nnnnn> records )._

_We recommend creating a [Budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this Guidance._

### Sample Cost Table 

**Note : Once you have created a sample cost table using AWS Pricing Calculator, copy the cost breakdown to below table and upload a PDF of the cost estimation on BuilderSpace.**

The following table provides a sample cost breakdown for deploying this Guidance with the default parameters in the US East (N. Virginia) Region for one month.

| AWS service  | Dimensions | Cost [USD] |
| ----------- | ------------ | ------------ |
| Amazon DocumentDB | xxx  | $ 3.50month |
| ....... | 1,000 active users per month without advanced security feature | $ 0.00 |

## Prerequisites 

1. Install and configure the latest version of the [AWS CLI (2.2.37 or newer)](https://aws.amazon.com/cli/) on the compute instance you are going to use to interact with. This can be your personal laptop, an Amazon EC2 instance, Cloud9, or similar. 
2.  To deploy this guidance, ensure that the user has permissions to create, list, and modify resources 
   - A VPC and the required networking components
   - Amazon DocumentDB
   - Amazon OpenSearch
   - AWS Lambda
   - An AWS Cloud9 environment 
   - AWS Secrets Manager  

### Operating System 

“These deployment instructions are optimized to best work on **<Amazon Linux 2 AMI>**.  Deployment in another OS may require additional steps.”

## Deployment Steps

### Using AWS CLI
1. Clone the repo using command ```gh repo clone aws-solutions-library-samples/guidance-for-integrated-scalable-search-for-amazon-documentdb-with-amazon-opensearch```
2. cd to the repo folder ```cd guidance-for-integrated-scalable-search-for-amazon-documentdb-with-amazon-opensearch/deployment```
3. Choose the parameters
4. Run this command to deploy the stack ```aws cloudformation create-stack --stack-name <stack-name> --template-body file://docdb_change_streams_amazon_os.yml --parameters <>=<key1>,ParameterValue=<value1> ParameterKey=<key2>,ParameterValue=<value2> --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM``` 
   

### Using AWS Console
1. Download the [docdb_change_streams_amazon_os.yml](#https://aws-blogs-artifacts-public.s3.amazonaws.com/artifacts/DBBLOG-3344/docdb_change_streams_amazon_os.yml)
2. Navigate to AWS CloudFormation service on your AWS Console
3. Choose ***Create stack*** and select **with new resources (standard)**
4. On **Specify template** choose ***Upload a template file***
5. For Stack name, enter the name for your CloudFormation stack.
6. For DocDBIdentifier, enter the name of your Amazon DocumentDB cluster.
7. For DocDBPassword, enter the administrator password for your Amazon DocumentDB cluster (minimum 8 characters).
8. For DocDBUsername, enter the name of your administrator user in the Amazon DocumentDB cluster.
9. For ExistingCloud9Role, choose True if you have the AWS Identity and Access Management (IAM) role AWSCloud9SSMAccessRole created in your account. If you have used AWS Cloud9 before, you should already have an existing role. You can verify by going to the IAM console and searching for it on the Roles page. Stack creation will fail if the roles exists and you choose False.
Choose Next.
10. Select the check box in the Capabilities section to allow the stack to create an IAM role, then choose Submit.


## Deployment Validation  (required)

<Provide steps to validate a successful deployment, such as terminal output, verifying that the resource is created, status of the CloudFormation template, etc.>


**Examples:**

* Open CloudFormation console and verify the status of the template with the name starting with xxxxxx.
* If deployment is successful, you should see an active database instance with the name starting with <xxxxx> in        the RDS console.
*  Run the following CLI command to validate the deployment: ```aws cloudformation describe xxxxxxxxxxxxx```



## Running the Guidance (required)

<Provide instructions to run the Guidance with the sample data or input provided, and interpret the output received.> 

This section should include:

* Guidance inputs
* Commands to run
* Expected output (provide screenshot if possible)
* Output description



## Next Steps (required)

Provide suggestions and recommendations about how customers can modify the parameters and the components of the Guidance to further enhance it according to their requirements.


## Cleanup (required)

- Include detailed instructions, commands, and console actions to delete the deployed Guidance.
- If the Guidance requires manual deletion of resources, such as the content of an S3 bucket, please specify.




## Notices 

Disclaimer: 
*Customers are responsible for making their own independent assessment of the information in this Guidance. This Guidance: (a) is for informational purposes only, (b) represents AWS current product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS products or services are provided “as is” without warranties, representations, or conditions of any kind, whether express or implied. AWS responsibilities and liabilities to its customers are controlled by AWS agreements, and this Guidance is not part of, nor does it modify, any agreement between AWS and its customers.*


## Authors 

Anshu Vajpayee
Kaarthiik Thota
