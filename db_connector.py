import mysql.connector, os

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="inventory_db"
    )
    cursor = connection.cursor()

except mysql.connector.Error as error:
    print(f"Database connection failed: {error}")