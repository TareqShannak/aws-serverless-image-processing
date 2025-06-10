# 🖼️ AWS Serverless Image Processing

A serverless solution that automatically resizes images uploaded to Amazon S3 using AWS Lambda and Pillow.

---

## 🌐 Overview

This project showcases how to build an automated image processing pipeline using AWS services. When an image is uploaded to the `original-images-shannak` S3 bucket, a Lambda function is triggered to resize the image to **500x500 pixels**. The resized image is then saved to the `resized-images-shannak` bucket.

---

## 🏗️ Architecture

![Image Architecture](<AWS Image Processing Architecture.png>)

---

## 🧰 AWS Services Utilized

- **Amazon S3** – Stores original and resized images.
- **AWS Lambda** – Processes image resizing using the Pillow library.
- **IAM** – Manages permissions for secure access between Lambda and S3.
- **AWS SAM (Serverless Application Model)** – Manages infrastructure as code and automates deployment.

---

## 🛠️ Technologies Used

- **Python 3.9**
- **Pillow** – Python Imaging Library
- **AWS SAM CLI** – For building and deploying serverless applications

---

## 📁 Project Structure
```
aws-serverless-image-processing/
│
├── template.yaml                # AWS SAM template for defining resources
└── image-listener/
    ├── lambda_image_function.py # Main Lambda handler for resizing images
    └── requirements.txt         # Python dependencies
```
---

## 🚀 Deployment Guide

### ✅ Prerequisites

Make sure you have the following installed:

- An active **AWS account**
- [AWS CLI](https://aws.amazon.com/cli/)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

### 🧪 Build & Deploy

```bash
# Build the serverless application
sam build

# Deploy the application (interactive mode)
sam deploy --guided
```
## 👤 Author

**Tareq Shannak**  
🔗 [LinkedIn](https://www.linkedin.com/in/tareq-shannak-54221324b/)  
📧 Email: [tshannk@gmail.com](mailto:tshannk@gmail.com)
