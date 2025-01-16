"""
This script demonstrates LLM-assisted evaluation of a Q&A system using LangChain, including:
1. Suppressing deprecation warnings.
2. Setting up the OpenAI API using environment variables.
3. Dynamically selecting the appropriate GPT model based on the current date.
4. Creating a Q&A application with LangChain's RetrievalQA.
5. Generating and combining example query-answer pairs.
6. Running the Q&A system to get predictions for each example.
7. Evaluating the predictions using an LLM-based evaluation chain.

Author: [Roger J. Campbell]
Date: [2025-01-16]
"""

import warnings
import langchain
from helper_functions import setup_openai_api, determine_model
from langchain_openai import ChatOpenAI
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.evaluation.qa import QAGenerateChain, QAEvalChain

def main():
    """
    Main function demonstrating LLM-assisted evaluation of the Q&A system.
    """
    # Step 1: Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Step 2: Set up the OpenAI API by loading environment variables
    setup_openai_api()

    # Step 3: Determine which model to use based on the current date
    llm_model = determine_model()

    # Step 4: Initialise the chat model with specified temperature
    llm = ChatOpenAI(temperature=0.0, model=llm_model)

    # Step 5: Load documents from a CSV file
    file_path = 'OutdoorClothingCatalog_1000.csv'
    loader = CSVLoader(file_path=file_path)
    data = loader.load()

    index = VectorstoreIndexCreator(
        vectorstore_cls=DocArrayInMemorySearch
    ).from_loaders([loader])

    llm = ChatOpenAI(temperature=0.0, model=llm_model)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=index.vectorstore.as_retriever(),
        verbose=True,
        chain_type_kwargs={
            "document_separator": "<<<<>>>>>"
        }
    )

    # Step 6: Demonstrate creating test points
    print(data[10])
    print(data[11])

    # Step 7: Hard-coded examples
    examples = [
        {
            "query": "Do the Cozy Comfort Pullover Set have side pockets?",
            "answer": "Yes"
        },
        {
            "query": "What collection is the Ultra-Lofty 850 Stretch Down Hooded Jacket from?",
            "answer": "The DownTek collection"
        }
    ]

    # Step 8: LLM-generated examples
    example_gen_chain = QAGenerateChain.from_llm(ChatOpenAI(model=llm_model))
    new_examples = example_gen_chain.apply_and_parse(
        [{"doc": t} for t in data[:5]]
    )

    # For demonstration
    print(new_examples[0])
    print(data[0])

    # Step 9: Combine hard-coded and LLM-generated examples
    examples += new_examples

    # Step 10: Run a sample query from the combined examples
    qa.run(examples[0]["query"])

    # Step 11: Use the Q&A chain to get predictions for all examples
    predictions = qa.apply(examples)

    # Step 12: Perform LLM-assisted evaluation of the predictions
    llm_eval = ChatOpenAI(temperature=0, model=llm_model)
    eval_chain = QAEvalChain.from_llm(llm_eval)

    graded_outputs = eval_chain.evaluate(examples, predictions)

    # Step 13: Print the evaluation results
    for i, eg in enumerate(examples):
        print(f"Example {i}:")
        print("Question: " + predictions[i]['query'])
        print("Real Answer: " + predictions[i]['answer'])
        print("Predicted Answer: " + predictions[i]['result'])
        print("Predicted Grade: " + graded_outputs[i]['text'])
        print()

    # Optional: Print the first graded output for convenience
    print(graded_outputs[0])

if __name__ == "__main__":
    main()
