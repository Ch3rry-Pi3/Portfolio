# <span style="color:#4682B4">**Dynamic Query Processing with LangChain Tools and Agents**</span>

## Overview

This project demonstrates the integration of LangChain tools and agents to handle dynamic queries across multiple sources, including web pages, Wikipedia, and academic articles. By combining advanced retrieval mechanisms, embeddings, and OpenAI's GPT models, the project enables accurate and contextually relevant responses to user queries.

### Key Features:
1. **Web Scraping**: Load and process online documentation from LangSmith.
2. **Wikipedia Integration**: Retrieve concise summaries from Wikipedia using the Wikipedia tool.
3. **Academic Article Querying**: Fetch and summarize academic articles from Arxiv.
4. **Dynamic Query Orchestration**: Use LangChain agents to manage queries across multiple tools.
5. **Agent Execution**: Dynamically interact with tools to generate responses based on user inputs.

## Tools Used:
1. **LangSmith Tool**: Retrieves information from LangSmith's documentation.
2. **Wikipedia Tool**: Queries Wikipedia for information about general topics.
3. **Arxiv Tool**: Retrieves and summarizes academic papers from the Arxiv database.

## Setup Instructions

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
- `langchain`: For building query pipelines with tools and agents.
- `langchain-openai`: For integrating OpenAI's GPT models.
- `dotenv`: For securely loading API keys.
- `langchain_community`: For tools like Wikipedia and Arxiv integration.

### 3. Add Configuration File
Create a `.env` file in the project directory to securely store your OpenAI API key. The file should look like this:

```plaintext
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Running the Notebook
1. Navigate to the project directory:
   ```bash
   cd dynamic-query-processing
   ```

2. Open the Jupyter notebook:
   ```bash
   jupyter notebook query_processing.ipynb
   ```

3. Follow the notebook instructions to:
   - Load LangSmith documentation from the web.
   - Query Wikipedia and Arxiv for information.
   - Create and test agents to dynamically handle queries.

### Example Queries
1. **LangSmith Example**:
   ```python
   {"input": "Tell me about LangSmith."}
   ```

2. **Wikipedia Example**:
   ```python
   {"input": "Tell me about Machine Learning."}
   ```

3. **Arxiv Example**:
   ```python
   {"input": "What is the paper 1605.08386 about?"}
   ```

Each query dynamically routes to the appropriate tool, retrieves relevant information, and generates a detailed response.

## Additional Notes
- Ensure the `requirements.txt` file matches the required versions of dependencies.
- Place the `query_processing.ipynb` notebook and the `.env` file in the same directory.
- This project demonstrates the versatility of LangChain tools and agents for multi-source query handling.
