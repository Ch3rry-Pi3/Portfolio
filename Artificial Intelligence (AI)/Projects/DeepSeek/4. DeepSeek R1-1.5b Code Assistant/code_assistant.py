"""
Local Code Assistant

This Streamlit-based application provides AI-powered assistance for code generation, explanation,
and review using the DeepSeek R1 model running locally via Ollama.

Features:
- Generate Python code based on user descriptions.
- Explain existing code in a structured manner.
- Perform a code review, identifying optimisations and best practices.
- Provides an interactive UI for user input and AI responses.

Dependencies:
- streamlit
- openai

Usage:
Run the script with `streamlit run code_assistant.py` to launch the application.
"""

import streamlit as st
from openai import OpenAI


class LocalCodeAssistant:
    """
    AI-powered code assistant for generating, explaining, and reviewing Python code.
    """
    
    def __init__(self):
        """Initialise the AI model with local API credentials."""
        self.client = OpenAI(
            api_key="ollama",
            base_url="http://localhost:11434/v1/",
        )
        self.model = "deepseek-r1:1.5b"

    def process_request(self, system_prompt: str, user_prompt: str) -> str:
        """Processes a user request based on the selected mode (generation, explanation, review)."""
        try:
            # Step 1: Send request to the AI model
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                stream=True,
            )
            
            result = st.empty()
            collected_chunks = []
            
            # Step 2: Stream and display AI response
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    collected_chunks.append(chunk.choices[0].delta.content)
                    result.markdown("".join(collected_chunks))
            
            return "".join(collected_chunks)
        except Exception as e:
            return f"Error: {str(e)}"


def get_system_prompts():
    """Defines system prompts for different modes of code assistance."""
    return {
        "Code Generation": """You are an expert Python programmer who writes clean, efficient, and well-documented code.
Follow these guidelines:
1. Start with a brief comment explaining the code's purpose
2. Include docstrings for functions
3. Use clear variable names
4. Add inline comments for complex logic
5. Follow PEP 8 style guidelines
6. Include example usage
7. Handle common edge cases""",

        "Code Explanation": """You are a patient and knowledgeable coding tutor.
Analyse the code and explain:
1. Overall purpose and functionality
2. Breakdown of each major component
3. Key programming concepts used
4. Flow of execution
5. Important variables and functions
6. Any clever techniques or patterns
7. Potential learning points for students""",

        "Code Review": """You are a senior code reviewer with expertise in Python best practices.
Review the code for:
1. Logical errors or bugs
2. Performance optimisation opportunities
3. Security vulnerabilities
4. Code style and PEP 8 compliance
5. Error handling improvements
6. Documentation completeness
7. Code modularity and reusability
8. Memory efficiency
Provide specific suggestions for improvements.""",
    }


def get_example_prompts():
    """Provides example prompts for different modes."""
    return {
        "Code Generation": {
            "placeholder": """Examples:
1. "Create a Wordle game clone with a simple CLI interface"
2. "Build a PDF merger tool with a progress bar"
3. "Develop a simple REST API for a todo list using FastAPI"
4. "Create a data visualisation dashboard using matplotlib"
5. "Build a file encryption tool using Fernet"

Your request:""",
            "default": "Create a tic-tac-toe game with a simple GUI using tkinter",
        },
        "Code Explanation": {
            "placeholder": "Paste your code here for explanation.",
            "default": "",
        },
        "Code Review": {
            "placeholder": "Paste your code here for review.",
            "default": "",
        },
    }


def main():
    """Main function to launch the Streamlit app."""
    
    # Step 1: Configure Streamlit UI
    st.set_page_config(
        page_title="DeepSeek R1 Code Assistant", page_icon="🤖", layout="wide"
    )
    st.title("🤖 Local DeepSeek R1 Code Assistant")
    st.markdown("Using DeepSeek R1 1.5B model running locally through Ollama")

    system_prompts = get_system_prompts()
    example_prompts = get_example_prompts()

    # Step 2: Sidebar settings
    st.sidebar.title("Settings")
    mode = st.sidebar.selectbox(
        "Choose Mode", ["Code Generation", "Code Explanation", "Code Review"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Current Mode**: {mode}")
    st.sidebar.markdown("**Mode Description:**")
    st.sidebar.markdown(system_prompts[mode].replace("\n", "\n\n"))

    # Step 3: Input and output layout
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.markdown(f"### Input for {mode}")
        user_prompt = st.text_area(
            "Enter your prompt or code:",
            height=300,
            placeholder=example_prompts[mode]["placeholder"],
            value=example_prompts[mode]["default"],
        )
        process_button = st.button("🚀 Process", type="primary", use_container_width=True)
    
    with col2:
        st.markdown("### Output")
        output_container = st.container()

    # Step 4: Process user input
    if process_button:
        if user_prompt:
            with st.spinner("Processing..."):
                with output_container:
                    assistant = LocalCodeAssistant()
                    assistant.process_request(system_prompts[mode], user_prompt)
        else:
            st.warning("⚠️ Please enter some input!")
    
    # Step 5: Footer
    st.markdown("---")
    st.markdown("<div style='text-align: center'><p>Made with ❤️ using DeepSeek R1 and Ollama</p></div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
