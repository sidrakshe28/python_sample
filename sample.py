import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
# Connect to the database
db_connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Create a cursor object
cursor = db_connection.cursor()

# Execute a query
cursor.execute("SELECT * FROM component")

# Fetch results
results = cursor.fetchall()
print("Connected successfully!")

# Close the cursor and connection
cursor.close()
db_connection.close()


