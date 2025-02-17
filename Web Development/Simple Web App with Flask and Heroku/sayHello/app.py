"""
Filename: app.py
Author: [Roger J. Campbell]
Date: [2025-02-17]
Description: A simple Flask web application that greets the user 
             based on input from a form.
"""

from flask import Flask, render_template, request, flash

# Initialize the Flask application
app = Flask(__name__)

# Secret key for flash messages (used for session management)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
    """
    Route: /hello
    Purpose: Displays the main page and prompts the user for their name.
    Returns:
        Renders the 'index.html' template with a flash message.
    """
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
    """
    Route: /greet
    Purpose: Processes the form input and greets the user.
    Methods: POST, GET
    Returns:
        Renders the 'index.html' template with a personalized greeting.
    """
    # Retrieve the user input from the form and display a greeting message
    flash("Hello, " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)         # Enable debug mode for easier troubleshooting
