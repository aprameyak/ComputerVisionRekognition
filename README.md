# **ComputerVisionRekognition**

This project is a script that can be run locally to analyze an image file stored within an AWS S3 bucket. The project uses the AWS SDK and AWS Rekognition to identify objects and label them with confidence levels.

![AWS Badge](https://img.shields.io/badge/AWS-SDK-FF9900)
![Rekognition Badge](https://img.shields.io/badge/AWS-Rekognition-00A1E4)
![S3 Badge](https://img.shields.io/badge/AWS-S3-569A31)

## Features

- **AWS Rekognition**: Uses AWS Rekognition to detect and identify objects within images stored in an AWS S3 bucket.
- **Confidence Scores**: Each detected object is labeled with a confidence score to indicate the accuracy of the recognition.
- **AWS SDK**: The project uses the AWS SDK for JavaScript to interact with AWS services.
- **IAM Permissions**: Utilizes AWS IAM permissions configured through the `aws configure` command for secure access to AWS Rekognition and S3.
- **Local Execution**: The script can be executed locally after configuring AWS CLI with the necessary IAM permissions.

## Tech Stack

- **Backend**: Node.js, AWS SDK, AWS Rekognition
- **Cloud Services**: AWS S3, AWS Rekognition, AWS IAM
