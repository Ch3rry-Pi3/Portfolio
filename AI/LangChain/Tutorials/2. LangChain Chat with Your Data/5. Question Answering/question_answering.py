"""
This script demonstrates retrieval-based question answering using LangChain and OpenAI models.
It covers:

1. Suppressing deprecation warnings.
2. Setting up the OpenAI API using environment variables.
3. Initialising a Chroma vector database with OpenAI embeddings.
4. Querying the vector database for document similarity search.
5. Implementing a basic retrieval-based QA system using LangChain.
6. Customising the QA pipeline with different retrieval strategies.

Author: [Roger J. Campbell]
Date: [2025-02-09]
"""

import warnings
from helper_functions import setup_openai_api, determine_model
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


def setup_vector_db():
    """
    Step 3: Initialise the Chroma vector database using OpenAI embeddings.
    """
    persist_directory = 'docs/chroma/'
    embedding = OpenAIEmbeddings()
    return Chroma(persist_directory=persist_directory, embedding_function=embedding)


def query_vector_db(vectordb, question, top_k=3):
    """
    Step 4: Perform a similarity search in the vector database.

    Args:
        vectordb (Chroma): The vector database instance.
        question (str): The query to search for.
        top_k (int): Number of top matching documents to retrieve.

    Returns:
        list: Retrieved document results.
    """
    docs = vectordb.similarity_search(question, k=top_k)
    print(f"Retrieved {len(docs)} documents.")
    return docs


def setup_qa_pipeline(vectordb, model_name):
    """
    Step 5: Set up the retrieval-based QA system.

    Args:
        vectordb (Chroma): The vector database instance.
        model_name (str): The language model to use.

    Returns:
        RetrievalQA: The QA chain instance.
    """
    llm = ChatOpenAI(model_name=model_name, temperature=0)
    return RetrievalQA.from_chain_type(llm, retriever=vectordb.as_retriever())


def run_qa_chain(qa_chain, question):
    """
    Step 6: Query the QA chain.

    Args:
        qa_chain (RetrievalQA): The QA pipeline.
        question (str): The user query.

    Returns:
        str: The model's answer.
    """
    result = qa_chain({"query": question})
    print(result["result"])
    return result["result"]


def setup_custom_qa_chain(vectordb, model_name):
    """
    Step 7: Customise the QA pipeline with a structured prompt template.

    Args:
        vectordb (Chroma): The vector database instance.
        model_name (str): The language model to use.

    Returns:
        RetrievalQA: Customised QA chain instance.
    """
    template = """Use the following pieces of context to answer the question at the end. 
    If you don't know the answer, just say that you don't know. 
    Use three sentences maximum and keep the answer concise. 
    Always say "Thanks for asking!" at the end.
    
    {context}
    
    Question: {question}
    Helpful Answer:"""
    
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    llm = ChatOpenAI(model_name=model_name, temperature=0)
    
    return RetrievalQA.from_chain_type(
        llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )


def test_alternative_chains(vectordb, model_name, question):
    """
    Step 8: Test alternative retrieval chain methods.

    Args:
        vectordb (Chroma): The vector database instance.
        model_name (str): The language model to use.
        question (str): The user query.
    """
    for chain_type in ["map_reduce", "refine"]:
        print(f"\nTesting '{chain_type}' retrieval chain:")
        qa_chain = RetrievalQA.from_chain_type(llm=ChatOpenAI(model_name=model_name), retriever=vectordb.as_retriever(), chain_type=chain_type)
        run_qa_chain(qa_chain, question)


def demonstrate_qa_limitations(qa_chain):
    """
    Step 9: Showcase limitations of retrieval-based QA (lack of memory).

    Args:
        qa_chain (RetrievalQA): The QA pipeline.
    """
    print("\n### Testing QA Chain Without Memory ###")
    
    question1 = "Is probability a class topic?"
    run_qa_chain(qa_chain, question1)

    question2 = "Why are those prerequisites needed?"
    run_qa_chain(qa_chain, question2)


def main():
    """
    Main function to execute the script in sequential steps.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Step 2: Set up the OpenAI API
    setup_openai_api()

    # Step 3: Initialise the vector database
    vectordb = setup_vector_db()

    print(f"Vector DB contains {vectordb._collection.count()} entries.")

    # Step 4: Perform a similarity search
    question = "What are major topics for this class?"
    query_vector_db(vectordb, question)

    # Step 5: Set up the QA pipeline
    model_name = determine_model()
    qa_chain = setup_qa_pipeline(vectordb, model_name)

    # Step 6: Run a basic QA query
    run_qa_chain(qa_chain, question)

    # Step 7: Customise QA chain with prompt template
    qa_chain_custom = setup_custom_qa_chain(vectordb, model_name)
    
    question = "Is probability a class topic?"
    result = run_qa_chain(qa_chain_custom, question)
    print("Source Document:", result)

    # Step 8: Test alternative retrieval chains
    test_alternative_chains(vectordb, model_name, question)

    # Step 9: Demonstrate retrieval QA limitations (lack of memory)
    demonstrate_qa_limitations(qa_chain)


if __name__ == "__main__":
    # Execute main function
    main()
