"""
Simple Flask application to demonstrate a basic Hello World service and display a pandas DataFrame in the browser.

Steps:
1. Import required modules and initialize the Flask app.
2. Create a simple pandas DataFrame.
3. Define routes to return a greeting and the DataFrame as an HTML table.
4. Run the application in debug mode.
"""

# Step 1: Import required modules and initialize the Flask app
from flask import Flask
from markupsafe import Markup  # Import Markup for safe HTML rendering
import os
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Step 2: Create a simple pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['London', 'Paris', 'New York']
}
df = pd.DataFrame(data)

# Step 3: Define routes
@app.route('/', methods=['GET'])
def home():
    """
    Home endpoint returning a greeting and the DataFrame as an HTML table.
    """
    # Convert DataFrame to HTML
    table_html = df.to_html(classes='dataframe table table-striped', index=False)

    # Combine greeting and table into one HTML response
    html = f"""
    <html>
      <head>
        <title>Flask DataFrame Display</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.5.2/css/bootstrap.min.css">
      </head>
      <body class="p-4">
        <h1>Hello World</h1>
        {table_html}
      </body>
    </html>
    """
    return Markup(html)

# Optional separate route if you still want /data only for the table
def display_data():
    """
    Endpoint to display the DataFrame as an HTML table (without greeting).
    """
    table_html = df.to_html(classes='dataframe table table-striped', index=False)
    return Markup(table_html)

# Step 4: Run the application
if __name__ == '__main__':
    app.run(debug=True)
