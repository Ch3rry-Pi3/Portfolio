"""
Simple RAG Pipeline from Scratch with OpenAI and ChromaDB

This program loads documents from a directory, splits them into chunks, generates embeddings using OpenAI's embedding API,
stores them in a ChromaDB collection, and provides a query-based retrieval system. Users can query the database for relevant
document chunks, which are then used to generate concise answers via OpenAI's GPT-3.5-Turbo.

Main Features:
1. Load documents from a specified directory.
2. Split documents into manageable text chunks for processing.
3. Generate embeddings for text chunks using OpenAI's embedding model.
4. Store the chunks and their embeddings in a persistent ChromaDB collection.
5. Query the database for relevant document chunks based on a user question.
6. Generate a concise answer from the retrieved chunks using OpenAI's language model.
"""

import os
from dotenv import load_dotenv
import chromadb
from openai import OpenAI
from chromadb.utils import embedding_functions

# Load environment variables from .env file
load_dotenv()

# ==========================
# 1. Configuration Setup
# ==========================
openai_key = os.getenv("OPENAI_API_KEY")

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=openai_key, model_name="text-embedding-3-small"
)

# Initialise the Chroma client with persistence
chroma_client = chromadb.PersistentClient(path="chroma_persistent_storage")
collection_name = "document_qa_collection"
collection = chroma_client.get_or_create_collection(
    name=collection_name, embedding_function=openai_ef
)

client = OpenAI(api_key=openai_key)

# ==========================
# 2. Utility Functions
# ==========================

def load_documents_from_directory(directory_path):
    """
    Load text documents from a specified directory.

    Args:
        directory_path (str): Path to the directory containing text files.

    Returns:
        list: A list of dictionaries, each containing 'id' (filename) and 'text' (file content).
    """
    print("==== Loading documents from directory ====")
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            with open(
                os.path.join(directory_path, filename), "r", encoding="utf-8"
            ) as file:
                documents.append({"id": filename, "text": file.read()})
    return documents

def split_text(text, chunk_size=1000, chunk_overlap=20):
    """
    Split text into chunks of a specified size with overlap.

    Args:
        text (str): The text to split.
        chunk_size (int): Maximum size of each chunk.
        chunk_overlap (int): Number of overlapping characters between chunks.

    Returns:
        list: A list of text chunks.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - chunk_overlap
    return chunks

def get_openai_embedding(text):
    """
    Generate an embedding for a given text using OpenAI's embedding API.

    Args:
        text (str): The input text to embed.

    Returns:
        list: A vector embedding for the input text.
    """
    response = client.embeddings.create(input=text, model="text-embedding-3-small")
    embedding = response.data[0].embedding
    print("==== Generating embeddings... ====")
    return embedding

def query_documents(question, n_results=2):
    """
    Query the ChromaDB collection for the most relevant document chunks.

    Args:
        question (str): The query question.
        n_results (int): Number of top results to retrieve.

    Returns:
        list: Relevant document chunks.
    """
    results = collection.query(query_texts=question, n_results=n_results)

    # Extract the relevant chunks
    relevant_chunks = [doc for sublist in results["documents"] for doc in sublist]
    print("==== Returning relevant chunks ====")
    return relevant_chunks

def generate_response(question, relevant_chunks):
    """
    Generate a concise response to a question using retrieved context and OpenAI's GPT-3.5-Turbo.

    Args:
        question (str): The query question.
        relevant_chunks (list): List of relevant document chunks.

    Returns:
        str: Generated response to the question.
    """
    context = "\n\n".join(relevant_chunks)
    prompt = (
        "You are an assistant for question-answering tasks. Use the following pieces of "
        "retrieved context to answer the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the answer concise."
        "\n\nContext:\n" + context + "\n\nQuestion:\n" + question
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": question,
            },
        ],
    )

    answer = response.choices[0].message
    return answer

# ==========================
# 3. Main Function
# ==========================

def main():
    """
    Main function to execute the document QA pipeline.
    """
    # Load documents from the directory
    directory_path = "./news_articles"
    documents = load_documents_from_directory(directory_path)

    print(f"Loaded {len(documents)} documents")

    # Split documents into chunks
    chunked_documents = []
    for doc in documents:
        chunks = split_text(doc["text"])
        print("==== Splitting docs into chunks ====")
        for i, chunk in enumerate(chunks):
            chunked_documents.append({"id": f"{doc['id']}_chunk{i+1}", "text": chunk})

    # Generate embeddings for the document chunks
    for doc in chunked_documents:
        print("==== Generating embeddings... ====")
        doc["embedding"] = get_openai_embedding(doc["text"])

    # Upsert documents with embeddings into ChromaDB
    for doc in chunked_documents:
        print("==== Inserting chunks into db... ====")
        collection.upsert(
            ids=[doc["id"]], documents=[doc["text"]], embeddings=[doc["embedding"]]
        )

    # Example query and response generation
    question = "Tell me about DataBricks."
    relevant_chunks = query_documents(question)
    answer = generate_response(question, relevant_chunks)

    print(answer)

# ==========================
# 4. Entry Point
# ==========================
if __name__ == "__main__":
    main()