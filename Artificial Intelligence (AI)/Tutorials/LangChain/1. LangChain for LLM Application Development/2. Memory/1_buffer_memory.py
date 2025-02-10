"""
This script demonstrates the use of LangChain's ConversationBufferMemory module.
It includes:
1. Setting up the OpenAI API using environment variables.
2. Dynamically selecting the appropriate GPT model based on the current date.
3. Initialsing LangChain's ConversationBufferMemory to retain conversational context.
4. Demonstrating how ConversationBufferMemory stores and retrieves chat history.

Author: [Roger J. Campbell]
Date: [2025-01-13]
"""

from helper_functions import setup_openai_api, determine_model
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import warnings


def main():
    """
    Main function demonstrating the use of ConversationBufferMemory for context persistence.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()

    # Step 3: Determine which model to use based on the current date
    llm_model = determine_model()

    # Step 4: Initialise the chat model with specified temperature
    llm = ChatOpenAI(temperature=0.0, model=llm_model)

    # Step 5: Initialise ConversationBufferMemory
    memory = ConversationBufferMemory()

    # Step 6: Create a ConversationChain with memory and verbosity
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )

    # Step 7: Interact with the ConversationChain
    print(conversation.predict(input="Hi, my name is Roger"))
    print(conversation.predict(input="What is 1+1?"))
    print(conversation.predict(input="What is my name?"))

    # Step 8: Display the buffer contents and memory variables
    print("\nConversation Buffer Contents:")
    print(memory.buffer)

    print("\nMemory Variables:")
    print(memory.load_memory_variables({}))

    # Step 9: Demonstrate manual saving of context
    memory = ConversationBufferMemory()
    memory.save_context({"input": "Hi"}, {"output": "What's up"})
    print("\nUpdated Conversation Buffer (after manual save):")
    print(memory.buffer)

    print("\nMemory Variables (after manual save):")
    print(memory.load_memory_variables({}))

    # Step 10: Add additional context manually
    memory.save_context({"input": "Not much, just hanging"}, {"output": "Cool"})
    print("\nMemory Variables (after adding more context):")
    print(memory.load_memory_variables({}))


if __name__ == "__main__":
    main()
