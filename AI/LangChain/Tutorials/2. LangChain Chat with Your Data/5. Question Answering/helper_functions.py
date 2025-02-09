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