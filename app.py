import pyodbc
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import os

# Fetch the connection string from the environment variable
connection_string = os.environ.get('CONNECTION_STRING')

# Check if the connection string is available
if connection_string:
    print(f"Connection String: {connection_string}")
else:
    print("Connection string not found in environment variables.")
    
app = FastAPI()

# Configure CORSMiddleware to allow all origins (disable CORS for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows all origins (use '*' for development only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define the Task model
class Task(BaseModel):
    title: str
    description: str

# Create a table for tasks (You can run this once outside of the app)
@app.get("/")
def get_tasks():
    return [
        {"id": 1, "title": "Task 1", "description": "Test task"},
        {"id": 2, "title": "Task 2", "description": "Demo task"}
    ]

# List all tasks
@app.get("/tasks")
def get_tasks():
    return [
        {"id": 1, "title": "Task 1", "description": "Test task"},
        {"id": 2, "title": "Task 2", "description": "Demo task"}
    ]

# Retrieve a single task by ID
@app.get("/tasks/{task_id}")
def get_tasks():
    return [
        {"id": 1, "title": "Task 1", "description": "Test task"},
        {"id": 2, "title": "Task 2", "description": "Demo task"}
    ]

if __name__ == "__main__":
    create_tasks_table()
