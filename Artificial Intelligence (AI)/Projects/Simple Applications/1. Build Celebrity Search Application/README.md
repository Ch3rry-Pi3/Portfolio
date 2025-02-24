# LangChain and Streamlit Project

## Overview
This project demonstrates the integration of LangChain with OpenAI's GPT models to create interactive applications using Streamlit. It includes two main applications:
1. `basic_app.py`: A simple application showcasing LangChain's capabilities without using advanced features like prompt engineering or memory.
2. `prompt_engineering_app.py`: A more advanced application that uses LangChain's prompt templates, memory, and sequential chains to build a dynamic and context-aware celebrity search app.

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
  This command ensures the environment uses Python version 3.9 (required as the project requires Python > 3.8.1). A folder named `myenv` will be created in the project directory.

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
