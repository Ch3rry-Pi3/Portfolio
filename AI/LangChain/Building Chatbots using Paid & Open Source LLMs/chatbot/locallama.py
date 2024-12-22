"""LangChain Streamlit App with LLAMA2 API Integration

This Streamlit application demonstrates the use of LangChain's prompt templates 
and the LLAMA2 model via LangChain to process and respond to user queries.

Parameters:
----------
dotenv : module
    Used to load environment variables from a `.env` file.

os : module
    Used to set and retrieve environment variables for LangChain and OpenAI keys.

streamlit : module
    Used to create an interactive and user-friendly web app interface.

ChatPromptTemplate : class
    LangChain class for defining templates to generate prompts for the language model.

ChatOpenAI : class
    LangChain class to interact with OpenAI's chat models.

Ollama : class
    LangChain class to interact with LLAMA2 API.

StrOutputParser : class
    LangChain class to parse and format the output from the language model.

Returns:
-------
Streamlit Application:
    - Accepts a user query via a text input.
    - Passes the query to the LLAMA2 model via LangChain.
    - Displays the model's response in the Streamlit interface.

Launch Instructions:
--------------------
1. Ensure the `.env` file is set up with the following keys:
    - LANGCHAIN_API_KEY
    - LLAMA2_API_KEY (if required)

2. Install necessary dependencies:
    - Run `pip install langchain streamlit dotenv`.

3. Run the application:
    - Navigate to the project directory in the terminal.
    - Run `streamlit run app.py`.

Code Organisation:
------------------
1. **Environment Setup**:
    - Loads environment variables using the `dotenv` library.

2. **Prompt Template**:
    - Defines a chat prompt template for the chatbot's behavior.

3. **LLM Initialization**:
    - Initializes the LLAMA2 model using LangChain's Ollama class.

4. **Streamlit Interface**:
    - Accepts user input and displays the model's response interactively.
"""

# Import necessary libraries
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set environment variables for LangChain
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Define the chat prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit interface
def main():
    """
    Main function to render the Streamlit application.
    """
    st.title('LangChain Demo With LLAMA2 API')

    # Input box for user query
    input_text = st.text_input("Search the topic you want:")

    if input_text:
        # Initialize the LLAMA2 model via LangChain
        llm = Ollama(model="llama2")
        output_parser = StrOutputParser()

        # Combine the prompt template, model, and output parser into a chain
        chain = prompt | llm | output_parser

        # Get the response from the chain
        response = chain.invoke({"question": input_text})

        # Display the model's response
        st.write(response)

# Run the Streamlit app
if __name__ == '__main__':
    main()