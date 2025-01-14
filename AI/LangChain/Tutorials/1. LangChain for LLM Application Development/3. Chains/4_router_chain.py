"""
This script demonstrates the use of LangChain's LLMRouterChain and MultiPromptChain modules.
It includes:
1. Setting up the OpenAI API using environment variables.
2. Dynamically selecting the appropriate GPT model based on the current date.
3. Creating multiple prompt templates for different subject areas.
4. Using LLMRouterChain to dynamically select the appropriate prompt based on the input.
5. Demonstrating the chain's functionality with example inputs.

Author: [Roger J. Campbell]
Date: [2025-01-14]
"""

import pandas as pd
from helper_functions import setup_openai_api, determine_model
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.chains import LLMChain
from langchain.chains.router import MultiPromptChain
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
import warnings

def main():
    """
    Main function demonstrating the use of LLMRouterChain and MultiPromptChain.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()

    # Step 3: Determine which model to use based on the current date
    llm_model = determine_model()

    # Step 4: Initialise the chat model with specified temperature
    llm = ChatOpenAI(temperature=0.0, model=llm_model)

    # Step 5: Define prompt templates for various subjects
    prompt_infos = [
        {
            "name": "physics", 
            "description": "Good for answering questions about physics", 
            "prompt_template": """You are a very smart physics professor. You are great at answering questions about physics in a concise and easy-to-understand manner. When you don't know the answer to a question, you admit that you don't know.\n\nHere is a question:\n{input}"""
        },
        {
            "name": "math", 
            "description": "Good for answering math questions", 
            "prompt_template": """You are a very good mathematician. You are great at answering math questions. You are so good because you are able to break down hard problems into their component parts, answer the component parts, and then put them together to answer the broader question.\n\nHere is a question:\n{input}"""
        },
        {
            "name": "history", 
            "description": "Good for answering history questions", 
            "prompt_template": """You are a very good historian. You have an excellent knowledge of and understanding of people, events, and contexts from a range of historical periods.\n\nHere is a question:\n{input}"""
        },
        {
            "name": "computer science", 
            "description": "Good for answering computer science questions", 
            "prompt_template": """You are a successful computer scientist. You are great at solving problems with a balance of time and space complexity.\n\nHere is a question:\n{input}"""
        },
        {
            "name": "DEFAULT",
            "description": "A fallback prompt for questions that don't match any specific category",
            "prompt_template": "{input}"
        }
    ]

    # Step 6: Create destination chains
    destination_chains = {}
    for p_info in prompt_infos:
        name = p_info["name"]
        prompt_template = p_info["prompt_template"]
        prompt = ChatPromptTemplate.from_template(template=prompt_template)
        chain = LLMChain(llm=llm, prompt=prompt)
        destination_chains[name] = chain

    # Step 7: Define router prompt
    destinations = [f"{p['name']}: {p['description']}" for p in prompt_infos]
    destinations_str = "\n".join(destinations)

    MULTI_PROMPT_ROUTER_TEMPLATE = """Given a raw text input to a language model, select the model prompt best suited for the input.\n\n<< CANDIDATE PROMPTS >>\n{destinations}\n\n<< INPUT >>\n{{input}}\n\n<< OUTPUT >>\n```json\n{{{{\n    \"destination\": string,\n    \"next_inputs\": string\n}}}}\n```"""

    router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(destinations=destinations_str)
    router_prompt = PromptTemplate(template=router_template, input_variables=["input"], output_parser=RouterOutputParser())

    # Step 8: Create router chain and MultiPromptChain
    router_chain = LLMRouterChain.from_llm(llm, router_prompt)
    chain = MultiPromptChain(router_chain=router_chain, destination_chains=destination_chains, verbose=True)

    # Step 9: Test the chain with example inputs
    print("Physics Question:", chain.run("What is black body radiation?"))
    print("Math Question:", chain.run("What is 2 + 2?"))
    print("Default Question:", chain.run("Why does every cell in our body contain DNA?"))

if __name__ == "__main__":
    main()
