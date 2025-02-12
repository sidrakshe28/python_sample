import mysql.connector
from faker import Faker
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Faker
fake = Faker()

# Connect to MySQL
db_connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database="test_db"
)

cursor = db_connection.cursor()

# SQL Query to Insert Data
insert_query = """
INSERT INTO users (name, email, phone, address) 
VALUES (%s, %s, %s, %s)
"""
phone_number = fake.phone_number()
if len(phone_number) > 10:  
    phone_number = phone_number[:10]


# Generate and Insert 100 Fake Users
fake_users = [
    (fake.name(), fake.email(), fake.phone_number(), fake.address())
    for i in range(100)
]

cursor.executemany(insert_query, fake_users)
db_connection.commit()

print(f"Inserted {cursor.rowcount} fake records successfully!")

# Close the cursor and connection
cursor.close()
db_connection.close()