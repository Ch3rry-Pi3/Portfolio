"""ChatGroq Streamlit Application

This application demonstrates the integration of LangChain with ChatGroq's API for dynamic query processing. 
It showcases how to use embeddings, vector databases, and retrieval chains to build an interactive application.

The application performs the following:
- Embedding and vectorsation of web-based documents.
- Retrieval of relevant document chunks based on user queries.
- Context-aware responses using ChatGroq's language model.

Parameters:
-----------
os : module
    Used to set environment variables for the Groq API key.
st : module
    Streamlit framework for building interactive web applications.
time : module
    Measures the response time for processing queries.

Modules and Classes:
--------------------
ChatGroq : class
    LangChain class for interacting with the ChatGroq model.
WebBaseLoader : class
    LangChain class for loading web-based documents.
OllamaEmbeddings : class
    LangChain class for creating embeddings using Llama 3.1.
RecursiveCharacterTextSplitter : class
    LangChain utility for splitting documents into chunks.
FAISS : class
    LangChain vector database for storing embeddings.
ChatPromptTemplate : class
    LangChain utility for creating prompt templates.
create_stuff_documents_chain : function
    Combines documents and language model interactions into a single chain.
create_retrieval_chain : function
    Creates a chain for querying a retriever and processing results.

Returns:
--------
Streamlit Application:
    - Interactive user interface for querying documents.
    - Provides document similarity results alongside answers.

Launch Instructions:
--------------------
1. Ensure the `.env` file is set up with the Groq API key:
    - GROQ_API_KEY

2. Run the Streamlit application:
    ```
    streamlit run app.py
    ```

3. Navigate to the provided URL in your browser to interact with the application.
"""

# Import required libraries and modules
import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import time

# Load environment variables from the .env file
load_dotenv()

# Retrieve the Groq API key from environment variables
groq_api_key = os.environ.get('GROQ_API_KEY')

# Initialise embeddings and vector database in Streamlit's session state
if "vector" not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings(model="llama3.1")                    # Initialise embeddings with Llama 3.1
    st.session_state.loader = WebBaseLoader("https://docs.smith.langchain.com/")        # Load the LangSmith documentation
    st.session_state.docs = st.session_state.loader.load()                              # Load documents from the webpage

    # Split documents into chunks
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:50])

    # Create a FAISS vector store from the document chunks
    st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

# Display the application title
st.title("ChatGroq Demo")

# Initialise the ChatGroq language model
llm = ChatGroq(
    groq_api_key=groq_api_key,                          # Groq API key
    model_name="mixtral-8x7b-32768"                     # Model name for ChatGroq
)

# Define a prompt template for interacting with the LLM
prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question.
    <context>
    {context}
    <context>
    Questions: {input}
    """
)

# Create a document processing chain
document_chain = create_stuff_documents_chain(llm, prompt)

# Create a retriever from the FAISS vector store
retriever = st.session_state.vectors.as_retriever()

# Create a retrieval chain
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# Create an input field for user prompts
prompt = st.text_input("Input your prompt here")

# Process the user query if a prompt is provided
if prompt:
    start = time.process_time()  # Record the start time
    response = retrieval_chain.invoke({"input": prompt})            # Invoke the retrieval chain with the user input
    elapsed_time = time.process_time() - start                      # Calculate the response time

    # Display the response and the response time
    st.write("Response time:", elapsed_time)
    st.write(response['answer'])

    # Expandable section for document similarity search
    with st.expander("Document Similarity Search"):
        # Display relevant document chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")