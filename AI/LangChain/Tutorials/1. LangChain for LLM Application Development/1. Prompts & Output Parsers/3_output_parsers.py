"""
This script demonstrates the use of LangChain's Response Schemas and Structured Output Parsers.
It includes:
1. Setting up the OpenAI API using environment variables.
2. Dynamically selecting the appropriate GPT model based on the current date.
3. Utilizing LangChain's ChatPromptTemplate to create structured prompts.
4. Using Response Schemas to define and parse structured outputs into JSON or Python dictionaries.

This script showcases how to extract specific information (e.g., gift status, delivery days, and price-related sentences)
from a customer review using LangChain's structured output parsing capabilities.

Author: [Roger J. Campbell]
Date: [Current Date]
"""

from helper_functions import setup_openai_api, determine_model
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
import warnings

def main():
    """
    Main function demonstrating Response Schemas and Structured Output Parsers.
    """
    # Step 1: Suppress depreciation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Step 2: Set up the OpenAI API by loading the environment variables
    setup_openai_api()

    # Step 3: Determine which model to use based on the current date
    llm_model = determine_model()

    # Step 4: Define the review text
    customer_review = """
    This leaf blower is pretty amazing. It has four settings: candle blower, gentle breeze, windy city, and tornado.
    It arrived in two days, just in time for my wife's anniversary present.
    I think my wife liked it so much she was speechless.
    So far I've been the only one using it, and I've been using it every other morning to clear the leaves on our lawn.
    It's slightly more expensive than the other leaf blowers out there, but I think it's worth it for the extra features.
    """

    # Step 5: Define the prompt template
    review_template = """
    For the following text, extract the following information:

    gift: Was the item purchased as a gift for someone else? Answer True if yes, False if not or unknown.

    delivery_days: How many days did it take for the product to arrive? If this information is not found, output -1.

    price_value: Extract any sentences about the value or price, and output them as a comma-separated Python list.

    Format the output as JSON with the following keys:
    gift
    delivery_days
    price_value

    text: {text}
    """

    # Step 6: Create a ChatPromptTemplate from the review template
    prompt_template = ChatPromptTemplate.from_template(review_template)

    # Step 7: Format the message using the template
    messages = prompt_template.format_messages(text=customer_review)

    # Step 8: Initialize the chat model
    chat = ChatOpenAI(temperature=0.0, model=llm_model)

    # Step 9: Get the response
    response = chat(messages)
    print("\nRaw Response Content:")
    print(response.content)

    # Step 10: Define Response Schemas
    gift_schema = ResponseSchema(name="gift", description="Was the item purchased as a gift for someone else? Answer True if yes, False if not or unknown.")
    delivery_days_schema = ResponseSchema(name="delivery_days", description="How many days did it take for the product to arrive? If this information is not found, output -1.")
    price_value_schema = ResponseSchema(name="price_value", description="Extract any sentences about the value or price, and output them as a comma-separated Python list.")

    response_schemas = [gift_schema, delivery_days_schema, price_value_schema]

    # Step 11: Create a StructuredOutputParser
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()
    print("\nFormat Instructions:")
    print(format_instructions)

    # Step 12: Define a new prompt with format instructions
    review_template_2 = """
    For the following text, extract the following information:

    gift: Was the item purchased as a gift for someone else? Answer True if yes, False if not or unknown.

    delivery_days: How many days did it take for the product to arrive? If this information is not found, output -1.

    price_value: Extract any sentences about the value or price, and output them as a comma-separated Python list.

    text: {text}

    {format_instructions}
    """

    # Step 13: Format the new prompt
    prompt = ChatPromptTemplate.from_template(template=review_template_2)
    messages = prompt.format_messages(text=customer_review, format_instructions=format_instructions)

    print("\nFormatted Message Content:")
    print(messages[0].content)

    # Step 14: Get the structured response
    response = chat(messages)
    print("\nStructured Response Content:")
    print(response.content)

    # Step 15: Parse the structured response into a Python dictionary
    output_dict = output_parser.parse(response.content)
    print("\nParsed Output Dictionary:")
    print(output_dict)

    # Step 16: Access specific values from the dictionary
    print("\nDelivery Days:", output_dict.get('delivery_days'))

if __name__ == "__main__":
    main()
