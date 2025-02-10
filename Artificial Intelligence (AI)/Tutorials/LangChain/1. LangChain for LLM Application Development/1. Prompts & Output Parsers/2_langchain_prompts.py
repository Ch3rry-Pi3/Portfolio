"""
This script demonstrates the use of LangChain for prompt templating.
It includes:
1. Setting up the OpenAI API using environment variables.
2. Dynamically selecting the appropriate GPT model based on the current date.
3. Introducing LangChain's ChatPromptTemplate to format prompts for a conversational AI model.

Author: [Roger J. Campbell]
Date: [2025-01-12]
"""

from helper_functions import setup_openai_api, determine_model
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import warnings

def main():
    """
    Main function demonstrating LangChain's prompt templating features.
    """
    # Step 1: Suppress depreciation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Step 2: Set up the OpenAI API by loading the environment variables
    setup_openai_api()

    # Step 3: Determine which model to use based on the current date
    llm_model = determine_model()

    # Step 4: Initialise the chat model with specified temperature
    chat = ChatOpenAI(temperature=0.0, model=llm_model)

    # Step 5: Define the template string for prompts
    template_string = """Translate the text that is delimited by triple backticks into a style that is {style}. text: ```{text}```"""

    # Step 6: Create a ChatPromptTemplate from the template string
    prompt_template = ChatPromptTemplate.from_template(template_string)

    # Step 7: Define customer message style and content
    customer_style = "American English in a calm and respectful tone"
    customer_email = """Arrr, I be fuming that me blender lid flew off and splattered me kitchen walls with smoothie! And to make matters worse, the warranty don't cover the cost of cleaning up me kitchen. I need yer help right now, matey!"""

    # Step 8: Format the customer message with the template
    customer_messages = prompt_template.format_messages(
        style=customer_style,
        text=customer_email
    )

    print("\nStep 1: Type of customer_messages:", type(customer_messages))
    print("\nStep 2: Type of first message in customer_messages:", type(customer_messages[0]))
    print("\nStep 3: Content of the first message in customer_messages:")
    print(customer_messages[0])

    # Step 9: Call the LLM to translate to the style of the customer message
    customer_response = chat(customer_messages)

    print("\nStep 4: Content of the customer response:")
    print(customer_response.content)

    # Step 10: Define service message style and content
    service_reply = """Hey there customer, the warranty does not cover cleaning expenses for your kitchen because it's your fault that you misused your blender by forgetting to put the lid on before starting the blender. Tough luck! See ya!"""

    service_style_pirate = "a polite tone that speaks in English Pirate"

    # Step 11: Format the service message with the template
    service_messages = prompt_template.format_messages(
        style=service_style_pirate,
        text=service_reply
    )

    print("\nStep 5: Content of the first service message:")
    print(service_messages[0].content)

    # Step 12: Call the LLM to translate the service message
    service_response = chat(service_messages)

    print("\nStep 6: Content of the service response:")
    print(service_response.content)

if __name__ == "__main__":
    main()
