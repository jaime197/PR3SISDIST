import sys
import logging
import pymysql
import json

host = "54.173.189.228"

def lambda_handler(event , context):
    username = event['username']
    password = event['password']
    response = {}  # Initialize the response dictionary

    try:
        conn = None
        conn = pymysql.connect(host, user="admin", passwd="password", db="distribuidos", connect_timeout=10, port=3306)
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM credenciales WHERE username = %s AND password = %s", (username, password))
            
            if cur.rowcount == 1:
                response['message'] = 'Login successful'
            else:
                response['message'] = 'Invalid credentials'
            
            cur.close()
        
    except pymysql.MySQLError as e:
        print(e)
        response['message'] = 'An error occurred'
        
    finally:
        if conn:
            conn.close()

    
    return {
        'statusCode': 200,
        'headers': { 'Access-Control-Allow-Origin': '*' },
        'body': json.dumps(response)
    }
#      

