from fastapi import FastAPI
import mysql.connector
import  os
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

app = FastAPI()


# MySQL Database Configuration
db_connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database="test_db",
)



# Function to connect to MySQL
def get_db_connection():
    try:
        #connection = mysql.connector.connect(**DB_CONFIG)
        if db_connection.is_connected():
            return db_connection
    except Error as e:
        print(f"Error: {e}")
        return None
    
# Root Route to Prevent 404 Error
@app.get("/")
def home():
    return {"message": "FastAPI is running"}

# Handling Favicon Requests
@app.get("/favicon.ico")
def favicon():
    return {}

# API Route to Fetch Data
@app.get("/users/")
def get_users():
    db_connection = get_db_connection()
    if not db_connection:
        return {"error": "Failed to connect to the database"}

    cursor = db_connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM  users limit 10")  
    results = cursor.fetchall()
    cursor.close()
    db_connection.close()
    return results
