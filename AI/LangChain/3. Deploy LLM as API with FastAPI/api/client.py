"""Streamlit Client for LangChain FastAPI Server

This script creates a Streamlit-based web app that interacts with the FastAPI server to generate essays and poems 
using OpenAI's GPT models and the LLAMA2 model.

Parameters:
-----------
requests : module
    Used to make HTTP POST requests to the FastAPI server.
streamlit : module
    Framework for creating the web app interface.

get_openai_response : function
    Sends a topic to the FastAPI essay endpoint and returns the generated essay.

get_ollama_response : function
    Sends a topic to the FastAPI poem endpoint and returns the generated poem.

Returns:
--------
Streamlit Application:
    - Provides input fields for topics to generate essays and poems.
    - Displays the generated content interactively.

Launch Instructions:
--------------------
1. Ensure the FastAPI server is running (via `python app.py`).
2. Run the Streamlit app:
    ```
    streamlit run client.py
    ```

3. Access the app in your browser at:
    - `http://localhost:8501`
"""

# Import requests library for making HTTP requests to the FastAPI server
import requests

# Import Streamlit library for building the web application interface
import streamlit as st

# Function to interact with the essay endpoint
def get_openai_response(input_text):
    """
    Sends a POST request to the FastAPI essay endpoint and retrieves the generated essay.
    
    Parameters:
    ----------
    input_text : str
        The topic for the essay.

    Returns:
    -------
    str
        The essay content generated by OpenAI.
    """
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={"input": {"topic": input_text}}
    )
    return response.json()["output"]["content"]

# Function to interact with the poem endpoint
def get_ollama_response(input_text):
    """
    Sends a POST request to the FastAPI poem endpoint and retrieves the generated poem.
    
    Parameters:
    ----------
    input_text : str
        The topic for the poem.

    Returns:
    -------
    str
        The poem content generated by LLAMA2.
    """
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={"input": {"topic": input_text}}
    )
    return response.json()["output"]

# Create Streamlit interface
st.title("LangChain Demo with Llama2 API")

# Input fields for essay and poem topics
input_text = st.text_input("Write an essay on:")  # OpenAI GPT models
input_text1 = st.text_input("Write a poem on:")   # LLAMA2 model

# Display the generated essay
if input_text:
    st.write("Essay:")
    st.write(get_openai_response(input_text))

# Display the generated poem
if input_text1:
    st.write("Poem:")
    st.write(get_ollama_response(input_text1))