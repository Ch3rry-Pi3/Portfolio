"""
This script demonstrates alternative retrieval techniques using SVM and TF-IDF retrievers in LangChain.
It covers:

1. Suppressing deprecation warnings.
2. Setting up the OpenAI API using environment variables.
3. Loading and processing PDF documents.
4. Implementing text splitting with `RecursiveCharacterTextSplitter`.
5. Utilising SVM-based and TF-IDF-based retrieval methods.

Author: [Roger J. Campbell]
Date: [2025-01-19]
"""

import warnings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.retrievers import SVMRetriever, TFIDFRetriever
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from helper_functions import setup_openai_api

def load_pdf():
    """
    Step 3: Load PDF document using LangChain's PyPDFLoader.
    """
    loader = PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture01.pdf")
    pages = loader.load()
    return " ".join([p.page_content for p in pages])

def split_text(text):
    """
    Step 4: Split text using RecursiveCharacterTextSplitter.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
    return text_splitter.split_text(text)

def setup_retrievers(splits, embedding):
    """
    Step 5: Initialise SVM and TF-IDF retrievers.
    """
    svm_retriever = SVMRetriever.from_texts(splits, embedding)
    tfidf_retriever = TFIDFRetriever.from_texts(splits)
    return svm_retriever, tfidf_retriever

def retrieve_documents(svm_retriever, tfidf_retriever):
    """
    Step 6: Perform retrieval using SVM and TF-IDF retrievers.
    """
    question1 = "What are major topics for this class?"
    docs_svm = svm_retriever.get_relevant_documents(question1)
    print("SVM Retriever Result:", docs_svm[0].page_content[:200])
    
    question2 = "What did they say about MATLAB?"
    docs_tfidf = tfidf_retriever.get_relevant_documents(question2)
    print("TF-IDF Retriever Result:", docs_tfidf[0].page_content[:200])

def main():
    """
    Main function to execute the script in sequential steps.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    
    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()
    
    # Step 3: Load and process PDF text
    text = load_pdf()
    
    # Step 4: Split text into chunks
    splits = split_text(text)
    
    # Step 5: Set up retrievers
    embedding = OpenAIEmbeddings()
    svm_retriever, tfidf_retriever = setup_retrievers(splits, embedding)
    
    # Step 6: Perform retrieval tasks
    retrieve_documents(svm_retriever, tfidf_retriever)

if __name__ == "__main__":
    # Execute main function
    main()
