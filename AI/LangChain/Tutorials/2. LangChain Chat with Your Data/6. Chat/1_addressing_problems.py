"""
This script demonstrates advanced retrieval techniques in LangChain.
It covers:

1. Suppressing deprecation warnings.
2. Setting up the OpenAI API using environment variables.
3. Implementing similarity search with Chroma vector store.
4. Addressing retrieval limitations using maximal marginal relevance (MMR).
5. Enhancing specificity with metadata filtering and self-query retriever.
6. Improving efficiency with contextual compression retriever.

Author: [Roger J. Campbell]
Date: [2025-01-19]
"""

import warnings
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from helper_functions import setup_openai_api

def setup_vector_store():
    """
    Step 3: Initialise the Chroma vector store and embeddings.
    """
    persist_directory = 'documents/chroma/'
    embedding = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
    return vectordb, embedding

def perform_similarity_search(vectordb, embedding):
    """
    Step 4: Perform similarity search on a small example database.
    """
    texts = [
        """The Amanita phalloides has a large and imposing epigeous (aboveground) fruiting body (basidiocarp).""",
        """A mushroom with a large fruiting body is the Amanita phalloides. Some varieties are all-white.""",
        """A. phalloides, a.k.a Death Cap, is one of the most poisonous of all known mushrooms.""",
    ]
    smalldb = Chroma.from_texts(texts, embedding=embedding)
    question = "Tell me about all-white mushrooms with large fruiting bodies"
    print(smalldb.similarity_search(question, k=2))
    print(smalldb.max_marginal_relevance_search(question, k=2, fetch_k=3))

def demonstrate_mmr(vectordb):
    """
    Step 5: Address diversity in retrieval using Maximal Marginal Relevance (MMR).
    """
    question = "what did they say about matlab?"
    docs_ss = vectordb.similarity_search(question, k=3)
    docs_mmr = vectordb.max_marginal_relevance_search(question, k=3)
    
    for i, doc in enumerate(docs_ss[:2]):
        print(f"Standard Similarity Search Doc {i+1}: {doc.page_content[:100]}")
    for i, doc in enumerate(docs_mmr[:2]):
        print(f"MMR Search Doc {i+1}: {doc.page_content[:100]}")

def filter_by_metadata(vectordb):
    """
    Step 6: Use metadata filtering to improve specificity.
    """
    question = "what did they say about regression in the third lecture?"
    docs = vectordb.similarity_search(question, k=3, filter={"source": "docs/cs229_lectures/MachineLearning-Lecture03.pdf"})
    for d in docs:
        print(d.metadata)

def setup_self_query_retriever(vectordb):
    """
    Step 7: Implement SelfQueryRetriever for metadata-aware retrieval.
    """
    metadata_field_info = [
        AttributeInfo(
            name="source",
            description="The lecture the chunk is from",
            type="string",
        ),
        AttributeInfo(
            name="page",
            description="The page from the lecture",
            type="integer",
        ),
    ]
    document_content_description = "Lecture notes"
    llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0)
    retriever = SelfQueryRetriever.from_llm(llm, vectordb, document_content_description, metadata_field_info, verbose=True)
    
    question = "what did they say about regression in the third lecture?"
    docs = retriever.get_relevant_documents(question)
    for d in docs:
        print(d.metadata)

def setup_compression_retriever(vectordb):
    """
    Step 8: Improve efficiency using a contextual compression retriever.
    """
    llm = OpenAI(temperature=0, model="gpt-3.5-turbo-instruct")
    compressor = LLMChainExtractor.from_llm(llm)
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor,
        base_retriever=vectordb.as_retriever()
    )
    question = "what did they say about matlab?"
    compressed_docs = compression_retriever.get_relevant_documents(question)
    pretty_print_docs(compressed_docs)

def pretty_print_docs(docs):
    """
    Helper function to display documents in a readable format.
    """
    print(f"\n{'-' * 100}\n".join([f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]))

def main():
    """
    Main function to execute the script in sequential steps.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    
    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()
    
    # Step 3: Initialise the Chroma vector store
    vectordb, embedding = setup_vector_store()
    
    # Step 4: Perform similarity search
    perform_similarity_search(vectordb, embedding)
    
    # Step 5: Demonstrate maximal marginal relevance (MMR)
    demonstrate_mmr(vectordb)
    
    # Step 6: Apply metadata filtering
    filter_by_metadata(vectordb)
    
    # Step 7: Use SelfQueryRetriever for metadata-aware retrieval
    setup_self_query_retriever(vectordb)
    
    # Step 8: Implement contextual compression retriever
    setup_compression_retriever(vectordb)

if __name__ == "__main__":
    # Execute main function
    main()
