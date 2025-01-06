# **Dense Passage Retrieval (DPR) Example**

## 📖 **Overview**
This project demonstrates the application of **Dense Passage Retrieval (DPR)**, a widely used technique in **Retrieval-Augmented Generation (RAG)** pipelines. DPR is a dense retrieval method that leverages deep learning models to generate semantic embeddings for queries and context passages. It improves upon traditional retrieval methods (e.g., TF-IDF, BM25) by capturing the meaning and context of text rather than relying on exact word matches.

### **Key Concepts in DPR**
1. **Dense Embeddings**:
   - Queries and passages are represented as fixed-size dense vectors in a high-dimensional space, capturing semantic meaning.
2. **Dual Encoders**:
   - Separate encoders for queries and contexts ensure each representation is specialized for its task.
3. **Similarity Matching**:
   - **Cosine similarity** is computed between query and passage embeddings to retrieve the most relevant passages.

### **Why Use DPR in RAG?**
- **Advantages Over Traditional Retrieval**:
  - Captures semantic relationships between queries and passages.
  - Handles query variations and paraphrasing effectively.
  - Scales well with large corpora using precomputed passage embeddings.
- **Integration with RAG Pipelines**:
  - Acts as the **retrieval component**, providing top-k relevant passages to a generative model for final answer generation.


## ⚙️ **Pipeline Steps**

### 1. **Model and Tokenizer Loading**
- Two separate encoders are used:
  - **DPRQuestionEncoder**: Encodes the query into a dense embedding.
  - **DPRContextEncoder**: Encodes each context passage into a dense embedding.
- These models are pre-trained on datasets like **Natural Questions (NQ)** and **MS MARCO**.

### 2. **Query and Passage Encoding**
- The query is tokenized and passed through the **question encoder** to generate a semantic embedding.
- Context passages are tokenized and processed by the **context encoder** to generate passage embeddings.

### 3. **Similarity Computation**
- The cosine similarity between the query embedding and each passage embedding is calculated, ranking the passages by relevance.

### 4. **Passage Retrieval**
- The passage with the highest similarity score is identified as the most relevant.

## 🔧 **Setup Instructions**

### 1. **Environment Setup**
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

### 2. **Install Dependencies**
📦 Install the required libraries:
```bash
pip install torch transformers numpy scikit-learn
```

### 3. **Run the Script**
▶️ Execute the script:
```bash
python dpr_example.py
```

## 🧠 **Theoretical Context**
### **Dense Passage Retrieval (DPR)**
- DPR employs **deep bidirectional transformers** (e.g., BERT) to encode both queries and passages.
- It replaces traditional sparse retrieval methods like **TF-IDF** and **BM25**, which rely on keyword matches, with dense embeddings that capture semantic similarity.

| **Aspect**                | **DPR (Dense)**           | **TF-IDF/BM25 (Sparse)**        |
|---------------------------|---------------------------|----------------------------------|
| **Representation**        | Dense vectors            | Sparse term-based vectors       |
| **Retrieval Basis**       | Semantic similarity      | Exact or partial word matches   |
| **Handling Synonyms**     | Robust (e.g., "car" ~ "automobile") | Limited                        |
| **Context Awareness**     | High                     | None                            |
| **Performance**           | Strong for open-domain tasks | Better for exact-match queries |

### **Applications**
- **Retrieval-Augmented Generation (RAG)**:
  - DPR acts as the **retriever**, narrowing down the corpus to the most relevant documents for a given query.
- **Open-Domain Question Answering**:
  - DPR retrieves passages that are semantically aligned with the question.

---

## 📜 **Example Output**

### **Input Query**
```
"capital of africa?"
```

### **Passages**
1. Paris is the capital of France.
2. Berlin is the capital of Germany.
3. Madrid is the capital of Spain.
4. Rome is the capital of Italy.
5. Maputo is the capital of Mozambique.
6. To be or not to be, that is the question.
7. The quick brown fox jumps over the lazy dog.
8. Grace Hopper was an American computer scientist...

### **Results**
- **Similarities**:
    ```
    [[0.5736569  0.5479354  0.5798749  0.5730073  0.5849961  0.46129075
      0.36704755 0.34993213]]
    ```
- **Most Relevant Passage**:
    ```
    Maputo is the capital of Mozambique.
    ```

## 📂 **Key Code Snippets**

### **1. Loading Models**
```python
# Load question encoder and tokenizer
question_encoder = DPRQuestionEncoder.from_pretrained(
    "facebook/dpr-question_encoder-single-nq-base"
)
question_tokenizer = DPRQuestionEncoderTokenizer.from_pretrained(
    "facebook/dpr-question_encoder-single-nq-base"
)

# Load context encoder and tokenizer
context_encoder = DPRContextEncoder.from_pretrained(
    "facebook/dpr-ctx_encoder-single-nq-base"
)
context_tokenizer = DPRContextEncoderTokenizer.from_pretrained(
    "facebook/dpr-ctx_encoder-single-nq-base"
)
```

### **2. Encoding Query**
```python
query = "capital of africa?"
question_inputs = question_tokenizer(query, return_tensors="pt")
question_embedding = question_encoder(**question_inputs).pooler_output
```

### **3. Encoding Passages**
```python
passages = [
    "Paris is the capital of France.",
    "Berlin is the capital of Germany.",
    # ...
]

context_embeddings = []
for passage in passages:
    context_inputs = context_tokenizer(passage, return_tensors="pt")
    context_embedding = context_encoder(**context_inputs).pooler_output
    context_embeddings.append(context_embedding)
context_embeddings = torch.cat(context_embeddings, dim=0)
```

### **4. Computing Similarities**
```python
similarities = cosine_similarity(
    question_embedding.detach().numpy(), context_embeddings.detach().numpy()
)
most_relevant_idx = np.argmax(similarities)
most_relevant_passage = passages[most_relevant_idx]
```

## 🎯 **Additional Notes**
- The script uses **Hugging Face Transformers** to leverage pre-trained DPR models.
- Warnings (e.g., unused weights) are suppressed for cleaner output.
- Modify the `passages` list or query to experiment with different inputs.

Feel free to reach out if you have questions or need further assistance! 🚀