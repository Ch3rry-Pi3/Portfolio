"""
This script demonstrates context-aware text splitting using LangChain.
It covers:

1. Suppressing deprecation warnings.
2. Setting up the OpenAI API using environment variables.
3. Implementing text splitting using `MarkdownHeaderTextSplitter`.

Author: [Roger J. Campbell]
Date: [2025-01-17]
"""

import os
import sys
import warnings
from langchain.text_splitter import MarkdownHeaderTextSplitter
from helper_functions import setup_openai_api

def main():
    """
    Main function demonstrating markdown-based text splitting using LangChain.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    
    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()
    
    # Step 3: Define markdown document
    markdown_document = """# Title\n\n \
    ## Chapter 1\n\n \
    Hi this is Jim\n\n Hi this is Joe\n\n \
    ### Section \n\n \
    Hi this is Lance \n\n 
    ## Chapter 2\n\n \
    Hi this is Molly"""
    
    # Step 4: Define headers for splitting
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
    
    # Step 5: Initialise and apply the MarkdownHeaderTextSplitter
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on
    )
    
    md_header_splits = markdown_splitter.split_text(markdown_document)
    
    # Step 6: Print split results
    print("Step 6: First Split Segment:")
    print(md_header_splits[0])
    
    print("\nStep 7: Second Split Segment:")
    print(md_header_splits[1])

if __name__ == "__main__":
    # Step 8: Execute main function
    main()
