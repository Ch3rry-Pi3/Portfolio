# 🦜🔗 **LangChain Q&A Evaluation Workflows**

## 📖 **Overview**
This part of the project focuses on evaluating the performance of a Q&A application built with LangChain. We demonstrate two primary workflows:

1. **Manual Evaluation** – Manually checking query responses against expected answers.
2. **LLM-Assisted Evaluation** – Leveraging a language model to automatically compare responses with ground-truth answers and provide grades (e.g., "CORRECT", "INCORRECT").

Both workflows rely on LangChain's `RetrievalQA` chain to retrieve relevant documents from a vectorstore, and OpenAI’s GPT models to generate and evaluate responses. These approaches help streamline the testing and validation of Q&A systems, ensuring accurate and reliable results.

## 📂 **Files**
1. **`1_manual_evaluation.py`**  
   Demonstrates how to create a Q&A system and manually evaluate the answers. Sample queries are run through the system, and the answers are checked against expected results.
   
2. **`2_llm_assisted_eval.py`**  
   Extends the Q&A system with an automated evaluation mechanism. It uses an LLM (GPT model) to generate additional test examples and then grades the predictions against the ground-truth answers.

## 🛠 **Functionality**
### **Key Features**
- Suppresses deprecation warnings for a cleaner console output.
- Dynamically selects an appropriate GPT model based on the current date.
- Loads a CSV file of product information and converts documents into embeddings for vector-based retrieval.
- Creates a Q&A system using LangChain’s `RetrievalQA` chain.
- **Manual Evaluation:** Prints out the real answer vs. predicted answer for each test query.
- **LLM-Assisted Evaluation:** Automatically grades the predictions ("CORRECT", "INCORRECT", or other feedback) by comparing them to ground-truth answers using `QAEvalChain`.

### **High-Level Flow**
1. **Document Loading**  
   Reads CSV data (e.g., `OutdoorClothingCatalog_1000.csv`) and loads it into LangChain structures.
2. **Vector Index Creation**  
   Converts documents into embeddings and stores them in a vector database (`DocArrayInMemorySearch`).
3. **Retrieval and Q&A**  
   Uses the `RetrievalQA` chain to fetch the most relevant chunks and generate answers.
4. **Evaluation**  
   - **Manual**: Compare the response to a known answer, printing both to the console.  
   - **LLM-Assisted**: Use an LLM-driven `QAEvalChain` to generate a grade or score for each answer.

## 📝 **Example Outputs**

Below are some **sample console outputs** (imagine these were displayed in your terminal rather than a Jupyter notebook):

<details>
<summary>Manual Evaluation Example</summary>

```plaintext
Example 0:
Question: Do the Cozy Comfort Pullover Set have side pockets?
Real Answer: Yes
Predicted Answer: Yes, the Cozy Comfort Pullover Set does have side pockets.
Predicted Grade: (N/A for manual evaluation)

Example 1:
Question: What collection is the Ultra-Lofty 850 Stretch Down Hooded Jacket from?
Real Answer: The DownTek collection
Predicted Answer: The Ultra-Lofty 850 Stretch Down Hooded Jacket is from the DownTek collection.
Predicted Grade: (N/A for manual evaluation)
```
</details>

<details>
<summary>LLM-Assisted Evaluation Example</summary>

```plaintext
Example 0:
Question: Do the Cozy Comfort Pullover Set have side pockets?
Real Answer: Yes
Predicted Answer: Yes, the Cozy Comfort Pullover Set does have side pockets.
Predicted Grade: CORRECT

Example 1:
Question: According to the document, what is the approximate weight of the Women's Campside Oxfords per pair?
Real Answer: The approximate weight of the Women's Campside Oxfords per pair is 1 lb. 1 oz.
Predicted Answer: The approximate weight of the Women's Campside Oxfords per pair is 1 lb. 1 oz.
Predicted Grade: CORRECT

Example 2:
Question: What collection is the Ultra-Lofty 850 Stretch Down Hooded Jacket from?
Real Answer: The DownTek collection
Predicted Answer: The Ultra-Lofty 850 Stretch Down Hooded Jacket is from the DownTek collection.
Predicted Grade: CORRECT
```
</details>

As shown, the **LLM-Assisted** workflow appends a grade, allowing you to quickly gauge the accuracy of each prediction.

## 📊 **Approaches for Querying Large Datasets**
In this project, we rely on the **stuff** approach for smaller datasets. For larger or more complex datasets, LangChain provides other options:

1. **Map-Reduce**  
   - **Description:** Splits documents into chunks, processes each chunk, and then merges results into a final answer.  
   - **Best For:** Summaries or generating coherent long-form answers from extensive sources.

2. **Refine**  
   - **Description:** Iteratively refines an initial answer with subsequent chunks of content.  
   - **Best For:** Tasks requiring iterative refinement or improved specificity.

3. **Map-Rerank**  
   - **Description:** Processes chunks independently, scores them, and selects the best-scoring result.  
   - **Best For:** Tasks needing the single most relevant chunk from multiple options.

## 🚀 **Conclusion**
These scripts demonstrate how to build and evaluate a Q&A application using LangChain, vector databases, and OpenAI’s GPT models. The **manual evaluation** process is straightforward and transparent, while the **LLM-assisted** approach speeds up testing by automatically grading each answer. 

Experiment with different evaluation strategies and retrieval chain approaches to handle larger datasets or more complex requirements. Happy coding! 🦜🔗
