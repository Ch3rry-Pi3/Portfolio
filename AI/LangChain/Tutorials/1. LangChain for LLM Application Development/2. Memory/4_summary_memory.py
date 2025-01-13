"""
This script demonstrates the use of LangChain's ConversationSummaryBufferMemory module.
It includes:
1. Setting up the OpenAI API using environment variables.
2. Dynamically selecting the appropriate GPT model based on the current date.
3. Initialising LangChain's ConversationSummaryBufferMemory to retain a summarised context of the conversation.
4. Demonstrating how summarised memory can handle long conversational exchanges within token limits.

Author: [Roger J. Campbell]
Date: [2025-01-13]
"""

from helper_functions import setup_openai_api, determine_model
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
import warnings


def main():
    """
    Main function demonstrating the use of ConversationSummaryBufferMemory for summarised context persistence.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()

    # Step 3: Determine which model to use based on the current date
    llm_model = determine_model()

    # Step 4: Initialise the chat model with specified temperature
    llm = ChatOpenAI(temperature=0.0, model=llm_model)

    # Step 5: Create a long schedule string for demonstration
    schedule = (
        "There is a meeting at 8am with your product team. "
        "You will need your PowerPoint presentation prepared. "
        "9am-12pm have time to work on your LangChain project which will go quickly because LangChain is such a powerful tool. "
        "At Noon, lunch at the Italian restaurant with a customer who is driving over an hour away to meet you to understand the latest in AI. "
        "Be sure to bring your laptop to show the latest LLM demo."
    )

    # Step 6: Initialise ConversationSummaryBufferMemory with a token limit
    memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)

    # Step 7: Demonstrate saving context with summarised memory
    memory.save_context({"input": "Hello"}, {"output": "What's up"})
    memory.save_context({"input": "Not much, just hanging"}, {"output": "Cool"})
    memory.save_context({"input": "What is on the schedule today?"}, {"output": schedule})

    print("\nMemory Variables (after saving context):")
    print(memory.load_memory_variables({}))

    # Step 8: Integrate memory with a ConversationChain
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )

    # Step 9: Interact with the ConversationChain
    print("\nConversation Output:")
    print(conversation.predict(input="What would be a good demo to show?"))

    print("\nUpdated Memory Variables (after interaction):")
    print(memory.load_memory_variables({}))


if __name__ == "__main__":
    main()
