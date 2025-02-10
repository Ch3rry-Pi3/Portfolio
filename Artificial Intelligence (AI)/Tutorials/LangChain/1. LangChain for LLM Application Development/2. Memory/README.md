# 🦜🔗 **LangChain Memory Modules for LLM Application Development**

## 📖 **Overview**
Memory modules are essential in developing advanced conversational applications using large language models (LLMs). They enable chat systems to retain context, recall past interactions, and provide a more coherent user experience. This part of the project demonstrates the capabilities of LangChain's memory modules, showing how they can be configured for different use cases and contexts.

The memory modules covered in this tutorial are:

1. **ConversationBufferMemory**: Retains the full conversational history.
2. **ConversationBufferWindowMemory**: Maintains a sliding window of recent exchanges.
3. **ConversationTokenBufferMemory**: Stores context up to a specific token limit.
4. **ConversationSummaryBufferMemory**: Summarises past interactions to preserve context efficiently.

## 📂 **Files**
1. `conversation_buffer_memory.py`: Demonstrates the use of ConversationBufferMemory.
2. `conversation_buffer_window_memory.py`: Showcases ConversationBufferWindowMemory.
3. `conversation_token_buffer_memory.py`: Highlights ConversationTokenBufferMemory.
4. `conversation_summary_memory.py`: Explores ConversationSummaryBufferMemory.
5. `helper_functions.py`: Contains reusable utility functions for API setup and model selection.

## 🥇 **1. ConversationBufferMemory**
### 🛠 **Description**
This module retains the full conversational history, making it suitable for applications that require the entire context of past exchanges.

### **Key Features**
- Stores the entire conversation history.
- Useful for in-depth interactions that need full context recall.

### 🔑 **Code Snippet**
```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory, verbose=True)

print(conversation.predict(input="Hi, my name is Roger"))
print(conversation.predict(input="What is 1+1?"))
print(conversation.predict(input="What is my name?"))

print(memory.load_memory_variables({}))
```

### 📝 **Example Output**
```
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. ...

Current conversation:

Human: Hi, my name is Roger
AI:

> Finished chain.
Hello Roger! It's nice to meet you. How can I assist you today?

> Entering new ConversationChain chain...
Current conversation:
Human: Hi, my name is Roger
AI: Hello Roger! ...
Human: What is 1+1?
AI:

> Finished chain.
1+1 equals 2. Is there anything else you would like to know?

{'history': "Human: Hi, my name is Roger\nAI: Hello Roger! ..."}
```

## 🥈 **2. ConversationBufferWindowMemory**
### 🛠 **Description**
This module maintains a sliding window of recent exchanges, making it ideal for contexts where only the most recent interactions are relevant.

### **Key Features**
- Retains a fixed number of recent exchanges.
- Reduces memory overhead while preserving relevant context.

### 🔑 **Code Snippet**
```python
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=1)
conversation = ConversationChain(llm=llm, memory=memory, verbose=False)

print(conversation.predict(input="Hi, my name is Roger"))
print(conversation.predict(input="What is 1+1?"))
print(conversation.predict(input="What is my name?"))

print(memory.load_memory_variables({}))
```

### 📝 **Example Output**
```
Hello Roger! It's nice to meet you. How can I assist you today?
1+1 equals 2. Is there anything else you would like to know?
I'm sorry, I do not have access to personal information such as your name.

{'history': 'Human: Not much, just hanging\nAI: Cool'}
```

## 🥉 **3. ConversationTokenBufferMemory**
### 🛠 **Description**
This module limits the context retained by a specific token count, balancing context retention and computational efficiency.

### **Key Features**
- Retains context up to a defined token limit.
- Useful for managing memory in resource-constrained environments.

### 🔑 **Code Snippet**
```python
from langchain.memory import ConversationTokenBufferMemory

memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=50)
memory.save_context({"input": "AI is what?!"}, {"output": "Amazing!"})
...

print(memory.load_memory_variables({}))
```

### 📝 **Example Output**
```
{'history': 'Human: AI is what?!\nAI: Amazing!\n...'}
```

## 🏆 **4. ConversationSummaryBufferMemory**
### 🛠 **Description**
This module summarises past interactions, enabling long-term context retention within a limited token budget.

### **Key Features**
- Summarises interactions to preserve key details.
- Ideal for maintaining coherence in extended conversations.

### 🔑 **Code Snippet**
```python
from langchain.memory import ConversationSummaryBufferMemory

memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
memory.save_context({"input": "What is on the schedule today?"}, {"output": schedule})
...

print(memory.load_memory_variables({}))
```

### 📝 **Example Output**
```
{'history': 'System: The human and AI exchange greetings and discuss the schedule for the day...'}
```

## 🚀 **Conclusion**
Memory modules are critical for creating responsive and context-aware LLM applications. By leveraging LangChain's memory capabilities, developers can:

1. **Retain Conversational Context**: Choose between full, sliding-window, token-limited, or summarised memories.
2. **Optimise Resources**: Adapt memory strategies to balance performance and resource usage.

LangChain's memory modules empower developers to craft intelligent, flexible, and scalable applications. Happy building! 🦜🔗

