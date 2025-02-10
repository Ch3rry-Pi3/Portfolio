"""
End-to-End RAG Project: Document Q&A with Gemma and Groq

This project demonstrates a retrieval-augmented generation (RAG) pipeline using:
1. **Gemma (Google Generative AI)**: For embeddings and document similarity.
2. **Groq (ChatGroq LLM)**: For question-answering based on document retrieval.
3. **FAISS**: For efficient vector-based similarity search.
4. **Streamlit**: For building an interactive user interface.

Modules and Libraries:
- **LangChain**: For chaining document retrieval and LLM-based responses.
- **Streamlit**: For the interactive interface.
- **FAISS**: For embedding storage and retrieval.
"""

# Import necessary libraries
import streamlit as st  # For interactive UI
import os               # For environment variable management
from dotenv import load_dotenv  # To load environment variables securely

# Import LangChain components
from langchain_groq import ChatGroq  # LLM integration with ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Splits documents into manageable chunks
from langchain.chains.combine_documents import create_stuff_documents_chain  # Combines documents for processing
from langchain_core.prompts import ChatPromptTemplate  # Creates prompt templates
from langchain.chains import create_retrieval_chain  # Creates retrieval-based chains
from langchain_community.vectorstores import FAISS  # Vector database for similarity search
from langchain_community.document_loaders import PyPDFDirectoryLoader  # Loads all PDFs in a directory
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # Generates embeddings using Gemma

# Load environment variables from the .env file
load_dotenv()

# Retrieve API keys from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')  # Groq API Key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")  # Google API Key for embeddings

# Application Title
st.title("Gemma Model Document Q&A")

# Initialize the Groq LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,        # API key for authentication
    model_name="Llama3-8b-8192"      # Model name for the Groq LLM
)

# Define the prompt template for the LLM
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

# Function to create embeddings and vector store
def vector_embedding():
    """
    Initialise embeddings and vector store.

    - Uses GoogleGenerativeAIEmbeddings for embedding text.
    - Loads PDF documents from a specified directory.
    - Splits documents into chunks using RecursiveCharacterTextSplitter.
    - Stores embeddings in a FAISS vector database.
    """
    
    if "vectors" not in st.session_state:
        # Initialise embeddings using Google Generative AI
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        
        # Load documents from the specified directory
        st.session_state.loader = PyPDFDirectoryLoader("./us_census")
        st.session_state.docs = st.session_state.loader.load()
        
        # Split documents into chunks for embedding
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,          # Maximum size of each chunk (in characters)
            chunk_overlap=200         # Overlap between consecutive chunks to preserve context
        )
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:20])

        # Create a FAISS vector store from document chunks
        st.session_state.vectors = FAISS.from_documents(
            st.session_state.final_documents,  # Document chunks
            st.session_state.embeddings        # Embedding model
        )

# Input field for user query
prompt1 = st.text_input("Enter Your Question From Documents")

# Button to trigger document embedding
if st.button("Documents Embedding"):
    vector_embedding()
    st.write("Vector Store DB Is Ready")

import time  # For tracking response time

# Process user query if provided
if prompt1:
    # Create a document processing chain
    document_chain = create_stuff_documents_chain(llm, prompt)

    # Create a retriever from the vector store
    retriever = st.session_state.vectors.as_retriever()

    # Create a retrieval chain for question answering
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # Measure response time
    start = time.process_time()
    response = retrieval_chain.invoke({'input': prompt1})
    response_time = time.process_time() - start
    print("Response time:", response_time)

    # Display the response
    st.write(response['answer'])

    # Expandable section to show document similarity results
    with st.expander("Document Similarity Search"):
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")