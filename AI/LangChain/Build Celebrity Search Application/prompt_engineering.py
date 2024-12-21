# Integrate code with OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI 
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# OpenAI LLMs
llm = OpenAI(temperature=0.8)

# Memory
person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
description_memory = ConversationBufferMemory(input_key='dob', memory_key='description_history')

# Streamlit framework
st.title('Celebrity Search Results')
input_text = st.text_input("Search a topic about a celebrity")

# First Prompt Template
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template='Tell me about the celebrity {name}.'
)

# First LLM Chain
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person', memory=person_memory)

# Second Prompt Template
second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template='When was {person} born?'
)

# Second LLM Chain
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob', memory=dob_memory)

# Third Prompt Template
third_input_prompt = PromptTemplate(
    input_variables=['person', 'dob'],
    template='Mention 5 major events that happened around the time {person} was born, specifically around {dob}.'
)

# Third LLM Chain
chain3 = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='description', memory=description_memory)

# Combine the chains
parent_chain = SequentialChain(
    chains=[chain, chain2, chain3],
    input_variables=['name'],
    output_variables=['person', 'dob', 'description'],
    verbose=True
)

if input_text:
    # Use the __call__ method instead of run to handle multiple outputs
    result = parent_chain({'name': input_text})
    st.write(f"About: {result['person']}")
    st.write(f"Date of Birth: {result['dob']}")
    st.write(f"Major Events: {result['description']}")

    with st.expander('Person Name'):
        st.info(person_memory.buffer)

    with st.expander('Major Events'):
        st.info(description_memory.buffer)
