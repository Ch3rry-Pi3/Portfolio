"""
This script demonstrates text embedding using LangChain.
It covers:

1. Suppressing deprecation warnings.
2. Setting up the OpenAI API using environment variables.
3. Loading and processing PDF documents.
4. Implementing text splitting with `RecursiveCharacterTextSplitter`.
5. Generating and comparing text embeddings using OpenAI.

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

def generate_embeddings():
    """
    Step 5: Generate embeddings for text sentences and compute similarity.
    """
    embedding = OpenAIEmbeddings()
    
    sentence1 = "i like dogs"
    sentence2 = "i like canines"
    sentence3 = "the weather is ugly outside"
    
    embedding1 = embedding.embed_query(sentence1)
    embedding2 = embedding.embed_query(sentence2)
    embedding3 = embedding.embed_query(sentence3)
    
    print("Similarity between sentence1 and sentence2:", np.dot(embedding1, embedding2))
    print("Similarity between sentence1 and sentence3:", np.dot(embedding1, embedding3))
    print("Similarity between sentence2 and sentence3:", np.dot(embedding2, embedding3))

def main():
    """
    Main function to execute the script in sequential steps.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    
    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()
    
    # Step 3: Load documents
    documents = load_documents()
    
    # Step 4: Split documents into smaller chunks
    splits = split_documents(documents)
    
    # Step 5: Generate and compare embeddings
    generate_embeddings()

if __name__ == "__main__":
    # Execute main function
    main()
