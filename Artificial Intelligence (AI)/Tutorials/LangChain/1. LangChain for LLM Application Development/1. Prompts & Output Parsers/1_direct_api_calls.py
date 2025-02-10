"""
This script demonstrates the use of the OpenAI API for handling basic, direct prompts.

The focus of this code is on:
1. Setting up the OpenAI API with an API key stored in a .env file.
2. Dynamically selecting the appropriate GPT model based on the current date.
3. Using the OpenAI API for simple, vanilla prompt-response tasks, such as answering questions
   and transforming text into a specified style.

This code represents the first part of a project on advanced prompt engineering. The next stage will 
introduce the use of LangChain for formatting prompts and managing workflows.

Author: [Roger J. Campbell]
Date: [2025-01-12]
"""

from helper_functions import setup_openai_api, determine_model, get_completion

def main():
    """
    Main function to demonstrate the use of OpenAI API with different prompts.
    """
    # Step 1: Set up the OpenAI API by loading the environment variables
    setup_openai_api()

    # Step 2: Determine which model to use based on the current date
    llm_model = determine_model()

    # Step 3: Example 1 - Simple arithmetic prompt
    arithmetic_prompt = "What is 1+1?"
    arithmetic_response = get_completion(arithmetic_prompt, model=llm_model)
    print("Arithmetic Response:", arithmetic_response)

    # Step 4: Example 2 - Translate a customer email into a calm and respectful tone
    customer_email = (
        "Arrr, I be fuming that me blender lid "
        "flew off and splattered me kitchen walls "
        "with smoothie! And to make matters worse, "
        "the warranty don't cover the cost of "
        "cleaning up me kitchen. I need yer help "
        "right now, matey!"
    )

    style = "American English in a calm and respectful tone"

    # Step 5: Construct the translation prompt with the specified style
    translation_prompt = (
        f"Translate the text that is delimited by triple backticks "
        f"into a style that is {style}.\n"
        f"text: ```{customer_email}```"
    )

    # Step 6: Get the translation response from the API
    translation_response = get_completion(translation_prompt, model=llm_model)
    print("Translation Response:", translation_response)

if __name__ == "__main__":
    main()
