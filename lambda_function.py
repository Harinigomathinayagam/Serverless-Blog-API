import json
import boto3
import uuid

# Connect DynamoDB
dynamodb = boto3.resource('dynamodb')

# Connect BlogPosts table
table = dynamodb.Table('BlogPosts')

# Main Lambda Function
def lambda_handler(event, context):

    # Get HTTP Method
    method = event['httpMethod']

    # ---------------- CREATE BLOG ----------------

    if method == 'POST':

        # Convert JSON body to Python dictionary
        body = json.loads(event['body'])

        # Generate unique ID
        post_id = str(uuid.uuid4())

        # Insert into DynamoDB
        table.put_item(
            Item={
                'postId': post_id,
                'title': body['title'],
                'content': body['content']
            }
        )

        # Return response
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': 'Post created successfully',
                'postId': post_id
            })
        }

    # ---------------- GET BLOGS ----------------

    elif method == 'GET':

        # Read all items from table
        response = table.scan()

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(response['Items'])
        }

    # ---------------- UPDATE BLOG ----------------

    elif method == 'PUT':

        body = json.loads(event['body'])

        # Get postId
        post_id = body['postId']

        # Update item
        table.update_item(
            Key={
                'postId': post_id
            },
            UpdateExpression='SET title=:t, content=:c',
            ExpressionAttributeValues={
                ':t': body['title'],
                ':c': body['content']
            }
        )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps('Post updated successfully')
        }

    # ---------------- DELETE BLOG ----------------

    elif method == 'DELETE':

        body = json.loads(event['body'])

        # Get postId
        post_id = body['postId']

        # Delete item
        table.delete_item(
            Key={
                'postId': post_id
            }
        )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps('Post deleted successfully')
        }

    # Invalid Request
    return {
        'statusCode': 400,
        'body': json.dumps('Invalid Request')
    }
