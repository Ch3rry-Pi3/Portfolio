"""
This script demonstrates the use of LangChain's SequentialChain module.
It includes:
1. Setting up the OpenAI API using environment variables.
2. Dynamically selecting the appropriate GPT model based on the current date.
3. Creating a SequentialChain with multiple LLMChains for a multi-step process.
4. Demonstrating the chain's functionality by processing a product review.

Author: [Roger J. Campbell]
Date: [2025-01-14]
"""

import pandas as pd
from helper_functions import setup_openai_api, determine_model
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain, SequentialChain
import warnings

def main():
    """
    Main function demonstrating the use of SequentialChain for a multi-step workflow.
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
        "Translate the following review to English:\n\n{Review}"
    )
    chain_one = LLMChain(llm=llm, prompt=first_prompt, output_key="English_Review")

    # Step 7: Define the second prompt template
    second_prompt = ChatPromptTemplate.from_template(
        "Can you summarise the following review in 1 sentence:\n\n{English_Review}"
    )
    chain_two = LLMChain(llm=llm, prompt=second_prompt, output_key="summary")

    # Step 8: Define the third prompt template
    third_prompt = ChatPromptTemplate.from_template(
        "What language is the following review:\n\n{Review}"
    )
    chain_three = LLMChain(llm=llm, prompt=third_prompt, output_key="language")

    # Step 9: Define the fourth prompt template
    fourth_prompt = ChatPromptTemplate.from_template(
        "Write a follow-up response to the following summary in the specified language:\n\nSummary: {summary}\n\nLanguage: {language}"
    )
    chain_four = LLMChain(llm=llm, prompt=fourth_prompt, output_key="followup_message")

    # Step 10: Combine the chains into a SequentialChain
    overall_chain = SequentialChain(
        chains=[chain_one, chain_two, chain_three, chain_four],
        input_variables=["Review"],
        output_variables=["English_Review", "summary", "followup_message"],
        verbose=True
    )

    # Step 11: Run the SequentialChain with an example input
    review = df.Review[5]
    print("Original Review:")
    print(review)

    result = overall_chain.run({"Review": review})
    print("\nChain Outputs:")
    print(f"English Review: {result['English_Review']}")
    print(f"Summary: {result['summary']}")
    print(f"Follow-Up Message: {result['followup_message']}")

if __name__ == "__main__":
    main()
