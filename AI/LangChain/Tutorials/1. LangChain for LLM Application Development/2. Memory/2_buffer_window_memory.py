"""
This script demonstrates the use of LangChain's ConversationBufferWindowMemory module.
It includes:
1. Setting up the OpenAI API using environment variables.
2. Dynamically selecting the appropriate GPT model based on the current date.
3. Initialising LangChain's ConversationBufferWindowMemory to store a sliding window of recent conversational context.
4. Demonstrating how ConversationBufferWindowMemory limits context retention to a specified number of exchanges.

Author: [Roger J. Campbell]
Date: [2025-01-13]
"""

from helper_functions import setup_openai_api, determine_model
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
import warnings


def main():
    """
    Main function demonstrating the use of ConversationBufferWindowMemory for limited context persistence.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()

    # Step 3: Determine which model to use based on the current date
    llm_model = determine_model()

    # Step 4: Initialise the chat model with specified temperature
    llm = ChatOpenAI(temperature=0.0, model=llm_model)

    # Step 5: Initialise ConversationBufferWindowMemory with a window size of 1
    memory = ConversationBufferWindowMemory(k=1)

    # Step 6: Demonstrate saving and loading memory manually
    memory.save_context({"input": "Hi"}, {"output": "What's up"})
    memory.save_context({"input": "Not much, just hanging"}, {"output": "Cool"})
    
    print("\nMemory Variables (after manual saves):")
    print(memory.load_memory_variables({}))

    # Step 7: Reset memory and demonstrate integration with ConversationChain
    memory = ConversationBufferWindowMemory(k=1)

    # Step 8: Create a ConversationChain with memory and verbosity disabled
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False
    )

    # Step 9: Interact with the ConversationChain
    print("\nConversation Outputs:")
    print(conversation.predict(input="Hi, my name is Roger"))
    print(conversation.predict(input="What is 1+1?"))
    print(conversation.predict(input="What is my name?"))


if __name__ == "__main__":
    main()
