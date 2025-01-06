"""
Dense Passage Retrieval (DPR) Example

This script demonstrates Dense Passage Retrieval (DPR) using the Hugging Face Transformers library. 
It retrieves the most relevant passage for a given query by:
1. Encoding the query and context passages into dense embeddings using pre-trained DPR models.
2. Calculating cosine similarity between the query embedding and passage embeddings.
3. Returning the passage with the highest similarity score.

Steps:
1. Import necessary libraries and suppress warnings.
2. Load pre-trained DPR models and tokenizers.
3. Encode a query into a dense embedding.
4. Encode context passages into dense embeddings.
5. Compute similarity scores and retrieve the most relevant passage.
"""

# ==========================
# 1. Import Libraries
# ==========================
import warnings
warnings.filterwarnings("ignore")  # Suppress all warnings for clarity

from transformers import (
    DPRQuestionEncoder,
    DPRContextEncoder,
    DPRQuestionEncoderTokenizer,
    DPRContextEncoderTokenizer,
)
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# ==========================
# 2. Main Function
# ==========================
def main():
    """
    Main function to demonstrate Dense Passage Retrieval (DPR).
    """
    # ==========================
    # 2.1 Load Pre-trained Models and Tokenizers
    # ==========================
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

    # ==========================
    # 2.2 Encode Query
    # ==========================
    # Define the query
    query = "capital of africa?"
    
    # Tokenize and encode the query
    question_inputs = question_tokenizer(query, return_tensors="pt")
    question_embedding = question_encoder(**question_inputs).pooler_output
    # The question embedding is a dense vector representation of the query

    # ==========================
    # 2.3 Encode Passages
    # ==========================
    # Define a list of context passages
    passages = [
        "Paris is the capital of France.",
        "Berlin is the capital of Germany.",
        "Madrid is the capital of Spain.",
        "Rome is the capital of Italy.",
        "Maputo is the capital of Mozambique.",
        "To be or not to be, that is the question.",
        "The quick brown fox jumps over the lazy dog.",
        "Grace Hopper was an American computer scientist...",
    ]

    # Tokenize and encode each passage
    context_embeddings = []
    for passage in passages:
        context_inputs = context_tokenizer(passage, return_tensors="pt")
        context_embedding = context_encoder(**context_inputs).pooler_output
        context_embeddings.append(context_embedding)
    context_embeddings = torch.cat(context_embeddings, dim=0)
    # Combine all passage embeddings into a single tensor for comparison

    # ==========================
    # 2.4 Compute Similarities
    # ==========================
    # Calculate cosine similarity between query and passage embeddings
    similarities = cosine_similarity(
        question_embedding.detach().numpy(), context_embeddings.detach().numpy()
    )
    print("Similarities:", similarities)

    # ==========================
    # 2.5 Retrieve Most Relevant Passage
    # ==========================
    # Find the passage with the highest similarity score
    most_relevant_idx = np.argmax(similarities)
    most_relevant_passage = passages[most_relevant_idx]

    # Print the most relevant passage
    print("\nMost Relevant Passage:")
    print(most_relevant_passage)

# ==========================
# 3. Entry Point
# ==========================
if __name__ == "__main__":
    main()
