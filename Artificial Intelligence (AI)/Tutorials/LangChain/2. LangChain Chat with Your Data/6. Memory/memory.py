"""
This script implements a conversational retrieval-based question answering (QA) system using LangChain.
It covers:

1. Suppressing deprecation warnings.
2. Setting up the OpenAI API using environment variables.
3. Initialising a Chroma vector database with OpenAI embeddings.
4. Performing similarity search on the vector database.
5. Constructing a retrieval-based QA pipeline.
6. Implementing conversational memory to retain past interactions.

Author: [Roger J. Campbell]
Date: [2025-02-09]
"""

import warnings
from helper_functions import setup_openai_api, determine_model
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

def setup_vector_db():
    """
    Step 3: Initialise the Chroma vector database using OpenAI embeddings.
    """
    persist_directory = 'documents/chroma/'
    embedding = OpenAIEmbeddings()
    return Chroma(persist_directory=persist_directory, embedding_function=embedding)

def setup_qa_pipeline(vectordb, llm):
    """
    Step 5: Set up the retrieval-based QA system.

    Args:
        vectordb (Chroma): The vector database instance.
        llm (ChatOpenAI): The language model to use.

    Returns:
        RetrievalQA: The QA chain instance.
    """
    template = """Use the following pieces of context to answer the question at the end. 
    If you don't know the answer, just say that you don't know. 
    Use three sentences maximum. Keep the answer concise. 
    Always say 'Thanks for asking!' at the end.
    
    {context}
    
    Question: {question}
    Helpful Answer:"""
    
    QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"], template=template)
    
    return RetrievalQA.from_chain_type(
        llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )

def setup_conversational_chain(vectordb, llm):
    """
    Step 6: Set up the conversational retrieval-based QA system with memory.

    Args:
        vectordb (Chroma): The vector database instance.
        llm (ChatOpenAI): The language model to use.

    Returns:
        ConversationalRetrievalChain: The conversational QA chain.
    """
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    return ConversationalRetrievalChain.from_llm(
        llm,
        retriever=vectordb.as_retriever(),
        memory=memory
    )

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
    docs = vectordb.similarity_search(question, k=3)
    print(f"Retrieved {len(docs)} documents.")
    
    # Step 5: Set up the QA pipeline
    llm_name = determine_model()
    llm = ChatOpenAI(model_name=llm_name, temperature=0)
    print(llm.predict("Hello world!"))
    
    qa_chain = setup_qa_pipeline(vectordb, llm)
    
    # Query the QA pipeline
    question = "Is probability a class topic?"
    result = qa_chain({"query": question})
    print(result["result"])
    
    # Step 6: Set up and test conversational retrieval-based QA system
    qa_conversational = setup_conversational_chain(vectordb, llm)
    
    question = "Is probability a class topic?"
    result = qa_conversational({"question": question})
    print(result["answer"])
    
    question = "Why are those prerequisites needed?"
    result = qa_conversational({"question": question})
    print(result["answer"])

if __name__ == "__main__":
    # Execute main function
    main()
