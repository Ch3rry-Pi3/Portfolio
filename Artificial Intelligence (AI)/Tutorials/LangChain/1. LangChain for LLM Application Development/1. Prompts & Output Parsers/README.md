# 🦜🔗 **LangChain for LLM Application Development**

## 📖 **Overview**
This repository demonstrates the progression of techniques for building LLM-powered applications. It covers three key stages:

1. **Direct API Calls**: Basic usage of OpenAI's API to interact with an LLM.
2. **LangChain Prompts**: Leveraging LangChain to streamline prompt design and management.
3. **Output Parsers**: Using LangChain's tools for structured and validated output.

These stages illustrate how LangChain simplifies the development of advanced applications by enhancing the flexibility and functionality of LLMs.

## 📂 **Files**
1. `1_direct_api_calls.py`: Demonstrates basic API usage for prompt-response tasks.
2. `2_langchain_prompts.py`: Introduces LangChain's `ChatPromptTemplate` for prompt templating.
3. `3_output_parsers.py`: Explores LangChain's `ResponseSchema` and `StructuredOutputParser` for extracting structured outputs.
4. `helper_functions.py`: Contains reusable utility functions for API setup and model selection.

## 🥇 **1. Direct API Calls**
### 🛠 **Description**
This script demonstrates how to make direct API calls to OpenAI's models for simple prompt-response tasks.

### **Key Features**
- API setup using environment variables.
- Dynamic model selection based on date.
- Basic interaction with the LLM.

### 🔑 **Code Snippet**
```python
from helper_functions import setup_openai_api, determine_model

setup_openai_api()
model = determine_model()

prompt = "What is 1+1?"
response = get_completion(prompt, model)
print("Response:", response)
```

### 📝 **Example Output**
**Input Prompt:**
```
What is 1+1?
```

**Output:**
```
Response: 2
```

## 🥈 **2. LangChain Prompts**
### 🛠 **Description**
This script introduces LangChain's `ChatPromptTemplate` for managing structured prompts. It shows how LangChain simplifies creating reusable and parameterized prompts.

### **Key Features**
- Dynamic prompt creation using `ChatPromptTemplate`.
- Formatting user-defined styles and input text into structured prompts.
- Simplifies the process of generating consistent prompts.

### 🔑 **Code Snippet**
```python
from langchain.prompts import ChatPromptTemplate

customer_style = "American English in a calm and respectful tone"
customer_email = "Arrr, I be fuming that me blender lid flew off and splattered me kitchen walls..."

template_string = """Translate the text that is delimited by triple backticks into a style that is {style}. text: ```{text}```"""

prompt_template = ChatPromptTemplate.from_template(template_string)
messages = prompt_template.format_messages(style=customer_style, text=customer_email)
response = chat(messages)
print("Response:", response.content)
```

### 📝 **Example Output**
**Input:**
```
Translate the text into American English in a calm and respectful tone.
```

**Output:**
```
Response: I understand your frustration. Unfortunately, the warranty does not cover cleaning expenses for the kitchen...
```

## 🥉 **3. Output Parsers**
### 🛠 **Description**
This script demonstrates the use of LangChain's `ResponseSchema` and `StructuredOutputParser` to extract structured outputs, ensuring consistent formatting and validation.

### **Key Features**
- Define schemas for structured responses.
- Automatically validate and parse LLM outputs into Python dictionaries.
- Handle complex extraction tasks with ease.

### 🔑 **Code Snippet**
```python
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

response_schemas = [
    ResponseSchema(name="gift", description="Was the item purchased as a gift for someone else?"),
    ResponseSchema(name="delivery_days", description="How many days did it take for the product to arrive?"),
    ResponseSchema(name="price_value", description="Sentences about the value or price.")
]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()

review_template = """For the following text, extract structured information. {format_instructions}"""
prompt = ChatPromptTemplate.from_template(template=review_template)
messages = prompt.format_messages(text=customer_review, format_instructions=format_instructions)
response = chat(messages)
output_dict = output_parser.parse(response.content)
print(output_dict)
```

### 📝 **Example Output**
**Input Review:**
```
This leaf blower is amazing... It arrived in two days...
```

**Structured Output:**
```json
{
    "gift": true,
    "delivery_days": 2,
    "price_value": [
        "It's slightly more expensive than other leaf blowers..."
    ]
}
```

## 🚀 **Conclusion**
This repository showcases the journey of building LLM-powered applications:

1. **Basic Direct API Calls**: Learn the fundamentals of interacting with OpenAI's API.
2. **LangChain Prompts**: Simplify and scale prompt creation with LangChain.
3. **Output Parsers**: Extract and validate structured responses for advanced use cases.

LangChain unlocks powerful tools for efficient and scalable LLM app development. Happy building! 🦜🔗
