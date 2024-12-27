```markdown
# <span style="color:#4682B4">**Document Question-Answering with LangChain and Llama2**</span>

## Overview

This project demonstrates the integration of LangChain and the Llama2 large language model (LLM) to build a question-answering system. It uses embeddings and the FAISS vector database to retrieve relevant document content and generate detailed, context-aware responses to user queries.

### Key Features:
1. **PDF Processing**: Load and process the *Attention Is All You Need* research paper.
2. **Text Splitting**: Divide the PDF content into manageable chunks for efficient processing.
3. **Embedding and Vector Database**: Convert document chunks into vector representations and store them in a FAISS vector database.
4. **Query Processing with Llama2**: Use the Llama2 LLM to process queries and generate responses based on retrieved document content.
5. **Custom Retrieval Chain**: Combine a retriever and a document chain to create a seamless query-response pipeline.

### Example Document:
1. **attention.pdf**: The *Attention Is All You Need* research paper by Vaswani et al., which introduced the Transformer model.

## Setup Instructions

### 1. Set Up the Environment
Ensure Python 3.10 is installed. Create and activate a virtual environment for the project:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Linux/Mac)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate
```

### 2. Install Dependencies
Install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:
- `openai`: For embedding and query processing with OpenAI models.
- `langchain`: For building document retrieval and processing pipelines.
- `langchain-openai`: For integrating OpenAI embeddings.
- `langchain-ollama`: For using the Llama2 LLM via Ollama.

### 3. Add Configuration
Create a `.env` file in the project directory to securely store your OpenAI API key. The file should look like this:

```plaintext
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Running the Notebook
1. Navigate to the project directory:
   ```bash
   cd rag
   ```

2. Open the Jupyter notebook:
   ```bash
   jupyter notebook simplerag.ipynb
   ```

3. Follow the notebook instructions to:
   - Load and process the `attention.pdf` document.
   - Embed document chunks into a FAISS vector database.
   - Create and test a retrieval chain to process user queries.

### Example Query
Here’s an example query to test the retrieval chain:

```python
query = "An attention function can be described as mapping a query"
response = retriever_chain.invoke({"input": query})
print(response["answer"])
```

## Additional Notes

- This project focuses on the integration of LangChain and Llama2 for advanced question-answering capabilities.
- Ensure the `attention.pdf` document is placed in the project directory before running the notebook.
- The notebook is modular, allowing you to customize the workflow for different documents or LLMs.
```