"""Creates a Streamlit application that integrates LangChain and OpenAI's GPT models to provide celebrity information, 
including a description, date of birth, and significant historical events around their birth.

The application is built using LangChain's LLM chains and memory to enable sequential prompts and conversation tracking.

Parameters:
----------
openai_key : str
    OpenAI API key loaded from the `constants.py` file and set as an environment variable.

os : module
    Used to set the OpenAI API key as an environment variable.

st : module
    Streamlit library for creating the interactive web app interface.

PromptTemplate : class
    LangChain class to define templates for generating prompts for OpenAI.

LLMChain : class
    LangChain class for creating language model chains using the defined prompts.

SequentialChain : class
    LangChain class for combining multiple LLMChains into a sequence.

ConversationBufferMemory : class
    LangChain memory class for storing conversation history for each chain.

Returns:
-------
Streamlit Application:
    The app allows users to:
    - Enter a celebrity's name to retrieve information.
    - View:
        - A brief description of the celebrity.
        - The celebrity's date of birth.
        - Five major events that occurred around their date of birth.
    - Expandable sections display:
        - Conversation history for the celebrity description and date of birth.
        - Major events history related to the date of birth.

Launch Instructions:
--------------------
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the following command:

    streamlit run prompt_engineering_app.py

Requirements:
-------------
1. `constants.py`:
    - Contains the OpenAI API key in a variable `openai_key`.
2. Libraries:
    - `os`: For setting environment variables.
    - `streamlit`: For creating the app's UI.
    - `langchain`: For defining and managing LLM chains, prompts, and memory.
3. Python Version:
    - Python 3.8 or later is recommended. 3.9 is used in myenv.

Code Organisation:
------------------
1. **Memory Management**:
    - `ConversationBufferMemory` is used to track conversation history for:
        - The celebrity's name and description (`person_memory`).
        - The celebrity's date of birth (`dob_memory`).
        - Significant historical events around their date of birth (`description_memory`).

2. **LLM Chains**:
    - `first_chain`: Generates a description of the celebrity based on their name.
    - `second_chain`: Retrieves the celebrity's date of birth.
    - `third_chain`: Identifies five major events that happened around the celebrity's date of birth.

3. **Sequential Execution**:
    - A `SequentialChain` combines all three chains, ensuring outputs from earlier chains are used as inputs for subsequent ones.

4. **Streamlit Interface**:
    - The main function renders the user interface, handles input, and displays results dynamically.
"""

# Import necessary libraries
import os
from constants import openai_key                            # OpenAI API key stored in constants.py
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
import streamlit as st

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = openai_key

# Initialise OpenAI LLM with specified temperature
llm = OpenAI(temperature=0.8)

# Define memory objects for conversation tracking
person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
description_memory = ConversationBufferMemory(input_key='dob', memory_key='description_history')

# Define prompt templates
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template='Tell me about the celebrity {name}.'
)

second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template='When was {person} born?'
)

third_input_prompt = PromptTemplate(
    input_variables=['person', 'dob'],
    template='Mention 5 major events that happened around the time {person} was born, specifically around {dob}.'
)

# Define LLM chains
first_chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person', memory=person_memory)
second_chain = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob', memory=dob_memory)
third_chain = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='description', memory=description_memory)

# Combine chains into a SequentialChain
celebrity_chain = SequentialChain(
    chains=[first_chain, second_chain, third_chain],
    input_variables=['name'],
    output_variables=['person', 'dob', 'description'],
    verbose=True
)

# Streamlit interface
def main():
    """
    Main function to render the Streamlit application.
    """

    st.title('Celebrity Search Results')

    # Input text box for user to search about a celebrity
    input_text = st.text_input("Search a topic about a celebrity")

    if input_text:
        # Execute the chain and fetch results
        result = celebrity_chain({'name': input_text})

        # Display results
        st.write(f"About: {result['person']}")
        st.write(f"Date of Birth: {result['dob']}")
        st.write(f"Major Events: {result['description']}")

        # Expanders for memory display
        with st.expander('Person Information History'):
            st.info(person_memory.buffer)

        with st.expander('Major Events History'):
            st.info(description_memory.buffer)

# Run the Streamlit app
if __name__ == '__main__':
    main()