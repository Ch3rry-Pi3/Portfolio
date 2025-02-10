"""
Multimodal AI Video Summariser

This script implements a Streamlit-based web application that utilises 
a multimodal AI agent powered by Gemini 2.0 and Google Generative AI.
The application allows users to upload video files, ask questions about 
the video content, and receive detailed, actionable insights generated 
by the AI agent.

Key Features:
1. Accepts video uploads in common formats (MP4, MOV, AVI) for analysis.
2. Employs a Gemini 2.0 AI model and DuckDuckGo for web research.
3. Provides a user-friendly interface for querying video content.

Requirements:
- Google Generative AI API key
- The `phi` framework for agent and tool integration

Author: Your Name
"""

# ==========================
# 1. Import Libraries
# ==========================
import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai

import time
import tempfile
from pathlib import Path
from dotenv import load_dotenv
import os

# ==========================
# 2. Load Environment Variables
# ==========================
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

# ==========================
# 3. Streamlit Configuration
# ==========================
st.set_page_config(
    page_title="Multimodal AI Agent - Video Summariser",
    page_icon="🎥",
    layout="wide"
)

# ==========================
# 4. Agent Initialisation
# ==========================
@st.cache_resource
def initialize_agent():
    """
    Initialises the multimodal AI agent with the Gemini model
    and DuckDuckGo as a web research tool.

    Returns:
        Agent: Configured AI agent.
    """
    return Agent(
        name="Video AI Summariser",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True
    )

# ==========================
# 5. Main Function
# ==========================
def main():
    """
    Main function to run the Streamlit application.
    """
    # Display application title and header
    st.title("Phidata Video AI Summariser Agent 🎥🎤🖬")
    st.header("Powered by Gemini 2.0 Flash Exp")

    # Initialise the multimodal AI agent
    multimodal_agent = initialize_agent()

    # File uploader for video files
    video_file = st.file_uploader(
        "Upload a video file", type=['mp4', 'mov', 'avi'],
        help="Upload a video for AI analysis."
    )

    if video_file:
        # Save uploaded video temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
            temp_video.write(video_file.read())
            video_path = temp_video.name

        # Display the uploaded video
        st.video(video_path, format="video/mp4", start_time=0)

        # Text area for user queries
        user_query = st.text_area(
            "What insights are you seeking from the video?",
            placeholder="Ask anything about the video content. The AI agent will analyse and gather additional context if needed.",
            help="Provide specific questions or insights you want from the video."
        )

        # Analyse video on button click
        if st.button("🔍 Analyse Video", key="analyze_video_button"):
            if not user_query:
                st.warning("Please enter a question or insight to analyse the video.")
            else:
                try:
                    with st.spinner("Processing video and gathering insights..."):
                        # Upload and process video file
                        processed_video = upload_file(video_path)
                        while processed_video.state.name == "PROCESSING":
                            time.sleep(1)
                            processed_video = get_file(processed_video.name)

                        # Construct analysis prompt
                        analysis_prompt = (
                            f"""
                            Analyse the uploaded video for content and context.
                            Respond to the following query using video insights and supplementary web research:
                            {user_query}

                            Provide a detailed, user-friendly, and actionable response.
                            """
                        )

                        # Get response from the AI agent
                        response = multimodal_agent.run(analysis_prompt, videos=[processed_video])

                    # Display the result
                    st.subheader("Analysis Result")
                    st.markdown(response.content)

                except Exception as error:
                    st.error(f"An error occurred during analysis: {error}")
                finally:
                    # Clean up temporary video file
                    Path(video_path).unlink(missing_ok=True)
    else:
        st.info("Upload a video file to begin analysis.")

    # Custom CSS for text area height
    st.markdown(
        """
        <style>
        .stTextArea textarea {
            height: 100px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# ==========================
# 6. Entry Point
# ==========================
if __name__ == "__main__":
    main()
