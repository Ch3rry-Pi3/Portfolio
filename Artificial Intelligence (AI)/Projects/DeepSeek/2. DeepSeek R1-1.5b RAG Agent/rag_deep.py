"""
DocuMind AI - Your Intelligent Document Assistant

This Streamlit-based application processes and analyses research documents using AI.
Users can:
    - Upload PDF documents
    - Extract and process text
    - Perform semantic search using vector embeddings
    - Ask queries and receive AI-powered responses

Technologies used:
    - Streamlit for UI
    - LangChain for NLP pipeline
    - Ollama for language modeling
    - InMemoryVectorStore for document retrieval
"""

import streamlit as st
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

def apply_custom_styles():
    """Applies custom CSS styles to enhance the UI."""
    st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .stChatInput input { background-color: #1E1E1E !important; color: #FFFFFF !important; }
    .stChatMessage[data-testid="stChatMessage"]:nth-child(odd) { background-color: #1E1E1E !important; border: 1px solid #3A3A3A !important; }
    .stChatMessage[data-testid="stChatMessage"]:nth-child(even) { background-color: #2A2A2A !important; border: 1px solid #404040 !important; }
    .stChatMessage .avatar { background-color: #00FFAA !important; color: #000000 !important; }
    .stFileUploader { background-color: #1E1E1E; border: 1px solid #3A3A3A; }
    h1, h2, h3 { color: #00FFAA !important; }
    </style>
    """, unsafe_allow_html=True)

def save_uploaded_file(uploaded_file):
    """Saves the uploaded PDF file to a storage directory."""
    file_path = f'document_store/pdfs/{uploaded_file.name}'
    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())
    return file_path

def load_pdf_documents(file_path):
    """Loads and extracts text from the uploaded PDF document."""
    document_loader = PDFPlumberLoader(file_path)
    return document_loader.load()

def chunk_documents(raw_documents):
    """Splits the extracted text into manageable chunks for processing."""
    text_processor = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
    return text_processor.split_documents(raw_documents)

def index_documents(document_chunks, vector_db):
    """Indexes the document chunks for efficient similarity search."""
    vector_db.add_documents(document_chunks)

def find_related_documents(query, vector_db):
    """Finds the most relevant document chunks based on semantic similarity."""
    return vector_db.similarity_search(query)

def generate_answer(user_query, context_documents, model):
    """Generates an AI-powered response based on relevant document context."""
    context_text = "\n\n".join([doc.page_content for doc in context_documents])
    conversation_prompt = ChatPromptTemplate.from_template(
        "You are an expert research assistant. Use the provided context to answer the query. "
        "If unsure, state that you don't know. Be concise and factual (max 3 sentences).\n\n"
        "Query: {user_query} \nContext: {document_context} \nAnswer:"
    )
    response_chain = conversation_prompt | model
    return response_chain.invoke({"user_query": user_query, "document_context": context_text})

def main():
    """Main function to run the Streamlit application."""
    st.title("📘 DocuMind AI")
    st.markdown("### Your Intelligent Document Assistant")
    st.markdown("---")
    
    # Apply custom UI styles
    apply_custom_styles()
    
    # Initialise AI components
    embedding_model = OllamaEmbeddings(model="deepseek-r1:1.5b")
    vector_db = InMemoryVectorStore(embedding_model)
    language_model = OllamaLLM(model="deepseek-r1:1.5b")
    
    # File Upload Section
    uploaded_pdf = st.file_uploader("Upload Research Document (PDF)", type="pdf", help="Select a PDF document for analysis")
    
    if uploaded_pdf:
        saved_path = save_uploaded_file(uploaded_pdf)
        raw_docs = load_pdf_documents(saved_path)
        processed_chunks = chunk_documents(raw_docs)
        index_documents(processed_chunks, vector_db)
        
        st.success("✅ Document processed successfully! Ask your questions below.")
        
        user_input = st.chat_input("Enter your question about the document...")
        
        if user_input:
            with st.chat_message("user"):
                st.write(user_input)
            
            with st.spinner("Analysing document..."):
                relevant_docs = find_related_documents(user_input, vector_db)
                ai_response = generate_answer(user_input, relevant_docs, language_model)
            
            with st.chat_message("assistant", avatar="🤖"):
                st.write(ai_response)

if __name__ == "__main__":
    main()
