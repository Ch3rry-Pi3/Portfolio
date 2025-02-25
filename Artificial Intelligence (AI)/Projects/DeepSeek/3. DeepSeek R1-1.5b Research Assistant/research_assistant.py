"""
Research Assistant

This program provides a Streamlit-based interface for analysing research documents.
It allows users to upload PDF, DOCX, and TXT files, extracts their text content, and 
processes queries using an AI model. The AI model provides analysis, including direct 
answers, supporting evidence, key findings, and limitations.

Features:
- Extract text from PDF, DOCX, and TXT files.
- Process and analyse content based on user queries.
- Present results in an interactive format with Streamlit.
- Support multi-document comparison for cross-analysis.

Dependencies:
- streamlit
- openai
- PyPDF2
- docx

Usage:
Run the script with `streamlit run research_assistant.py` to launch the app.
"""

import streamlit as st
from openai import OpenAI
import PyPDF2
import docx


class ResearchAssistant:
    """
    A research assistant that extracts text from uploaded documents and processes user queries 
    using an AI model.
    """
    
    def __init__(self):
        """Initialise the AI model with API credentials."""
        self.client = OpenAI(
            api_key="ollama",
            base_url="http://localhost:11434/v1/",
        )
        self.model = "deepseek-r1:1.5b"

    def extract_text(self, uploaded_file):
        """Extract text from uploaded files, supporting PDF, DOCX, and TXT formats."""
        text = ""
        
        # Step 1: Check file type
        if uploaded_file.type == "application/pdf":
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            
            # Step 2: Read text from each page
            for page in pdf_reader.pages:
                text += page.extract_text()
        
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = docx.Document(uploaded_file)
            
            # Step 3: Read text from each paragraph
            for para in doc.paragraphs:
                text += para.text + "\n"
        
        else:
            # Step 4: Read text from a plain text file
            text = str(uploaded_file.read(), "utf-8")
        
        return text

    def analyse_content(self, text, query):
        """Analyse extracted text based on the user query and return structured insights."""
        
        # Step 1: Construct the prompt
        prompt = f"""Analyse this text and answer the following query:
            Text: {text[:2000]}...
            Query: {query}
            
            Provide:
            1. Direct answer to the query
            2. Supporting evidence
            3. Key findings
            4. Limitations of the analysis
        """

        try:
            # Step 2: Send request to the AI model
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a research assistant skilled in analysing academic and technical documents."},
                    {"role": "user", "content": prompt},
                ],
                stream=True,
            )

            result = st.empty()
            collected_chunks = []
            
            # Step 3: Stream and display AI response
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    collected_chunks.append(chunk.choices[0].delta.content)
                    result.markdown("".join(collected_chunks))

            return "".join(collected_chunks)
        
        except Exception as e:
            return f"Error: {str(e)}"


def main():
    """Main function to launch the Streamlit app."""
    
    # Step 1: Configure Streamlit UI
    st.set_page_config(page_title="Research Assistant", layout="wide")
    st.title("📚 Research Document Analyser")
    
    assistant = ResearchAssistant()
    
    # Step 2: Sidebar for document upload
    with st.sidebar:
        st.header("Upload Documents")
        uploaded_files = st.file_uploader(
            "Upload research documents",
            type=["pdf", "docx", "txt"],
            accept_multiple_files=True,
        )
    
    # Step 3: Handle uploaded files
    if uploaded_files:
        st.write(f"📎 {len(uploaded_files)} documents uploaded")
        
        # Step 4: Get user query
        query = st.text_area(
            "What would you like to know about these documents?",
            placeholder="Example: What are the main findings regarding climate change impact?",
            height=100,
        )
        
        if st.button("Analyse", type="primary"):
            with st.spinner("Analysing documents..."):
                # Step 5: Process each document
                for file in uploaded_files:
                    st.write(f"### Analysis of {file.name}")
                    text = assistant.extract_text(file)
                    
                    # Step 6: Create tabs for different analyses
                    tab1, tab2, tab3 = st.tabs(["Main Analysis", "Key Points", "Summary"])
                    
                    with tab1:
                        assistant.analyse_content(text, query)
                    
                    with tab2:
                        assistant.analyse_content(text, "Extract key points and findings")
                    
                    with tab3:
                        assistant.analyse_content(text, "Provide a brief summary")
                
                # Step 7: Compare documents if multiple uploaded
                if len(uploaded_files) > 1:
                    st.write("### Cross-Document Analysis")
                    st.write("Comparing findings across documents...")
                    # Add comparison logic here


if __name__ == "__main__":
    main()
