# Serverless Blog API using AWS

A scalable and cost-effective Serverless Blog API built on AWS using AWS Lambda, API Gateway, DynamoDB, and S3. The application provides RESTful endpoints for managing blog posts with full CRUD functionality. API testing and validation are performed using Postman collections. The serverless architecture ensures high availability, automatic scaling, and reduced infrastructure management.

---

## 🚀 Features

- Create, Read, Update, and Delete (CRUD) blog posts
- Serverless backend powered by AWS Lambda
- RESTful API endpoints using Amazon API Gateway
- Data storage with Amazon DynamoDB
- Media/Image storage with Amazon S3
- API testing using Postman
- Secure access control with AWS IAM
- Automated deployment using AWS SAM / Serverless Framework
- Highly scalable and cost-efficient architecture

---

##  Architecture

```text
Client Application
       │
       ▼
Amazon API Gateway
       │
       ▼
AWS Lambda Functions
       │
 ┌─────┴─────┐
 ▼           ▼
DynamoDB     Amazon S3
(Blog Data)  (Images/Media)
```

---

##  Tech Stack

| Technology | Purpose |
|------------|---------|
| AWS Lambda | Serverless Compute |
| API Gateway | REST API Management |
| DynamoDB | NoSQL Database |
| Amazon S3 | Media Storage |
| AWS IAM | Access Management |
| Postman | API Testing |

---

##  API Endpoints

### Create Blog

```http
POST /blogs
```

Request Body:

```json
{
  "title": "My First Blog",
  "author": "Harini",
  "content": "This is a sample blog post."
}
```

### Get All Blogs

```http
GET /blogs
```

### Get Blog by ID

```http
GET /blogs/{id}
```

### Update Blog

```http
PUT /blogs/{id}
```

Request Body:

```json
{
  "title": "Updated Blog Title",
  "content": "Updated blog content."
}
```

### Delete Blog

```http
DELETE /blogs/{id}
```

---

##  Postman Testing

### Import Collection

1. Open Postman.
2. Click **Import**.
3. Select the provided Postman Collection JSON file.
4. Configure the API Gateway base URL.
5. Test all CRUD endpoints.

---

## 🔒 Security

- IAM-based access control
- Input validation for API requests
- Secure API Gateway configurations
- Least-privilege permissions for Lambda functions

---

##  Benefits of Serverless Architecture

- No server management
- Automatic scaling
- Pay-per-use pricing
- High availability
- Faster deployment cycles
- Reduced operational overhead

---


### Author

**Harini G**

Built with AWS Serverless Services and Postman API Testing.
