# <span style="color:#4682B4">**Simple RAG Pipeline from Scratch with OpenAI and ChromaDB**</span>

## Overview
📖 This project demonstrates how to use **OpenAI embeddings** with **ChromaDB** to create an application for answering document-based queries. The application processes text documents, retrieves relevant content using embeddings and vector databases, and generates context-aware responses to user queries.

The project includes:
1. **📄 Document Processing**: Loads and preprocesses text-based documents.
2. **📊 ChromaDB Vector Database**: Stores and retrieves document embeddings for similarity-based searches.
3. **❓ Question Answering**: Dynamically processes user queries with OpenAI's GPT-3.5-Turbo model and provides context-aware responses.
4. **✂️ Efficient Text Chunking**: Splits documents into manageable chunks to optimise processing.

## Setup Instructions

### 1. Set Up the Environment
1. Open the terminal inside the project folder.
2. Create a virtual environment using Python 3.10:
   ```bash
   python -m venv myenv
   ```
3. Activate the virtual environment:
   - **Windows**:
     ```bash
     myenv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source myenv/bin/activate
     ```

### 2. Install Dependencies
📦 Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Add a Configuration File
🔑 Create a `.env` file in the project directory. This file should include your OpenAI API key:
```plaintext
OPENAI_API_KEY="Enter your OpenAI API key here"
```

### 4. Prepare the Text Documents
🗂️ Ensure the text documents are stored in a folder named `./news_articles` in the project directory. These files will be used to generate embeddings and answer questions.

### 5. Run the Application
▶️ Run the application:
```bash
python main.py
```

### 6. Interact with the Application
🖥️ Enter your query when prompted in the terminal to get context-aware answers based on the loaded documents.

## Key Features

### 1. **📄 Document Processing**
   - **Function**: `load_documents_from_directory(directory_path)`
   - **Purpose**: Loads text documents from a specified directory.
   - **Key Input**: Path to the directory containing `.txt` files.
   - **Output**: List of documents, each represented as a dictionary with `id` (filename) and `text` (content).

### 2. **✂️ Efficient Text Chunking**
   - **Function**: `split_text(text, chunk_size=1000, chunk_overlap=20)`
   - **Purpose**: Splits large text documents into smaller, manageable chunks with optional overlap.
   - **Key Inputs**:
     - `chunk_size`: Maximum size of each chunk.
     - `chunk_overlap`: Number of overlapping characters between chunks.
   - **Output**: List of text chunks.

### 3. **🧠 Embeddings with OpenAI**
   - **Function**: `get_openai_embedding(text)`
   - **Purpose**: Generates embeddings for text chunks using OpenAI's `text-embedding-3-small` model.
   - **Key Input**: Text string.
   - **Output**: A vector embedding for the input text.

### 4. **📊 Vector Database Management**
   - **Purpose**: Stores embeddings in ChromaDB for similarity-based retrieval.
   - **Key Operations**:
     - `collection.upsert()`: Adds document chunks and their embeddings to the database.
     - `collection.query()`: Retrieves the most relevant document chunks based on a query.

### 5. **❓ Question Answering**
   - **Function**: `generate_response(question, relevant_chunks)`
   - **Purpose**: Generates a concise answer to a user query using retrieved context and OpenAI's GPT-3.5-Turbo.
   - **Key Inputs**:
     - `question`: User query.
     - `relevant_chunks`: List of relevant document chunks.
   - **Output**: A concise, context-aware answer.

## Example Queries
💡 Try the following prompts to explore the application:
1. **"Tell me about the latest advancements in AI."**
2. **"Summarise key points on climate change from the documents."**
3. **"Provide insights into data-driven decision-making."**

## Example Response
When asking a question such as **"What are the key findings on AI?"**, the application retrieves the context and generates a concise response based on the loaded documents.

```plaintext
AI has seen rapid advancements in natural language processing, with models like GPT-3.5 improving human-like interaction. Key applications include text summarisation, sentiment analysis, and AI-driven chat systems. Recent research focuses on ethical AI and reducing biases in model predictions.
```

## Additional Notes
- ⚙️ Ensure the `requirements.txt` file includes all necessary dependencies for OpenAI, ChromaDB, and dotenv.
- 🔒 The `.env` file should be placed in the root directory for secure API key management.
- 📜 Use high-quality text documents to ensure accurate and relevant results.
- ✂️ Customise the `chunk_size` and `chunk_overlap` parameters in `split_text()` based on your document sizes and use case.

---
**For further inquiries or enhancements, please contact the project maintainer.**
