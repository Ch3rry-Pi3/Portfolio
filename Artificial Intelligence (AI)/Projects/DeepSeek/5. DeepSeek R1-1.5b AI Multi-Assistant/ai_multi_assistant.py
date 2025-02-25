"""
AI Multi-Assistant

This Streamlit-based application provides an AI-powered multi-functional assistant
that supports code generation, code review, language tutoring, and document generation
using the DeepSeek R1 model running locally via Ollama.

Features:
- Code Assistant:
  - Generate Python code based on user descriptions.
  - Explain existing code in a structured manner.
  - Perform a code review, identifying optimizations and best practices.
- Language Tutor:
  - Perform grammar checks and suggest improvements.
  - Enhance vocabulary by suggesting alternative words and phrases.
- Document Generator:
  - Generate structured business proposals.
  - Draft professional emails with clarity and etiquette.

Dependencies:
- streamlit
- openai

Usage:
Run the script with `streamlit run ai_multi_assistant.py` to launch the application.
"""

import streamlit as st
from openai import OpenAI


class MultiAssistant:
    """
    AI-powered multi-functional assistant supporting various utilities such as code assistance,
    language tutoring, and document generation.
    """
    
    def __init__(self):
        """Initialize the AI model with local API credentials."""
        self.client = OpenAI(
            api_key="ollama",
            base_url="http://localhost:11434/v1/",
        )
        self.model = "deepseek-r1:1.5b"

    def process_request(self, system_prompt: str, user_prompt: str) -> str:
        """Processes a user request based on the selected tool (code, language, document generation)."""
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
    """Defines system prompts for different tools in the assistant."""
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
Analyze the code and explain:
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
2. Performance optimization opportunities
3. Security vulnerabilities
4. Code style and PEP 8 compliance
5. Error handling improvements
6. Documentation completeness
7. Code modularity and reusability
8. Memory efficiency""",

        "Grammar Check": """You are an expert English language teacher.
Review the text for:
1. Grammar errors
2. Punctuation mistakes
3. Sentence structure
4. Word choice improvements
5. Style consistency
Provide clear explanations and corrections.""",

        "Vocabulary Enhancement": """You are a vocabulary expert.
Analyze the text and:
1. Suggest more sophisticated alternatives
2. Explain idioms and phrases
3. Provide context for word usage
4. Suggest synonyms and antonyms
5. Explain connotations""",

        "Business Proposal": """You are a professional business writer.
Generate a proposal that includes:
1. Executive summary
2. Problem statement
3. Proposed solution
4. Timeline and milestones
5. Budget breakdown
6. Risk assessment
7. Expected outcomes""",

        "Professional Email": """You are an expert in business communication.
Create an email that:
1. Has a clear subject line
2. Maintains professional tone
3. Is concise and focused
4. Includes call to action
5. Has appropriate closing
6. Follows email etiquette""",
    }


def main():
    """Main function to launch the Streamlit app."""
    
    # Step 1: Configure Streamlit UI
    st.set_page_config(page_title="AI Multi-Assistant", page_icon="🤖", layout="wide")
    st.title("🤖 AI Multi-Assistant")

    # Step 2: Sidebar settings
    tool_categories = {
        "Code Assistant": ["Code Generation", "Code Explanation", "Code Review"],
        "Language Tutor": ["Grammar Check", "Vocabulary Enhancement"],
        "Document Generator": ["Business Proposal", "Professional Email"],
    }
    
    category = st.sidebar.selectbox("Select Category", list(tool_categories.keys()))
    mode = st.sidebar.selectbox("Select Tool", tool_categories[category])
    
    system_prompts = get_system_prompts()
    
    # Step 3: Display tool description
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Current Tool**: {mode}")
    st.sidebar.markdown("**Tool Description:**")
    st.sidebar.markdown(system_prompts[mode].replace("\n", "\n\n"))
    
    # Step 4: Input and output layout
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.markdown(f"### Input for {mode}")
        user_prompt = st.text_area("Enter your prompt:", height=300)
        process_button = st.button("🚀 Process", type="primary", use_container_width=True)
    
    with col2:
        st.markdown("### Output")
        output_container = st.container()
    
    # Step 5: Process user input
    if process_button:
        if user_prompt:
            with st.spinner("Processing..."):
                with output_container:
                    assistant = MultiAssistant()
                    assistant.process_request(system_prompts[mode], user_prompt)
        else:
            st.warning("⚠️ Please enter some input!")

    # Step 6: Footer
    st.markdown("---")
    st.markdown("<div style='text-align: center'><p>Made with ❤️ using DeepSeek R1 and Ollama</p></div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()