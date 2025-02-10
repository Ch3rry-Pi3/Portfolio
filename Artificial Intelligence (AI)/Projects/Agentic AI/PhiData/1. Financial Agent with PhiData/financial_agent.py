"""
Multi-Agent Application for Web Search and Financial Analysis

This script demonstrates the use of the `phi` framework to build a multi-agent system.
The app consists of two agents:
1. **Web Search Agent**: Uses DuckDuckGo to search the web for information.
2. **Finance AI Agent**: Retrieves financial data (e.g., stock prices, analyst recommendations) using YFinanceTools.

Agents collaborate to fulfill user queries. The multi-agent system processes tasks dynamically 
and provides formatted responses in Markdown.

Steps:
1. Import necessary libraries and set up environment.
2. Define the Web Search Agent.
3. Define the Finance AI Agent.
4. Combine the agents into a multi-agent system.
5. Execute a query to retrieve and display information about a stock (e.g., NVDA).
"""

# ==========================
# 1. Import Libraries and Set Up Environment
# ==========================
import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

# Load environment variables
load_dotenv()

# ==========================
# 2. Define Web Search Agent
# ==========================
def create_web_search_agent():
    """
    Creates and configures the Web Search Agent.
    """
    return Agent(
        name="Web Search Agent",
        role="Search the web for the information",
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
        show_tool_calls=True,
        markdown=True,
    )

# ==========================
# 4. Define Multi-Agent System
# ==========================
def create_multi_agent_system(web_search_agent, finance_agent):
    """
    Combines the Web Search Agent and Finance AI Agent into a multi-agent system.
    """
    return Agent(
        team=[web_search_agent, finance_agent],
        model=Groq(id="llama-3.1-70b-versatile"),
        instructions=[
            "Always include sources",
            "Use tables to display the data",
        ],
        show_tool_calls=True,
        markdown=True,
    )

# ==========================
# 5. Main Function
# ==========================
def main():
    """
    Main function to demonstrate the multi-agent system.
    """
    # Step 1: Create individual agents
    web_search_agent = create_web_search_agent()
    finance_agent = create_finance_agent()

    # Step 2: Combine agents into a multi-agent system
    multi_ai_agent = create_multi_agent_system(web_search_agent, finance_agent)

    # Step 3: Execute a query using the multi-agent system
    print("Executing query...")
    multi_ai_agent.print_response(
        "Summarize analyst recommendation and share the latest news for NVDA",
        stream=True,
    )

# ==========================
# 6. Entry Point
# ==========================
if __name__ == "__main__":
    main()