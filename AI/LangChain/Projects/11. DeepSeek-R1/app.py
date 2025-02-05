"""
DeepSeek Code Companion

This is a Streamlit-based AI-powered coding assistant built using LangChain and Ollama. 
The assistant helps with:
    - Python coding queries
    - Debugging support
    - Code documentation
    - Solution design

It uses a conversational interface where users can interact with an AI model to receive coding assistance.

Technologies used:
    - Streamlit for UI
    - LangChain for prompt management
    - Ollama for AI-powered responses
"""

import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

def apply_custom_styles():
    """Applies custom CSS styles to enhance the UI."""
    st.markdown("""
    <style>
        .main {
            background-color: #1a1a1a;
            color: #ffffff;
        }
        .sidebar .sidebar-content {
            background-color: #2d2d2d;
        }
        .stTextInput textarea {
            color: #ffffff !important;
        }
        .stSelectbox div[data-baseweb="select"] {
            color: white !important;
            background-color: #3d3d3d !important;
        }
        .stSelectbox svg {
            fill: white !important;
        }
        .stSelectbox option {
            background-color: #2d2d2d !important;
            color: white !important;
        }
        div[role="listbox"] div {
            background-color: #2d2d2d !important;
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)

def setup_sidebar():
    """Configures the sidebar with model selection and feature details."""
    with st.sidebar:
        st.header("⚙️ Configuration")
        selected_model = st.selectbox("Choose Model", ["deepseek-r1:1.5b", "deepseek-r1:3b"], index=0)
        st.divider()
        st.markdown("### Model Capabilities")
        st.markdown("""
        - 🐍 Python Expert
        - 🐞 Debugging Assistant
        - 📝 Code Documentation
        - 💡 Solution Design
        """)
        st.divider()
        st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")
    return selected_model

def initialise_chat_engine(model):
    """Initialises the chat model with the selected configuration."""
    return ChatOllama(model=model, base_url="http://localhost:11434", temperature=0.3)

def build_prompt_chain():
    """Constructs the chat prompt chain from user and AI messages."""
    prompt_sequence = [
        SystemMessagePromptTemplate.from_template(
            "You are an expert AI coding assistant. Provide concise, correct solutions "
            "with strategic print statements for debugging. Always respond in English."
        )
    ]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)

def generate_ai_response(prompt_chain, llm_engine):
    """Processes the chat input and generates an AI response."""
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})

def display_chat_messages():
    """Displays chat messages from the session state."""
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.message_log:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

def main():
    """Main function to run the Streamlit application."""
    st.title("🧠 DeepSeek Code Companion")
    st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers")
    
    # Apply custom styles
    apply_custom_styles()
    
    # Sidebar setup
    selected_model = setup_sidebar()
    
    # Initialise chat engine
    llm_engine = initialise_chat_engine(selected_model)
    
    # Initialise session state for message log
    if "message_log" not in st.session_state:
        st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]
    
    # Display chat messages
    display_chat_messages()
    
    # Capture user input
    user_query = st.chat_input("Type your coding question here...")
    
    if user_query:
        # Add user query to message log
        st.session_state.message_log.append({"role": "user", "content": user_query})
        
        # Generate AI response
        with st.spinner("🧠 Processing..."):
            prompt_chain = build_prompt_chain()
            ai_response = generate_ai_response(prompt_chain, llm_engine)
        
        # Add AI response to message log
        st.session_state.message_log.append({"role": "ai", "content": ai_response})
        
        # Rerun Streamlit app to update the chat display
        st.rerun()

if __name__ == "__main__":
    main()
