# Deploy LLM as API with FastAPI

## Overview
This project demonstrates how to deploy Large Language Models (LLMs) as APIs using FastAPI and integrate them with Streamlit for an interactive web interface. The project includes:
1. `app.py`: A FastAPI server for generating essays and poems using OpenAI's GPT models and LLAMA2.
2. `client.py`: A Streamlit client application for interacting with the FastAPI server.

## Setup Instructions

### 1. Set Up the Virtual Environment
1. Open the Command Prompt (cmd) inside the project folder.
2. Initialise Conda for your shell (if not already done):
   ```bash
   conda init
   ```
   Close and reopen the terminal for the changes to take effect.

3. Create a Conda environment with Python 3.9:
   ```bash
   conda create -p myenv python=3.9 -y
   ```
   A folder named `myenv` will be created in the project directory.

### 2. Install Dependencies
After activating the environment:
```bash
conda activate myenv/
```
Install the required dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 3. Add a Configuration File
Create a `.env` file in the project directory. This file should include your API keys:
```plaintext
LANGCHAIN_API_KEY="Enter LangChain API here"
OPENAI_API_KEY="Enter OpenAI API here"
LANGCHAIN_PROJECT="Tutorial2"
```

### 4. Create the `app.py` File
This file initialises the FastAPI server. It handles requests for generating essays and poems using OpenAI's GPT models and LLAMA2. The server provides the following endpoints:
- `/openai`: Uses OpenAI models.
- `/essay`: Generates essays.
- `/poem`: Generates poems.

Run the server:
```bash
python app.py
```

You can verify the server is running by visiting the FastAPI documentation at:
[http://localhost:8000/docs](http://localhost:8000/docs)

![FastAPI Documentation](images/Langchain%20Server.png)

### 5. Create the `client.py` File
This file serves as the frontend for the FastAPI server. It uses Streamlit to provide a user-friendly interface for interacting with the API.

### 6. Run the Streamlit Application
Open a new terminal window, reactivate the virtual environment, and ensure the FastAPI server is still running. Run the Streamlit app:
```bash
streamlit run client.py
```

In the terminal window, you can verify the connection is established:
![Streamlit Terminal Logs](images/Terminal%20View.png)

### 7. Interact with the Application
Navigate to the Streamlit app in your web browser. You can use it to generate essays and poems:

#### Essay Generation:
![Essay Example](images/Essay%20Example.png)

#### Poem Generation:
![Poem Example](images/Poem%20Example.png)
```