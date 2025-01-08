"""
PhiData Playground Application for Web Search and Financial Analysis

This script creates a PhiData Playground, which serves as a user interface for interacting with agents.
It includes:
1. A Web Search Agent: Performs web searches using DuckDuckGo.
2. A Finance AI Agent: Retrieves financial data like stock prices, analyst recommendations, and company news using YFinanceTools.

The app is built and served locally via the `phi.playground` module.

Steps:
1. Import necessary libraries and set up the environment.
2. Define the Web Search Agent.
3. Define the Finance AI Agent.
4. Configure the PhiData Playground.
5. Serve the Playground application.
"""

# ==========================
# 1. Import Libraries and Set Up Environment
# ==========================
import os
from dotenv import load_dotenv
import phi
import phi.api
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app

# Load environment variables
load_dotenv()

# Set the Phi API key
phi.api = os.getenv("PHI_API_KEY")

# ==========================
# 2. Define Web Search Agent
# ==========================
def create_web_search_agent():
    """
    Creates and configures the Web Search Agent.
    """
    return Agent(
        name="Web Search Agent",
        role="Search the web for information",
        model=Groq(id="llama-3.1-70b-versatile"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tools_calls=True,
        markdown=True,
    )

# ==========================
# 3. Define Finance AI Agent
# ==========================
def create_finance_agent():
    """
    Creates and configures the Finance AI Agent.
    """
    return Agent(
        name="Finance AI Agent",
        model=Groq(id="llama-3.1-70b-versatile"),
        tools=[
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                stock_fundamentals=True,
                company_news=True,
            )
        ],
        instructions=["Use tables to display the data"],
        show_tools_calls=True,
        markdown=True,
    )

# ==========================
# 4. Configure PhiData Playground
# ==========================
def create_playground():
    """
    Configures the PhiData Playground with the defined agents.
    """
    # Create agents
    web_search_agent = create_web_search_agent()
    finance_agent = create_finance_agent()

    # Create the Playground app
    return Playground(agents=[finance_agent, web_search_agent]).get_app()

# ==========================
# 5. Main Function
# ==========================
def main():
    """
    Main function to serve the PhiData Playground application.
    """
    print("Starting PhiData Playground...")
    app = create_playground()
    serve_playground_app("playground:app", reload=True)

# ==========================
# 6. Entry Point
# ==========================
if __name__ == "__main__":
    main()
