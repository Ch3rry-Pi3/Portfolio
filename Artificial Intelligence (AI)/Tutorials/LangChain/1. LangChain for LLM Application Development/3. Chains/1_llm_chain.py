"""
This script demonstrates the use of LangChain's LLMChain module.
It includes:
1. Setting up the OpenAI API using environment variables.
2. Dynamically selecting the appropriate GPT model based on the current date.
3. Creating an LLMChain with a custom prompt template.
4. Demonstrating how to run the chain with input data.

Author: [Roger J. Campbell]
Date: [2025-01-14]
"""

import pandas as pd
from helper_functions import setup_openai_api, determine_model
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import warnings

def main():
    """
    Main function demonstrating the use of LLMChain for running custom prompts.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()

    # Step 3: Determine which model to use based on the current date
    llm_model = determine_model()

    # Step 4: Initialise the chat model with specified temperature
    llm = ChatOpenAI(temperature=0.9, model=llm_model)

    # Step 5: Load and preview the dataset
    df = pd.read_csv('Data.csv')
    print("Dataset Preview:")
    print(df.head())

    # Step 6: Create a prompt template
    prompt = ChatPromptTemplate.from_template(
        "What is the best name to describe a company that makes {product}?"
    )

    # Step 7: Initialise the LLMChain
    chain = LLMChain(llm=llm, prompt=prompt)

    # Step 8: Run the chain with an example input
    product = "Queen Size Sheet Set"
    result = chain.run(product)
    print(f"Suggested Company Name for '{product}': {result}")

if __name__ == "__main__":
    main()
