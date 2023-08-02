import psycopg2
import json

def lambda_handler(event, context):
    # Retrieve form data from the API Gateway event
    form_data = json.loads(event['body'])

    # Connect to the PostgreSQL database
    connection = psycopg2.connect(
        host="database-1.cmqfs7njtabk.us-east-1.rds.amazonaws.com",
        database="database-1",
        user="postgres",
        password="7787809387",
    )

    # Insert the data into the database
    with connection.cursor() as cursor:
        query = "INSERT INTO user_details (name, email, age) VALUES (%s, %s, %s);"
        cursor.execute(query, (form_data['name'], form_data['email'], form_data['age']))
        connection.commit()

    return {
        'statusCode': 200,
        'body': json.dumps('Data stored successfully in the database.')
    }
