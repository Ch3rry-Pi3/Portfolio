"""LangChain and FastAPI Integration

This script creates a FastAPI server that integrates LangChain with OpenAI's GPT models and the LLAMA2 model 
via Ollama to handle dynamic requests for generating essays and poems.

The server demonstrates:
- Handling multiple routes for different tasks.
- Using LangChain's prompt templates and models (OpenAI and LLAMA2) to build an API-based application.

Parameters:
-----------
os : module
    Used to set environment variables for OpenAI and LangChain API keys.
load_dotenv : function
    Loads environment variables from the `.env` file.

FastAPI : class
    Framework used to create a RESTful API.
ChatOpenAI : class
    LangChain class for interacting with OpenAI's GPT models.
Ollama : class
    LangChain class for interacting with the LLAMA2 model via Ollama.
ChatPromptTemplate : class
    LangChain class for defining templates to generate prompts.

add_routes : function
    LangServe function for adding routes to the FastAPI app.

Returns:
--------
FastAPI Application:
    - Provides endpoints for generating essays and poems.
    - Integrates LangChain's OpenAI and LLAMA2 models.

Launch Instructions:
--------------------
1. Ensure the `.env` file is set up with:
    - OPENAI_API_KEY
    - LANGCHAIN_API_KEY

2. Run the FastAPI server:
    ```
    python app.py
    ```

3. Verify the server is running by navigating to:
    - `http://localhost:8000/docs` (Swagger API docs)
    - `http://localhost:8000/essay/invoke` (for essay endpoint)
    - `http://localhost:8000/poem/invoke` (for poem endpoint)
"""

# Import FastAPI framework for building the API
from fastapi import FastAPI

# Import LangChain components for creating prompts and interacting with OpenAI/LLMs
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import Ollama

# Import LangServe for adding routes to the FastAPI server
from langserve import add_routes

# Import Uvicorn for running the FastAPI app
import uvicorn

# Import libraries for environment variable management
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Debugging: Print loaded environment variables (Optional)
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("LANGCHAIN_API_KEY:", os.getenv("LANGCHAIN_API_KEY"))

# Initialise FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server for generating essays and poems using OpenAI and LLAMA2."
)

# Add a route for OpenAI's GPT models
add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

# Initialise LangChain models
model = ChatOpenAI()
llm = Ollama(model="llama2")

# Define prompts for essay and poem generation
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with approximately 100 words.")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} with approximately 100 words.")

# Add routes for essay and poem generation
add_routes(
    app,
    prompt1 | model,
    path="/essay"
)

add_routes(
    app,
    prompt2 | llm,
    path="/poem"
)

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
