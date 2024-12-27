# <span style="color:#4682B4">**Document Embedding and Retrieval with LangChain**</span>

## Overview

This project demonstrates the use of LangChain to process and retrieve information from various types of documents. It utilises embeddings and vector databases to perform similarity-based searches, making it possible to extract insights from both structured and unstructured data.

### Key Features:
1. **Data Ingestion**: Load documents from text files, web pages, and PDFs.
2. **Text Splitting**: Divide documents into manageable chunks to optimize processing.
3. **Embedding and Vector Databases**: Convert document chunks into vector representations and store them in Chroma and FAISS databases.
4. **Similarity Search**: Retrieve the most relevant document chunks based on user queries.

### Example Documents:
1. **speech.txt**: Contains excerpts from U.S. President Woodrow Wilson's 1917 "War Message to Congress."
2. **attention.pdf**: The *Attention Is All You Need* paper, which introduced the Transformer model.

### 1. Set Up the Environment
To begin, create a local Python environment for the project:
- Open the Command Prompt (cmd) inside the project folder.
- Run the following command to initialize Conda for your shell (if not already done):
  ```bash
  conda init
  ```
  Close and reopen the terminal for the changes to take effect.

- Next, create a Conda environment with Python 3.10:
  ```bash
  conda create -p myenv python=3.10 -y
  ```

### 2. Install Dependencies
After creating the environment, install the required dependencies using the `requirements.txt` file:
- Activate the environment:
  ```bash
  conda activate myenv/
  ```
- Install the dependencies:
  ```bash
  pip install -r requirements.txt
  ```
The `requirements.txt` file contains:
- `openai`: For interacting with OpenAI's GPT models.
- `langchain`: For building applications with LangChain.
- `streamlit`: For creating web-based interactive applications.

### 3. Add Configuration File
Create a `constants.py` file in the project directory. This file should include your OpenAI API key:
```python
openai_key = 'Enter OpenAI API here'
```
