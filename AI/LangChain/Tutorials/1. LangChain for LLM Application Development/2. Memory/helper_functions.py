import os
import openai
import datetime
from dotenv import load_dotenv

def setup_openai_api():
    """
    Loads environment variables and sets the OpenAI API key.
    """
    # Step 1: Load environment variables from the .env file
    load_dotenv()

    # Step 2: Retrieve the OpenAI API key from the environment variables
    openai.api_key = os.getenv("OPENAI_API_KEY")

def determine_model():
    """
    Determines which OpenAI GPT model to use based on the current date.

    Returns:
        str: The model name to use.
    """
    # Step 1: Get the current date
    current_date = datetime.datetime.now().date()

    # Step 2: Define the target date for model change
    target_date = datetime.date(2024, 6, 12)

    # Step 3: Compare the current date with the target date and select the model
    return "gpt-3.5-turbo" if current_date > target_date else "gpt-3.5-turbo-0301"

def get_completion(prompt, model):
    """
    Sends a prompt to the OpenAI API and retrieves the response.

    Args:
        prompt (str): The input prompt to send to the model.
        model (str): The OpenAI model to use.

    Returns:
        str: The generated response from the model.
    """
    # Step 1: Construct the request payload with the prompt
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0  # Step 2: Use deterministic output
    )

    # Step 3: Extract and return the generated content from the response
    return response["choices"][0]["message"]["content"]