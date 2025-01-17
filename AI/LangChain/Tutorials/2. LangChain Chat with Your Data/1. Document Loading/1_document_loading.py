"""
This script demonstrates various document loading techniques using LangChain, including:

1. Suppressing deprecation warnings.
2. Setting up the OpenAI API using environment variables.
3. Loading documents from different sources:
   - PDFs using `PyPDFLoader`
   - YouTube videos using `YoutubeAudioLoader` with `OpenAIWhisperParser`
   - Web pages using `WebBaseLoader`

Author: [Roger J. Campbell]
Date: [2025-01-17]
"""

import os
import sys
import warnings
from helper_functions import setup_openai_api
from langchain.document_loaders import PyPDFLoader, WebBaseLoader
from langchain.document_loaders.generic import GenericLoader, FileSystemBlobLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader

def main():
    """
    Main function demonstrating document loading from various sources.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()

    # Step 3: Add project path (if necessary)
    sys.path.append('../..')

    # Step 4: Load a PDF document
    pdf_path = "documents/MachineLearning-Lecture01.pdf"
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    print(f"Loaded {len(pages)} pages from PDF.")
    print("Sample page content:")
    print(pages[0].page_content[:500])
    print("Metadata:", pages[0].metadata)

    # Step 5: Load audio from a YouTube video and transcribe it
    youtube_url = "https://www.youtube.com/watch?v=jGwO_UgTS7I"
    save_dir = "documents/youtube/"
    loader = GenericLoader(
        YoutubeAudioLoader([youtube_url], save_dir),  # Fetch from YouTube
        OpenAIWhisperParser()
    )
    docs = loader.load()

    print("Sample transcribed content from YouTube video:")
    print(docs[0].page_content[:500])

    # Step 6: Load content from a webpage
    web_url = "https://github.com/basecamp/handbook/blob/master/titles-for-programmers.md"
    loader = WebBaseLoader(web_url)
    docs = loader.load()

    print("Sample webpage content:")
    print(docs[0].page_content[:500])

if __name__ == "__main__":
    main()