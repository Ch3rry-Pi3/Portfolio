"""
This script demonstrates manual evaluation of a Q&A system with LangChain, including:
1. Suppressing deprecation warnings.
2. Setting up the OpenAI API using environment variables.
3. Dynamically selecting the appropriate GPT model based on the current date.
4. Using a CSVLoader to load documents for vector-based retrieval.
5. Creating a Q&A application with LangChain's RetrievalQA.
6. Generating and combining example query-answer pairs.
7. Performing manual evaluation with debug logging.

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
from langchain.evaluation.qa import QAGenerateChain
from langchain.evaluation.qa import QAEvalChain  # QAEvalChain imported but not used here

def main():
    """
    Main function demonstrating the manual evaluation process using LangChain components.
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

    # Step 6: Create a vectorstore index and initialise the Q&A app
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

    # Step 7: Demonstrate creating test points
    print(data[10])
    print(data[11])

    # Step 8: Hard-coded examples
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

    # Step 9: LLM-generated examples
    example_gen_chain = QAGenerateChain.from_llm(ChatOpenAI(model=llm_model))
    new_examples = example_gen_chain.apply_and_parse(
        [{"doc": t} for t in data[:5]]
    )

    # For demonstration
    print(new_examples[0])
    print(data[0])

    # Step 10: Combine hard-coded and LLM-generated examples
    examples += new_examples

    # Step 11: Run a query and print the result
    print(qa.run(examples[0]["query"]))

    # Step 12: Manual evaluation with debug logging
    langchain.debug = True
    print(qa.run(examples[0]["query"]))
    langchain.debug = False

if __name__ == "__main__":
    main()
