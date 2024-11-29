import boto3

rekognition_client = boto3.client('rekognition')
bucket_name = 'BUCKETNAME'
image_file = 'FILENAME'

response = rekognition_client.detect_labels(
    Image={
        'S3Object': {
            'Bucket': bucket_name,
            'Name': image_file
        }
    },
    MaxLabels=10,  
    MinConfidence=80  
)

print("Detected labels:")
for label in response['Labels']:
    print(f"{label['Name']} - Confidence: {label['Confidence']:.2f}%")
