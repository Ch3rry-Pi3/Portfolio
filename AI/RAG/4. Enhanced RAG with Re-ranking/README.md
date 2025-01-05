# **Retrieval-Augmented Generation (RAG) with Multiple Queries and Re-ranking**

## Overview
📖 This project builds upon the **Query Expansion with Multiple Queries** model by introducing **re-ranking**. While multiple queries enhance recall by broadening the search scope, re-ranking improves precision by ensuring that only the most relevant documents are used for generating the final answer.

### Limitations of Simple Query Expansion:
1. ❌ **Lower Precision**: Even with expanded queries, retrieved documents may not fully align with the original query's intent.
2. ❌ **Suboptimal Context**: Without prioritisation, irrelevant documents may dilute the final context passed to the LLM.

### The Solution: Query Expansion with Re-ranking
In this project:
1. **Multiple queries** are used to retrieve a broader context from the vector store.
2. The retrieved documents are **re-ranked** using a cross-encoder model to ensure precision.
3. The most relevant documents are aggregated and passed to the LLM for generating a concise, context-aware final answer.

This technique significantly improves the alignment between the retrieved context and the user's query, resulting in more accurate and coherent answers.

## Pipeline Steps

### 1. **📄 Document Processing**
- **Purpose**: Load and preprocess a PDF document.
- **Process**: Text is extracted from the PDF and filtered for empty pages.
- **Output**: A list of strings, each representing the text from a PDF page.

### 2. **✂️ Text Splitting**
- **Purpose**: Divide text into manageable chunks to create embeddings.
- **Methods**:
  - **Character-based splitting**: Splits text into chunks based on character limits.
  - **Token-based splitting**: Further splits character-based chunks into token-sized chunks.
- **Output**: A list of text chunks suitable for embedding.

### 3. **📊 ChromaDB Vector Database**
- **Purpose**: Store and retrieve document embeddings.
- **Operations**:
  - **Add**: Store document chunks and their embeddings.
  - **Query**: Retrieve relevant document chunks based on a query.
- **Output**: Retrieved document chunks with their embeddings.

### 4. **🧠 Query Expansion**
- **Purpose**: Use multiple queries to expand the search scope and improve recall.
- **Process**: For this example, the generated queries are hardcoded. These are:
  - **Original Query**: "What were the most important factors that contributed to increases in revenue?"
  - **Generated Queries**:
    - "What were the major drivers of revenue growth?"
    - "Were there any new product launches that contributed to the increase in revenue?"
    - "Did any changes in pricing or promotions impact the revenue growth?"
    - "What were the key market trends that facilitated the increase in revenue?"
    - "Did any acquisitions or partnerships contribute to the revenue growth?"

### 5. **❓ Context Retrieval and Deduplication**
- **Purpose**: Retrieve document chunks for all queries and remove duplicates.
- **Process**:
  - Query the vector store with the original and generated queries.
  - Combine results and remove duplicate documents.
- **Output**: A set of unique, relevant documents.

### 6. **📉 Re-ranking**
- **Purpose**: Rank the retrieved documents by relevance to the original query.
- **Process**:
  - Use a cross-encoder model to assign relevance scores to each document.
  - Sort the documents by score in descending order.
- **Output**: A prioritised list of documents.

### 7. **📜 Answer Generation**
- **Purpose**: Generate a final, context-aware answer using the LLM.
- **Process**:
  - Aggregate the top-ranked documents into a single context.
  - Pass the context and the original query to the LLM to generate the answer.
- **Output**: A concise, well-informed answer.

## Example Queries and Output

### **Original Query**
"What were the most important factors that contributed to increases in revenue?"

### **Generated Queries**
- "What were the major drivers of revenue growth?"
- "Were there any new product launches that contributed to the increase in revenue?"
- "Did any changes in pricing or promotions impact the revenue growth?"
- "What were the key market trends that facilitated the increase in revenue?"
- "Did any acquisitions or partnerships contribute to the revenue growth?"

### **Final Answer**
```
1. Growth in intelligent cloud revenue, specifically driven by Azure and other cloud services.
2. Growth in productivity and business processes revenue, driven by Office 365 commercial and LinkedIn.
3. Investments in Azure, including 4 points of growth from the Nuance acquisition.
4. Increase in Microsoft cloud services.
5. Increase in Microsoft 365 demand.
6. Growth in Dynamics 365 and Dynamics products and cloud services revenue.
7. Increase in server products and cloud services revenue, particularly driven by Azure and other cloud services.
8. Increase in enterprise services revenue, primarily from growth in enterprise support services.
9. Increase in Office commercial products and cloud services revenue, driven by Office 365 commercial growth.
10. Increase in LinkedIn revenue.
```
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

### 4. Prepare the Input PDF
🗂️ Ensure the input PDF document is stored in the `data` directory and named `microsoft-annual-report.pdf`. This file will be used to generate embeddings and answer queries.

### 5. Run the Application
▶️ Run the application:
```bash
python rag_with_reranking.py
```

### 6. Interact with the Application
🖥️ Enter your query when prompted in the terminal to see enhanced context-aware answers.

## Additional Notes
- ⚙️ Ensure the `requirements.txt` file includes all necessary dependencies for OpenAI, ChromaDB, and dotenv.
- 🔒 The `.env` file should be placed in the root directory for secure API key management.
- 📜 Use high-quality PDF documents to ensure accurate and relevant results.
- ✂️ Customise the `chunk_size` and `tokens_per_chunk` parameters based on the document size and application requirements.

---
**For further inquiries or enhancements, please contact the project maintainer.**

