# 🧠 **LangChain Conversational Memory**

## 📖 **Overview**

This tutorial focuses on **adding memory** to a LangChain retrieval-based question-answering (QA) system. By using memory, we allow the system to **retain past conversations**, making it more contextually aware in multi-turn interactions.

The diagram below illustrates the **retrieval process**, showing how memory is integrated alongside retrieval to construct a more informed response:

![Retrieval Structure](images/L5-structure.png)

This section covers:

- **Basic retrieval-based QA** using a vector database.
- **Adding memory using `ConversationBufferMemory`**.
- **Using `ConversationalRetrievalChain`** to retain conversation history.
- **Comparing retrieval QA with and without memory**.

## 📂 **Files**

1. **`memory.py`** - Implements retrieval-based QA with conversational memory.

## 🛠 **Implementation Details**

### **Setting Up the Vector Database**

```python
import warnings
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from helper_functions import setup_openai_api

# Suppress deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Initialise OpenAI API
setup_openai_api()

# Setup the Chroma vector database
persist_directory = 'documents/chroma/'
embedding = OpenAIEmbeddings()
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

# Check the number of stored documents
print(f"Vector DB contains {vectordb._collection.count()} entries.")
```

#### 🖥 **Console Output**
```
Vector DB contains 1024 entries.
```

### **Performing a Retrieval-Based Query**

```python
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# Select language model
llm = ChatOpenAI(model_name="gpt-4", temperature=0)

# Create a retrieval-based QA pipeline
qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectordb.as_retriever())

# Define the question
question = "What are major topics for this class?"
result = qa_chain({"query": question})

print(result["result"])
```

#### 🖥 **Console Output**
```
'The major topics for this class include machine learning, statistics, and algebra.
Additionally, there will be discussions on extensions of the material covered in the main lectures.'
```

## 🧠 **Adding Memory to the QA System**

By default, **retrieval-based QA does not retain context** between queries. To enable memory, we use **`ConversationBufferMemory`**, which stores previous interactions.

```python
from langchain.memory import ConversationBufferMemory

# Initialise memory for tracking chat history
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)
```

## 🔄 **Using Conversational Retrieval Chain**

To integrate memory into our retrieval-based QA, we use **`ConversationalRetrievalChain`**.

```python
from langchain.chains import ConversationalRetrievalChain

# Create a conversational retrieval-based QA chain
qa = ConversationalRetrievalChain.from_llm(
    llm,
    retriever=vectordb.as_retriever(),
    memory=memory
)
```

### **Example Multi-Turn Conversation**

#### 📝 **First Question**
```python
question = "Is probability a class topic?"
result = qa({"question": question})
print(result['answer'])
```

#### 🖥 **Console Output**
```
'Yes, probability is a common topic covered in mathematics classes, particularly in courses like statistics or probability theory. It involves understanding the likelihood of different outcomes and events occurring.'
```

#### 📝 **Follow-Up Question (Uses Memory)**
```python
question = "Why are those prerequisites needed?"
result = qa({"question": question})
print(result['answer'])
```

#### 🖥 **Console Output**
```
'Prerequisites for probability classes are typically required to ensure that students have the necessary mathematical background to understand and apply the concepts taught in the probability course. This background knowledge may include topics such as algebra, calculus, and statistics, which are essential for a deeper understanding of probability theory.'
```

## 🔥 **Key Takeaways**

✅ **Retrieval-based QA** can be enhanced with **conversational memory**.  
✅ **`ConversationBufferMemory`** allows past questions to influence future answers.  
✅ **`ConversationalRetrievalChain`** seamlessly integrates memory into retrieval.  
✅ **Memory enables better contextual understanding in multi-turn conversations.**  