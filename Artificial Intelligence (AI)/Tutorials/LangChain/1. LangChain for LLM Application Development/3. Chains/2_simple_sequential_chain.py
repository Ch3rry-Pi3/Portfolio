"""
This script demonstrates the use of LangChain's SimpleSequentialChain module.
It includes:
1. Setting up the OpenAI API using environment variables.
2. Dynamically selecting the appropriate GPT model based on the current date.
3. Creating a SimpleSequentialChain with two LLMChains.
4. Demonstrating the chain's functionality by processing a product input.

Author: [Roger J. Campbell]
Date: [2025-01-14]
"""

import pandas as pd
from helper_functions import setup_openai_api, determine_model
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
import warnings

def main():
    """
    Main function demonstrating the use of SimpleSequentialChain for sequential prompt processing.
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

    # Step 6: Define the first prompt template
    first_prompt = ChatPromptTemplate.from_template(
        "What is the best name to describe a company that makes {product}?"
    )

    # Step 7: Create the first LLMChain
    chain_one = LLMChain(llm=llm, prompt=first_prompt)

    # Step 8: Define the second prompt template
    second_prompt = ChatPromptTemplate.from_template(
        "Write a 20-word description for the following company: {company_name}"
    )

    # Step 9: Create the second LLMChain
    chain_two = LLMChain(llm=llm, prompt=second_prompt)

    # Step 10: Combine the chains into a SimpleSequentialChain
    overall_simple_chain = SimpleSequentialChain(chains=[chain_one, chain_two], verbose=True)

    # Step 11: Run the SimpleSequentialChain with an example input
    product = "Queen Size Sheet Set"
    result = overall_simple_chain.run(product)
    print(f"Output of the SimpleSequentialChain for '{product}': {result}")

if __name__ == "__main__":
    main()
