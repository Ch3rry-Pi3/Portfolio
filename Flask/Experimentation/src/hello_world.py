"""
hello_world.py

Simple Flask application to demonstrate a basic Hello World service.

Steps:
1. Initialise the Flask application.
2. Define the home route to return a greeting.
3. Run the application in debug mode.
"""

# Step 1: Import required modules and initialize the Flask app
from flask import Flask
import os

# Initialize the Flask application
app = Flask(__name__)

# Step 2: Define routes
@app.route('/', methods=['GET'])
def home():
    """
    Home endpoint returning a simple greeting.
    """
    return "Hello World"

# Step 3: Run the application
if __name__ == '__main__':
    app.run(debug=True)
