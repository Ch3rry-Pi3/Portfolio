"""
This script demonstrates basic text splitting techniques using LangChain.
It covers:

1. Suppressing deprecation warnings.
2. Setting up the OpenAI API using environment variables.
3. Implementing text splitting using:
   - `RecursiveCharacterTextSplitter`
   - `CharacterTextSplitter`

Author: [Roger J. Campbell]
Date: [2025-01-17]
"""

import os
import sys
import warnings
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from helper_functions import setup_openai_api

def main():
    """
    Main function demonstrating text splitting using LangChain.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    
    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()
    
    # Step 3: Define chunking parameters
    chunk_size = 26
    chunk_overlap = 4
    
    # Step 4: Initialize text splitters
    r_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    
    c_splitter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    
    # Step 5: Define sample text inputs
    text1 = 'abcdefghijklmnopqrstuvwxyz'
    text2 = 'abcdefghijklmnopqrstuvwxyzabcdefg'
    text3 = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    
    # Step 6: Demonstrate RecursiveCharacterTextSplitter
    print("Step 6: RecursiveCharacterTextSplitter Results:")
    print(r_splitter.split_text(text1))
    print(r_splitter.split_text(text2))
    print(r_splitter.split_text(text3))
    
    # Step 7: Demonstrate CharacterTextSplitter
    print("\nStep 7: CharacterTextSplitter Results:")
    print(c_splitter.split_text(text3))
    
    # Step 8: Reinitialize CharacterTextSplitter with a space separator
    c_splitter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separator=' '
    )
    
    print("\nStep 8: CharacterTextSplitter with Space Separator:")
    print(c_splitter.split_text(text3))

if __name__ == "__main__":
    # Step 9: Execute main function
    main()
