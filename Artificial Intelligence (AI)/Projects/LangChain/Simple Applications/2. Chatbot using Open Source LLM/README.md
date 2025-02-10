# Building Chatbots using Paid & Open Source LLMs

## Overview
This project demonstrates how to integrate LangChain with OpenAI's GPT models and LLAMA2 to create interactive chatbot applications using Streamlit. It includes two main applications:
1. `app.py`: A basic chatbot application using OpenAI GPT models.
2. `locallama.py`: A chatbot application using the open-source LLAMA2 model integrated via LangChain.

## Setup Instructions

### 1. Set Up the Environment
To begin, create a local Python environment for the project:
- Open the Command Prompt (cmd) inside the project folder.
- Run the following command to initialize Conda for your shell (if not already done):
  ```bash
  conda init
  ```
  Close and reopen the terminal for the changes to take effect.

- Next, create a Conda environment with Python 3.9:
  ```bash
  conda create -p myenv python=3.9 -y
  ```
  This ensures the environment uses Python version 3.9 (required as the project requires Python > 3.8.1). A folder named `myenv` will be created in the project directory.

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
The `requirements.txt` file includes dependencies for:
- `openai`: For integrating OpenAI's GPT models.
- `langchain`: For building applications with LangChain.
- `streamlit`: For creating web-based interactive applications.
- Additional libraries for advanced features like LLAMA2 integration, document parsing, and vector search.

### 3. Install Ollama for LLAMA2 Integration
The `locallama.py` application uses the open-source LLAMA2 model through Ollama. Follow these steps to set up Ollama:
1. Visit the [Ollama website](https://ollama.com/) and download the Ollama software for your operating system.
2. Follow the installation instructions provided on the website to install Ollama on your machine.
3. Once installed, use the terminal to download the LLAMA2 model:
   ```bash
   ollama pull llama2
   ```
   Ensure the `ollama` command is accessible from your terminal after installation.

### 4. Add a Configuration File
Create a `.env` file in the project directory. This file should include your API keys:
```plaintext
LANGCHAIN_API_KEY="Enter LangChain API here"
OPENAI_API_KEY="Enter OpenAI API here"
LANGCHAIN_PROJECT="Tutorial1"
```

Ensure these API keys are valid for accessing LangChain and OpenAI services.

## Running the Applications

### Launch the OpenAI GPT Application
1. Navigate to the project directory in your terminal.
2. Run the following command to launch the application:
   ```bash
   streamlit run app.py
   ```

### Launch the LLAMA2 Application
1. Ensure Ollama is installed and the LLAMA2 model has been pulled successfully.
2. Run the following command to launch the LLAMA2 application:
   ```bash
   streamlit run locallama.py
   ```

Both applications will open in your default web browser, providing an interactive chatbot interface.