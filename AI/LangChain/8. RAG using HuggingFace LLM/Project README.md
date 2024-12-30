# <span style="color:#4682B4">**Statewise Insurance Data Analysis with LangChain and HuggingFace**</span>

## Overview

This project demonstrates the integration of LangChain's retrieval-based pipelines and HuggingFace models to process and analyze statewise insurance data. By combining advanced document processing, embeddings, and similarity search techniques, the project allows users to dynamically query and retrieve context-aware responses from PDF documents.

### Key Features:
1. **PDF Document Processing**: Load and split PDF files into manageable chunks for efficient analysis.
2. **HuggingFace Embeddings**: Use pre-trained HuggingFace models to create semantic embeddings for document chunks.
3. **Vector Database Integration**: Store and retrieve embeddings using FAISS for similarity-based searches.
4. **Custom Prompting**: Define prompts to ensure relevant and focused responses to queries.
5. **Question-Answering Pipeline**: Combine retrieval mechanisms and language models for accurate responses to user-defined queries.

## Tools Used:
1. **LangChain**: Provides the framework for document processing, retrieval, and Q&A pipelines.
2. **HuggingFace**: Powers embeddings and text generation through pre-trained models like GPT-2.
3. **FAISS**: Enables fast and efficient similarity search for document chunks.

## Setup Instructions

### 1. Set Up the Environment
To begin, create a local Python environment for the project:
- Open the Command Prompt (cmd) inside the project folder.
- Initialize Conda for your shell (if not already done):
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
- `langchain`: For building retrieval pipelines and prompt templates.
- `langchain-huggingface`: For HuggingFace model integration.
- `dotenv`: For securely managing API keys.
- `faiss-cpu`: For vector storage and similarity search.

### 3. Add Configuration File
Create a `.env` file in the project directory to securely store your HuggingFace API key. The file should look like this:

```plaintext
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here
```

## Usage

### Running the Notebook
1. Navigate to the project directory:
   ```bash
   cd statewise-insurance-analysis
   ```

2. Open the Jupyter notebook:
   ```bash
   jupyter notebook insurance_analysis.ipynb
   ```

3. Follow the notebook instructions to:
   - Load and preprocess PDF documents.
   - Create embeddings and store them in a FAISS vector database.
   - Execute similarity searches and run a Q&A pipeline.

### Example Queries
1. **Query Example 1**:
   ```python
   {"query": "What are the differences in uninsured rate by state in 2022?"}
   ```

2. **Query Example 2**:
   ```python
   {"query": "Explain the trends in health insurance coverage for 2022."}
   ```

Each query retrieves the most relevant document chunks and generates a detailed response.


## Additional Notes
- Ensure the `requirements.txt` file matches the required versions of dependencies.
- Place the `insurance_analysis.ipynb` notebook and the `.env` file in the same directory.
- This project demonstrates the potential of LangChain and HuggingFace tools for processing and querying document-based datasets.