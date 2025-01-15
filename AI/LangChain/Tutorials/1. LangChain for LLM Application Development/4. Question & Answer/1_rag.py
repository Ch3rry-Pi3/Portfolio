"""
This script demonstrates the use of LangChain's Q&A capabilities, including:
1. Setting up the OpenAI API using environment variables.
2. Dynamically selecting the appropriate GPT model based on the current date.
3. Using a CSVLoader to load documents for vector-based retrieval.
4. Initialising embeddings and vectorstore for document similarity search.
5. Using LangChain's RetrievalQA module for answering queries based on document retrieval.

Author: [Roger J. Campbell]
Date: [2025-01-15]
"""

import warnings
from helper_functions import setup_openai_api, determine_model
from langchain_openai import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA

def main():
    """
    Main function demonstrating Q&A capabilities with LangChain's RetrievalQA module.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()

    # Step 3: Determine which model to use based on the current date
    llm_model = determine_model()

    # Step 4: Initialise the chat model with specified temperature
    llm = ChatOpenAI(temperature=0.0, model=llm_model)

    # Step 5: Load documents from a CSV file
    file_path = 'OutdoorClothingCatalog_1000.csv'
    loader = CSVLoader(file_path=file_path)
    documents = loader.load()

    # Step 6: Initialise embeddings and create a vectorstore
    embeddings = OpenAIEmbeddings()
    vectorstore = DocArrayInMemorySearch.from_documents(documents, embeddings)

    # Step 7: Create a retriever for document similarity search
    retriever = vectorstore.as_retriever()

    # Step 8: Demonstrate embedding query example
    query_embedding = embeddings.embed_query("Hi my name is Harrison")
    print(f"Embedding length: {len(query_embedding)}")
    print(f"First 5 dimensions of the embedding: {query_embedding[:5]}")

    # Step 9: Example query for document similarity search
    query = "Please suggest a shirt with sunblocking"
    similar_docs = retriever.get_relevant_documents(query)
    print(f"Number of relevant documents: {len(similar_docs)}")
    if similar_docs:
        print(f"First document content: {similar_docs[0].page_content}")

    # Step 10: Use RetrievalQA to answer a query based on retrieved documents
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, verbose=True)

    # Example query for summarising shirts with sun protection
    final_query = "Please list all your shirts with sun protection in a table and summarise each one."
    response = qa_chain.run(final_query)
    print("Response from RetrievalQA:")
    print(response)

if __name__ == "__main__":
    main()
