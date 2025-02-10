"""
This script demonstrates potential failure modes in vector store implementation using LangChain.
It covers:

1. Suppressing deprecation warnings.
2. Setting up the OpenAI API using environment variables.
3. Loading and processing PDF documents.
4. Implementing text splitting with `RecursiveCharacterTextSplitter`.
5. Generating embeddings using OpenAI.
6. Storing embeddings in a vector database using Chroma.
7. Performing similarity search queries and handling failure cases.

Author: [Roger J. Campbell]
Date: [2025-01-18]
"""

import os
import sys
import warnings
import numpy as np
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from helper_functions import setup_openai_api

def load_documents():
    """
    Step 3: Load PDF documents using LangChain's PyPDFLoader.
    """
    loaders = [
        PyPDFLoader("documents/MachineLearning-Lecture01.pdf"),
        PyPDFLoader("documents/MachineLearning-Lecture01.pdf"),
        PyPDFLoader("documents/MachineLearning-Lecture02.pdf"),
        PyPDFLoader("documents/MachineLearning-Lecture03.pdf")
    ]
    documents = []
    for loader in loaders:
        documents.extend(loader.load())
    return documents

def split_documents(documents):
    """
    Step 4: Split text using RecursiveCharacterTextSplitter.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=150
    )
    return text_splitter.split_documents(documents)

def store_in_vector_db(splits):
    """
    Step 5: Store embeddings in a vector database (Chroma) and handle failure cases.
    """
    embedding = OpenAIEmbeddings()
    persist_directory = "documents/chroma/"
    
    try:
        # Initialise Chroma vector store
        vectordb = Chroma.from_documents(
            documents=splits,
            embedding=embedding,
            persist_directory=persist_directory
        )
        
        # Perform similarity search
        question = "is there an email i can ask for help"
        results = vectordb.similarity_search(question, k=5)
        
        print("Number of relevant documents found:", len(results))
        for i, doc in enumerate(results):
            print(f"Document {i + 1} content:")
            print(doc.page_content)
        
        # Persist the vector database
        vectordb.persist()
    except Exception as e:
        print("Error encountered during vector store operations:", str(e))

def main():
    """
    Main function to execute the script in sequential steps and handle potential failures.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    
    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()
    
    # Step 3: Load documents
    documents = load_documents()
    
    # Step 4: Split documents into smaller chunks
    splits = split_documents(documents)
    
    # Step 5: Store embeddings in a vector database and handle failures
    store_in_vector_db(splits)

if __name__ == "__main__":
    # Execute main function
    main()
