# 🦜🔗 **LangChain Q&A Application with Vector Databases**

## 📖 **Overview**
This project demonstrates the use of LangChain's Q&A capabilities for answering queries based on document retrieval. By leveraging a vector database, we efficiently retrieve and query information from a dataset, even with the constraints of large language models (LLMs).

LLMs, such as OpenAI’s GPT models, can only inspect a few thousand words at a time. This limitation makes vector databases essential, as they allow us to perform similarity-based searches across large datasets and pass only the most relevant chunks to the LLM for processing. This enhances efficiency and ensures high-quality responses.

In this implementation, we use LangChain's `RetrievalQA` with the **stuff** approach to process the retrieved data. The application also highlights the benefits of vector databases in facilitating queries over datasets.

## 📂 **Files**
1. `1_rag.py`: Demonstrates the Q&A process using LangChain, a CSV dataset, and a vector database.

## 🛠 **Functionality**
### **Key Features**
- Loads a CSV file containing product information.
- Converts the dataset into embeddings using OpenAI's embedding model.
- Stores embeddings in a vector database for efficient retrieval.
- Handles user queries using the `RetrievalQA` chain and outputs relevant results.

### 🔑 **Code Snippet**
Here is a brief overview of the core implementation:
```python
file_path = 'OutdoorClothingCatalog_1000.csv'
loader = CSVLoader(file_path=file_path)
documents = loader.load()

embeddings = OpenAIEmbeddings()
vectorstore = DocArrayInMemorySearch.from_documents(documents, embeddings)
retriever = vectorstore.as_retriever()

qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
query = "Please list all your shirts with sun protection in a table and summarise each one."
response = qa_chain.run(query)
print(response)
```

### 📝 **Example Outputs**
#### **Embedding Example**
```plaintext
Embedding length: 1536
First 5 dimensions of the embedding: [-0.021933607757091522, 0.006697045173496008, -0.01819835603237152, -0.03911325708316544, -0.014060650952160358]
```

#### **Query Example**
**Query:** `"Please suggest a shirt with sunblocking"`
```plaintext
Number of relevant documents: 4
First document content: Men's Tropical Plaid Short-Sleeve Shirt - UPF 50+ rated, 100% polyester, wrinkle-resistant, front and back cape venting, two front bellows pockets.
```

#### **Final Query Response**
**Query:** `"Please list all your shirts with sun protection in a table and summarise each one."`
```plaintext
Name                                   Description
Sun Shield Shirt                      High-performance sun shirt with UPF 50+ sun protection, moisture-wicking, and abrasion-resistant fabric.
Men's Plaid Tropic Shirt              Ultracomfortable shirt with UPF 50+ sun protection, wrinkle-free fabric, and front/back cape venting.
Men's TropicVibe Shirt                Men's sun-protection shirt with built-in UPF 50+ and front/back cape venting.
Men's Tropical Plaid Short-Sleeve Shirt Lightest hot-weather shirt with UPF 50+ sun protection and two front bellows pockets.

All of these shirts provide UPF 50+ sun protection, blocking 98% of the sun's harmful rays.
```

## 📊 **Approaches for Querying Large Datasets**
In this project, we used the **stuff** approach, but LangChain provides other powerful methods to process retrieved documents:

1. **Map-Reduce**
   - **Description:** Splits the documents into chunks, processes each chunk separately, and combines the results into a final answer.
   - **Best For:** Summarising large datasets or generating long-form answers.

2. **Refine**
   - **Description:** Processes the first chunk, produces an initial response, and refines it iteratively as subsequent chunks are processed.
   - **Best For:** Tasks requiring iterative improvement of the output.

3. **Map-Rerank**
   - **Description:** Processes chunks independently and assigns scores to each chunk. The chunk with the highest score determines the final answer.
   - **Best For:** Selecting the most relevant response from multiple options.

## 🚀 **Conclusion**
This application demonstrates the power of combining LLMs and vector databases to overcome token limitations and deliver efficient, accurate responses. While the **stuff** approach is sufficient for small datasets, alternative methods like map_reduce, refine, or map_rerank are better suited for large or complex datasets.

Explore these methods to build more scalable and versatile applications. Happy coding! 🦜🔗
