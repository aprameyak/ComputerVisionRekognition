# ComputerVisionRekognition

![AWS SDK](https://img.shields.io/badge/AWS%20SDK-FF9900?logo=amazon-aws&logoColor=white&style=for-the-badge)
![AWS Rekognition](https://img.shields.io/badge/AWS%20Rekognition-00A1E4?logo=amazon-aws&logoColor=white&style=for-the-badge)
![AWS S3](https://img.shields.io/badge/AWS%20S3-569A31?logo=amazon-aws&logoColor=white&style=for-the-badge)

## About

This project is a script that can be run locally to analyze an image file stored within an AWS S3 bucket. It uses the AWS SDK and AWS Rekognition to identify objects and label them with confidence levels.

## Features

- **AWS Rekognition**: Detects and identifies objects within images stored in an AWS S3 bucket  
- **Confidence Scores**: Labels each object with a confidence score representing recognition accuracy  
- **AWS SDK**: Uses the AWS SDK for JavaScript to interact with AWS services  
- **IAM Permissions**: Requires IAM permissions configured through `aws configure` for secure access  
- **Local Execution**: Script can be executed locally after AWS CLI is set up

## Tech Stack

- **Backend**: Node.js, AWS SDK, AWS Rekognition  
- **Cloud Services**: AWS S3, AWS Rekognition, AWS IAM
