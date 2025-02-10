"""
Thai Recipe Assistant

This script implements a Retrieval-Augmented Generation (RAG) application that leverages
a Postgres vector database to retrieve and generate responses about Thai recipes. 

Key Features:
1. Uses a PDF knowledge base loaded from a URL to populate a Postgres vector database.
2. Employs an AI assistant powered by the Groq model for intelligent query answering.
3. Supports chat history, knowledge base search, and tool call visibility.

The application is designed to demonstrate how AI can interact with a vector database for knowledge retrieval,
making it particularly suitable for recipe discovery or culinary learning.

Requirements:
- Dockerized Postgres vector database
- GROQ and OpenAI API keys
- The `phi` framework for knowledge bases, assistants, and vector databases.

Author: Your Name
"""

# ==========================
# 1. Import Libraries
# ==========================
import os
from dotenv import load_dotenv
from typing import Optional, List
import typer

from phi.assistant import Assistant  # Autonomous assistant AI
from phi.storage.assistant.postgres import PgAssistantStorage  # Storage for assistant runs
from phi.knowledge.pdf import PDFUrlKnowledgeBase  # PDF reader for knowledge base
from phi.vectordb.pgvector import PgVector2  # Vector database for knowledge retrieval
from phi.llm.groq import Groq  # Groq AI large language model

# ==========================
# 2. Load Environment Variables
# ==========================
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Database connection URL for the Postgres vector database
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

# ==========================
# 3. Configure Knowledge Base
# ==========================
# Load Thai Recipes PDF into the Postgres vector database
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector2(
        collection="recipes",  # Collection name in the vector database
        db_url=db_url
    )
)
knowledge_base.load()

# ==========================
# 4. Configure Assistant Storage
# ==========================
storage = PgAssistantStorage(
    table_name="pdf_assistant",  # Table to store assistant runs
    db_url=db_url
)

# ==========================
# 5. Define PDF Assistant
# ==========================
def pdf_assistant(new: bool = False, user: str = "user"):
    """
    Run the Thai Recipe Assistant.

    Args:
        new (bool): Whether to start a new session. Defaults to False.
        user (str): User identifier. Defaults to "user".
    """
    run_id: Optional[str] = None

    # Check for existing runs if not starting a new session
    if not new:
        existing_run_ids: List[str] = storage.get_all_run_ids(user)
        if len(existing_run_ids) > 0:
            run_id = existing_run_ids[0]

    # Initialise the assistant
    assistant = Assistant(
        run_id=run_id,
        user_id=user,
        knowledge_base=knowledge_base,
        storage=storage,
        show_tool_calls=True,  # Display tool calls in the response
        search_knowledge=True,  # Enable knowledge base search
        read_chat_history=True,  # Enable reading chat history
        llm=Groq(
            model="llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY")
        )
    )

    # Display whether the session is new or continuing
    if run_id is None:
        run_id = assistant.run_id
        print(f"Started New Run: {run_id}\n")
    else:
        print(f"Continuing Existing Run: {run_id}\n")

    # Run the assistant's command-line interface with Markdown support
    assistant.cli_app(markdown=True)

# ==========================
# 6. Entry Point
# ==========================
if __name__ == "__main__":
    typer.run(pdf_assistant)
