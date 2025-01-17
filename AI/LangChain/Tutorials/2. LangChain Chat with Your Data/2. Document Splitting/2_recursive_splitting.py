"""
This script demonstrates advanced text splitting techniques using LangChain.
It covers:

1. Suppressing deprecation warnings.
2. Setting up the OpenAI API using environment variables.
3. Implementing text splitting using:
   - `RecursiveCharacterTextSplitter`
   - `CharacterTextSplitter`
4. Loading and splitting documents from:
   - PDFs using `PyPDFLoader`

Author: [Roger J. Campbell]
Date: [2025-01-17]
"""

import os
import sys
import warnings
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, NotionDirectoryLoader
from helper_functions import setup_openai_api

def main():
    """
    Main function demonstrating recursive text splitting using LangChain.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    
    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()
    
    # Step 3: Define sample text input
    some_text = ("""When writing documents, writers will use document structure to group content. "
                 "This can convey to the reader, which ideas are related. For example, closely related ideas "
                 "are in sentences. Similar ideas are in paragraphs. Paragraphs form a document.\n\n  "
                 "Paragraphs are often delimited with a carriage return or two carriage returns. "
                 "Carriage returns are the 'backslash n' you see embedded in this string. "
                 "Sentences have a period at the end, but also, have a space. "
                 "and words are separated by space."""
                )
    
    print("Step 3: Length of input text:", len(some_text))
    
    # Step 4: Initialise Character and Recursive splitters
    c_splitter = CharacterTextSplitter(
        chunk_size=450,
        chunk_overlap=0,
        separator=' '
    )
    
    r_splitter = RecursiveCharacterTextSplitter(
        chunk_size=450,
        chunk_overlap=0,
        separators=["\n\n", "\n", " ", ""]
    )
    
    print("Step 4: CharacterTextSplitter Results:")
    print(c_splitter.split_text(some_text))
    
    print("\nStep 5: RecursiveCharacterTextSplitter Results:")
    print(r_splitter.split_text(some_text))
    
    # Step 6: Refining RecursiveCharacterTextSplitter with different separators
    r_splitter = RecursiveCharacterTextSplitter(
        chunk_size=150,
        chunk_overlap=0,
        separators=["\n\n", "\n", "\. ", " ", ""]
    )
    r_splitter.split_text(some_text)
    
    r_splitter = RecursiveCharacterTextSplitter(
        chunk_size=150,
        chunk_overlap=0,
        separators=["\n\n", "\n", "(?<=\. )", " ", ""]
    )
    r_splitter.split_text(some_text)
    
    # Step 7: Load and split a PDF document
    loader = PyPDFLoader("documents/MachineLearning-Lecture01.pdf")
    pages = loader.load()
    
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    
    docs = text_splitter.split_documents(pages)
    
    print("Step 7: PDF Document Splitting:")
    print("Number of pages:", len(pages))
    print("Number of split documents:", len(docs))
    

if __name__ == "__main__":
    # Step 9: Execute main function
    main()
