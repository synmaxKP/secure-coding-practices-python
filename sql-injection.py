import mysql.connector

def get_user_data(username):
    # Construct the SQL query
    query = "SELECT * FROM users WHERE username = '" + username + "'"

    # Execute the query
    conn = mysql.connector.connect(user='your_username', password='your_password', host='localhost', database='your_database')
    cursor = conn.cursor()
    cursor.execute(query)

    # Fetch and return the user data
    user_data = cursor.fetchone()
    return user_data

# Proper Solution - Parameterized Queries:
import mysql.connector

def get_user_data(username):
    # Construct the SQL query with a placeholder
    query = "SELECT * FROM users WHERE username = %s"

    # Execute the query with the username as a parameter
    conn = mysql.connector.connect(user='your_username', password='your_password', host='localhost', database='your_database')
    cursor = conn.cursor()
    cursor.execute(query, (username,))

    # Fetch and return the user data
    user_data = cursor.fetchone()
    return user_data

# Usage:
username = input("Enter the username: ")
user_data = get_user_data(username)
print(user_data)