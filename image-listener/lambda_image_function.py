from PIL import Image
import boto3
import io
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Handle Invalid Images
    if not object_key.lower().endswith(('.png', '.jpg', '.jpeg')):
        print("Invalid image.")
        return

    # Download image from S3
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    image_data = response['Body'].read()

    # Open image
    image = Image.open(io.BytesIO(image_data))

    # Resize image 
    resized_image = image.resize((500, 500))
    buffer = io.BytesIO()
    resized_image.save(buffer, format=image.format)
    
    # Upload to resized-images-shannak bucket
    output_bucket = 'resized-images-shannak'
    s3.put_object(
        Bucket=output_bucket,
        Key=f"resized-{object_key}",
        Body=buffer.getvalue()
    )

    print(f"Image {object_key} resized and saved to {output_bucket}")
