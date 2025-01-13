"""
This script demonstrates the use of LangChain's ConversationTokenBufferMemory module.
It includes:
1. Setting up the OpenAI API using environment variables.
2. Dynamically selecting the appropriate GPT model based on the current date.
3. Initialising LangChain's ConversationTokenBufferMemory to store conversational context limited by token count.
4. Demonstrating how ConversationTokenBufferMemory adjusts context retention based on a token limit.

Author: [Roger J. Campbell]
Date: [2025-01-13]
"""

from helper_functions import setup_openai_api, determine_model
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationTokenBufferMemory
import warnings


def main():
    """
    Main function demonstrating the use of ConversationTokenBufferMemory for token-limited context persistence.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()

    # Step 3: Determine which model to use based on the current date
    llm_model = determine_model()

    # Step 4: Initialise the chat model with specified temperature
    llm = ChatOpenAI(temperature=0.0, model=llm_model)

    # Step 5: Initialise ConversationTokenBufferMemory with a small token limit
    memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=10)

    # Step 6: Demonstrate saving context with a small token limit
    memory.save_context({"input": "AI is what?!"}, {"output": "Amazing!"})
    memory.save_context({"input": "Backpropagation is what?"}, {"output": "Beautiful!"})
    memory.save_context({"input": "Chatbots are what?"}, {"output": "Charming!"})

    print("\nMemory Variables with max_token_limit=10:")
    print(memory.load_memory_variables({}))

    # Step 7: Initialise ConversationTokenBufferMemory with a larger token limit
    memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=50)

    # Step 8: Demonstrate saving context with a larger token limit
    memory.save_context({"input": "AI is what?!"}, {"output": "Amazing!"})
    memory.save_context({"input": "Backpropagation is what?"}, {"output": "Beautiful!"})
    memory.save_context({"input": "Chatbots are what?"}, {"output": "Charming!"})

    print("\nMemory Variables with max_token_limit=50:")
    print(memory.load_memory_variables({}))


if __name__ == "__main__":
    main()
