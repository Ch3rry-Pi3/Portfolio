"""
This script demonstrates token-based text splitting using LangChain.
It covers:

1. Suppressing deprecation warnings.
2. Setting up the OpenAI API using environment variables.
3. Implementing text splitting using `TokenTextSplitter`.
4. Loading and splitting documents from PDFs using `PyPDFLoader`.

Author: [Roger J. Campbell]
Date: [2025-01-17]
"""

import os
import sys
import warnings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import TokenTextSplitter
from helper_functions import setup_openai_api

def main():
    """
    Main function demonstrating token-based text splitting using LangChain.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    
    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()
    
    # Step 3: Define and split sample text
    text_splitter = TokenTextSplitter(chunk_size=1, chunk_overlap=0)
    text1 = "foo bar bazzyfoo"
    
    print("Step 3: Original Text:")
    print(text1)
    
    print("Step 4: TokenTextSplitter with chunk_size=1:")
    print(text_splitter.split_text(text1))
    
    # Step 5: Initialise TokenTextSplitter with a larger chunk size
    text_splitter = TokenTextSplitter(chunk_size=10, chunk_overlap=0)
    
    # Step 6: Load and split a PDF document
    loader = PyPDFLoader("documents/MachineLearning-Lecture01.pdf")
    pages = loader.load()
    
    docs = text_splitter.split_documents(pages)
    
    print("Step 6: Split PDF Document:")
    print(docs[0])
    print("Metadata of first page:", pages[0].metadata)

if __name__ == "__main__":
    # Step 7: Execute main function
    main()
