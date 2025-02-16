from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

app = FastAPI()

# Load Jinja2 templates
templates = Jinja2Templates(directory="templates")

# MySQL Database Configuration
db_connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database="test_db",
    use_pure=True, 
    port=3306,
)

# Function to get database connection
def get_db_connection():
    try:
        if db_connection.is_connected():
            return db_connection
    except Error as e:
        print(f"Error: {e}")
        return None

# API Route to Fetch Data and Render in HTML Table
@app.get("/users/", response_class=HTMLResponse)
def get_users(request: Request):
    db_connection = get_db_connection()
    if not db_connection:
        return {"error": "Failed to connect to the database"}

    cursor = db_connection.cursor(dictionary=True)
    cursor.execute("SELECT id, name, email FROM users LIMIT 10")
    results = cursor.fetchall()
    cursor.close()
    db_connection.close()

    return templates.TemplateResponse("index.html", {"request": request, "users": results})
