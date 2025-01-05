"""
RAG with Multiple Queries and Re-ranking

This script demonstrates a retrieval-augmented generation (RAG) pipeline with multiple hardcoded queries 
and re-ranking. The pipeline retrieves relevant documents, re-ranks them using a cross-encoder model, 
and generates a final response using an LLM.

Steps include:
1. Loading and preprocessing a PDF document.
2. Splitting text into manageable chunks using advanced text-splitting techniques.
3. Generating embeddings for text chunks and storing them in a ChromaDB vector store.
4. Retrieving relevant documents using multiple queries.
5. Re-ranking the retrieved documents using a cross-encoder.
6. Generating a final answer using the most relevant documents.
"""

# ==========================
# 1. Import Libraries
# ==========================
import os
from dotenv import load_dotenv
from pypdf import PdfReader
import chromadb
import numpy as np
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from sentence_transformers import CrossEncoder
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    SentenceTransformersTokenTextSplitter,
)
from openai import OpenAI
from helper_utils import word_wrap  # Helper function for formatted text wrapping

# ==========================
# 2. Configuration Setup
# ==========================
# Load environment variables from .env file
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_key)

# Initialise embedding function
embedding_function = SentenceTransformerEmbeddingFunction()

# ==========================
# 3. Load and Preprocess PDF
# ==========================
def load_pdf_text(pdf_path):
    """Loads and extracts text from a PDF."""
    reader = PdfReader(pdf_path)
    pdf_texts = [p.extract_text().strip() for p in reader.pages]
    return [text for text in pdf_texts if text]  # Filter empty strings

# ==========================
# 4. Text Splitting
# ==========================
def split_text(texts):
    """Splits text into manageable chunks using character and token splitting."""
    character_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""], chunk_size=1000, chunk_overlap=0
    )
    character_split_texts = character_splitter.split_text("\n\n".join(texts))

    token_splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=0, tokens_per_chunk=256)
    token_split_texts = []
    for text in character_split_texts:
        token_split_texts += token_splitter.split_text(text)
    
    return token_split_texts

# ==========================
# 5. ChromaDB Setup and Embedding Generation
# ==========================
def setup_chromadb(text_chunks):
    """Sets up ChromaDB and adds embeddings for text chunks."""
    chroma_client = chromadb.Client()
    chroma_collection = chroma_client.get_or_create_collection(
        "microsoft-collection", embedding_function=embedding_function
    )
    ids = [str(i) for i in range(len(text_chunks))]
    chroma_collection.add(ids=ids, documents=text_chunks)
    return chroma_collection

# ==========================
# 6. Query Expansion and Retrieval
# ==========================
def retrieve_documents(collection, queries, top_k=10):
    """Retrieves documents using multiple queries."""
    results = collection.query(query_texts=queries, n_results=top_k, include=["documents"])
    # Deduplicate documents
    unique_documents = set()
    for documents in results["documents"]:
        unique_documents.update(documents)
    return list(unique_documents)

# ==========================
# 7. Re-ranking
# ==========================
def rerank_documents(query, documents, model_name="cross-encoder/ms-marco-MiniLM-L-6-v2"):
    """Re-ranks documents using a cross-encoder."""
    cross_encoder = CrossEncoder(model_name)
    pairs = [[query, doc] for doc in documents]
    scores = cross_encoder.predict(pairs)
    ranked_indices = np.argsort(scores)[::-1]  # Sort scores in descending order
    top_documents = [documents[i] for i in ranked_indices]
    return top_documents, scores

# ==========================
# 8. Generate Final Answer
# ==========================
def generate_final_answer(query, context, model="gpt-3.5-turbo"):
    """Generates the final answer using an LLM."""
    prompt = f"""
    You are a knowledgeable financial research assistant. 
    Your users are inquiring about an annual report. 
    Based on the following context, answer the user's question:

    Context:
    {context}

    Question:
    {query}
    """
    messages = [{"role": "system", "content": prompt}]
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content.strip()

# ==========================
# 9. Main Function
# ==========================
def main():
    # Load and preprocess PDF
    pdf_path = "data/microsoft-annual-report.pdf"
    pdf_texts = load_pdf_text(pdf_path)

    # Split text into chunks
    token_split_texts = split_text(pdf_texts)

    # Setup ChromaDB and add embeddings
    chroma_collection = setup_chromadb(token_split_texts)

    # Original query and expanded queries
    original_query = "What were the most important factors that contributed to increases in revenue?"
    expanded_queries = [
        "What were the major drivers of revenue growth?",
        "Were there any new product launches that contributed to the increase in revenue?",
        "Did any changes in pricing or promotions impact the revenue growth?",
        "What were the key market trends that facilitated the increase in revenue?",
        "Did any acquisitions or partnerships contribute to the revenue growth?",
    ]
    queries = [original_query] + expanded_queries

    # Retrieve and deduplicate documents
    unique_documents = retrieve_documents(chroma_collection, queries)

    # Re-rank retrieved documents
    top_documents, scores = rerank_documents(original_query, unique_documents)

    # Select top documents and generate context
    top_k = 5
    top_context = "\n\n".join(top_documents[:top_k])

    # Generate the final answer
    final_answer = generate_final_answer(original_query, top_context)
    print("\nFinal Answer:\n")
    print(final_answer)

# ==========================
# 10. Entry Point
# ==========================
if __name__ == "__main__":
    main()
