"""US Census AI Chatbot using Groq with Llama3

This project implements an interactive chatbot that uses Groq's Llama3 language model
to answer user queries based on US Census data stored in PDF files. 

Key Features:
- Document ingestion and preprocessing
- Embedding creation using OpenAI embeddings
- FAISS-based vector store for fast similarity searches
- Question answering powered by Groq's Llama3 model
- Interactive interface built with Streamlit

How it Works:
1. Load US Census data from PDFs.
2. Create embeddings for document chunks using OpenAI.
3. Store embeddings in a FAISS vector store for efficient retrieval.
4. Accept user queries, retrieve relevant document context, and generate responses.
"""

# ----------------------------
# Import Necessary Libraries
# ----------------------------
import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from dotenv import load_dotenv
import time

# ----------------------------
# Load Environment Variables
# ----------------------------
# Load API keys and other environment variables from .env file
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv('GROQ_API_KEY')

# ----------------------------
# Initialise Streamlit App
# ----------------------------
# Set the app title
st.title("US Census AI Chatbot Using Groq with Llama3")

# ----------------------------
# Initialise Language Model and Prompt Template
# ----------------------------
# Initialise the Groq Llama3 language model
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="Llama3-8b-8192"
)

# Define the prompt template for answering questions
prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question.
    <context>
    {context}
    Questions:{input}
    """
)

# ----------------------------
# Define Utility Functions
# ----------------------------
def vector_embedding():
    """
    Prepares document embeddings by:
    - Loading PDF files from a directory
    - Splitting the text into chunks
    - Generating vector embeddings using OpenAI embeddings
    - Storing the embeddings in a FAISS vector store
    """
    if "vectors" not in st.session_state:  # Check if embeddings are already prepared
        with st.spinner("Preparing embeddings..."):  # Display progress spinner
            try:
                # Initialise embeddings
                st.session_state.embeddings = OpenAIEmbeddings()

                # Load PDF files from the specified directory
                st.session_state.loader = PyPDFDirectoryLoader("./us_census")  
                st.session_state.docs = st.session_state.loader.load()  

                # Split the loaded documents into manageable text chunks
                st.session_state.text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000, 
                    chunk_overlap=200
                )
                st.session_state.final_documents = st.session_state.text_splitter.split_documents(
                    st.session_state.docs[:20]
                )  # Process the first 20 documents only

                # Create FAISS vector store from the processed chunks
                st.session_state.vectors = FAISS.from_documents(
                    st.session_state.final_documents, 
                    st.session_state.embeddings
                )

                # Indicate success
                st.success("Vector Store DB Is Ready!")
            except Exception as e:
                # Handle and display any errors during embedding preparation
                st.error(f"Error during vector embedding: {e}")

# ----------------------------
# Streamlit UI and Workflow
# ----------------------------

# Step 1: User inputs their question
prompt1 = st.text_input("Enter Your Question From Documents")

# Step 2: Button to trigger document embedding process
if st.button("Prepare Document Embeddings"):
    vector_embedding()

# Step 3: Retrieve and display results based on user question
if prompt1:
    # Ensure that embeddings are prepared
    if "vectors" not in st.session_state:
        st.error("Please prepare the document embeddings first by clicking the 'Prepare Document Embeddings' button.")
    else:
        with st.spinner("Retrieving answer..."):  # Display progress spinner
            try:
                # Create a document chain using the language model and prompt
                document_chain = create_stuff_documents_chain(llm, prompt)

                # Create a retriever object from the vector store
                retriever = st.session_state.vectors.as_retriever()

                # Combine the retriever and document chain into a retrieval chain
                retrieval_chain = create_retrieval_chain(retriever, document_chain)

                # Measure the response time
                start = time.process_time()
                response = retrieval_chain.invoke({'input': prompt1})
                response_time = time.process_time() - start
                print("Response time:", response_time)

                # Display the generated answer
                if response.get('answer'):
                    st.write(response['answer'])
                else:
                    st.write("No answer could be generated. Please refine your question.")

                # Display document similarity search in an expander
                with st.expander("Document Similarity Search"):
                    # Display relevant document chunks
                    if "context" in response:
                        for i, doc in enumerate(response["context"][:5]):  # Limit to top 5 chunks
                            st.write(doc.page_content)  # Display chunk content
                            st.write("--------------------------------")  # Separator between chunks
                    else:
                        st.write("No relevant context found.")
            except Exception as e:
                # Handle and display any errors during the retrieval process
                st.error(f"Error during retrieval: {e}")
