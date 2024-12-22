"""Basic Streamlit Application to Demonstrate OpenAI API Integration with LangChain

This application allows users to enter a query into a text box and displays the response generated 
by OpenAI's GPT model. Unlike more advanced examples, this app does not use prompt engineering, 
memory, or chains, providing a simpler demonstration of LangChain's capabilities.

Parameters:
----------
openai_key : str
    OpenAI API key loaded from the `constants.py` file and set as an environment variable.

os : module
    Used to set the OpenAI API key as an environment variable.

st : module
    Streamlit library for creating the interactive web app interface.

OpenAI : class
    LangChain's LLM wrapper for OpenAI's GPT models.

Returns:
-------
Streamlit Application:
    The app allows users to:
    - Enter a query via a text input field.
    - View the generated response from OpenAI's GPT model in real-time.

Launch Instructions:
--------------------
1. Open a terminal or command prompt.
2. Navigate to the directory containing this script.
3. Run the following command:

    streamlit run basic_app.py

Requirements:
-------------
1. `constants.py`:
    - Contains the OpenAI API key in a variable `openai_key`.
2. Libraries:
    - `os`: For setting environment variables.
    - `streamlit`: For creating the app's UI.
    - `langchain`: For integrating with OpenAI's GPT models.
3. Python Version:
    - Python 3.8 or later is recommended.

Code Organisation:
------------------
1. **Environment Variable Setup**:
    - The OpenAI API key is loaded from the `constants.py` file and set using `os.environ`.

2. **LangChain Integration**:
    - The `OpenAI` class is used to create an instance of the OpenAI GPT model with a temperature setting of 0.8.

3. **Streamlit Interface**:
    - The app provides:
        - A title (`LangChain Demo with OpenAI API`).
        - A text input field for user queries.
        - Display of the model's output dynamically as the user inputs text.
"""

# Import necessary libraries
import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st

# Set OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit application setup
st.title('LangChain Demo with OpenAI API')
input_text = st.text_input("Search the topic you want")

# Initialise OpenAI LLM with specified temperature
llm = OpenAI(temperature=0.8)

# Handle user input and display model output
if input_text:
    st.write(llm(input_text))