# 🦜🔍 **Q&A with LangChain**

## 📖 **Overview**

This tutorial explores **retrieval-based question answering** in LangChain, focusing on how to fetch relevant context from a vector database and construct an informative response using a large language model (LLM). This is part of a broader tutorial series on advanced **retrieval-augmented generation (RAG)** techniques.

The diagram below illustrates how this tutorial fits within the overall series:

![QnA Overview](images/L5-QnA.png)

## 🏗 **Structure of the Retrieval Process**

The question-answering pipeline consists of several key stages:

1. **Storage**: Questions are stored in a **vector database** for similarity search.
2. **Retrieval**: The most relevant text chunks are retrieved based on similarity.
3. **Output**: A final **prompt** is constructed and passed to the LLM to generate an answer.

The diagram below illustrates this structure:

![Retrieval Structure](images/L5-structure.png)

## 🛠 **Implementation Details**

This tutorial covers:

- **Setting up a Chroma vector database** with OpenAI embeddings.
- **Querying the database** for relevant information.
- **Constructing a retrieval-based QA system** using LangChain.
- **Exploring alternative retrieval strategies** for improved results.

## 📂 **Files**

1. **`question_answering.py`** - Implements a retrieval-based QA pipeline.

## 🚀 **Core Implementation**

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
persist_directory = 'docs/chroma/'
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

### **Enhancing the QA System with Custom Prompts**

```python
from langchain.prompts import PromptTemplate

# Custom prompt template
template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know. Use three sentences max.
Always say 'Thanks for asking!' at the end.

{context}

Question: {question}
Helpful Answer:"""

QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

# Create QA chain with custom prompt
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectordb.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

# Query the new QA chain
question = "Is probability a class topic?"
result = qa_chain({"query": question})

print(result["result"])
```

#### 🖥 **Console Output**
```
'Yes, probability is a class topic as the instructor assumes familiarity with
basic probability and statistics. Thanks for asking!'
```

## 📌 **Exploring Advanced Retrieval Techniques**

LangChain supports different **retrieval chain types**, which impact how retrieved documents are processed before being passed to the LLM. These include:

- **Map-Reduce**: Processes each document independently and then combines results.
- **Refine**: Iteratively refines the response across multiple chunks.
- **Map-Rerank**: Scores retrieved documents and selects the highest-ranked one.

The diagram below illustrates these techniques:

![Retrieval Techniques](images/L5-techniques.png)

### **Using `map_reduce` Retrieval**

```python
qa_chain_mr = RetrievalQA.from_chain_type(
    llm,
    retriever=vectordb.as_retriever(),
    chain_type="map_reduce"
)
result = qa_chain_mr({"query": question})
print(result["result"])
```

#### 🖥 **Console Output**
```
'Yes, probability is a class topic in the document.'
```

### **Using `refine` Retrieval**

```python
qa_chain_refine = RetrievalQA.from_chain_type(
    llm,
    retriever=vectordb.as_retriever(),
    chain_type="refine"
)
result = qa_chain_refine({"query": question})
print(result["result"])
```

#### 🖥 **Console Output**
```
'The original answer already provides a comprehensive explanation of how
probability is a class topic, including examples of class applications.
The refined response does not significantly alter the original answer.'
```

## 🔥 **Key Takeaways**

✅ **Retrieval-based QA** improves LLM responses by providing relevant context.  
✅ **Chroma vector store** enables efficient similarity-based document retrieval.  
✅ **Alternative retrieval methods** (`map_reduce`, `refine`, `map_rerank`) impact response quality.  
✅ **Custom prompt engineering** can tailor responses to be more concise and user-friendly.  