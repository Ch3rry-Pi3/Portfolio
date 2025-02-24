"""Creates a Streamlit application that integrates LangChain and OpenAI's GPT models 
to provide responses to user queries.

This application demonstrates the use of LangChain's prompt templates and OpenAI's 
LLMs to build an interactive chatbot interface using Streamlit.

Parameters:
----------
openai_key : str
    OpenAI API key loaded from the `.env` file and set as an environment variable.

langchain_key : str
    LangChain API key loaded from the `.env` file and set as an environment variable.

os : module
    Used to set the OpenAI and LangChain API keys as environment variables.

streamlit : module
    Streamlit library for creating the interactive web app interface.

ChatOpenAI : class
    LangChain class for interacting with OpenAI's chat models.

ChatPromptTemplate : class
    LangChain class to define templates for generating chat prompts.

StrOutputParser : class
    LangChain class for parsing and formatting the output from the LLM.

Returns:
-------
Streamlit Application:
    The app allows users to:
    - Enter a question or topic to get a response from the chatbot.
    - Display the chatbot's output interactively.
    - Integrate with OpenAI's GPT models using LangChain.

Launch Instructions:
--------------------
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the following command:

    streamlit run app.py

Requirements:
-------------
1. `.env` File:
    - Contains the following keys:
        - OPENAI_API_KEY
        - LANGCHAIN_API_KEY
2. Libraries:
    - `os`: For setting environment variables.
    - `dotenv`: For loading `.env` files.
    - `streamlit`: For creating the app's UI.
    - `langchain`: For defining and managing prompt templates and parsers.
3. Python Version:
    - Python 3.8 or later is recommended.

Code Organisation:
------------------
1. **Environment Setup**:
    - API keys are loaded from the `.env` file and set as environment variables.

2. **Prompt Template**:
    - Uses `ChatPromptTemplate` to define the system's response behaviour.

3. **Streamlit Interface**:
    - The user enters a query, and the chatbot's response is displayed interactively.
"""

# Import necessary libraries
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Debugging: Print loaded environment variables
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("LANGCHAIN_API_KEY:", os.getenv("LANGCHAIN_API_KEY"))

# Define a prompt template for the chatbot
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit interface
def main():
    """
    Main function to render the Streamlit chatbot application.
    """

    st.title('LangChain Demo with OpenAI')

    # Input box for user query
    input_text = st.text_input("Enter your query:")

    if input_text:
        # Initialise OpenAI LLM and output parser
        llm = ChatOpenAI(model="gpt-3.5-turbo")
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser

        # Get response from the chain
        response = chain.invoke({'question': input_text})

        # Display the chatbot's response
        st.write("Response:")
        st.write(response)

# Run the Streamlit app
if __name__ == '__main__':
    main()