import pandas as pd

def winning_candidate(candidate: pd.DataFrame, vote: pd.DataFrame) -> pd.DataFrame:
    """
    Determines the winning candidate based on the highest number of votes.

    Args:
        candidate (pd.DataFrame): A DataFrame containing candidate information with columns:
                                  - "id" (int): Unique candidate ID
                                  - "name" (str): Name of the candidate
        vote (pd.DataFrame): A DataFrame containing voting records with columns:
                             - "id" (int): Unique vote ID
                             - "candidateId" (int): Candidate ID that received the vote

    Returns:
        pd.DataFrame: A DataFrame with a single column "name" containing the name of the winning candidate.
    """
    return (
        candidate
        .merge(vote, left_on="id", right_on="candidateId", how="left")["name"]
        .value_counts()
        .reset_index()[["name"]]
        .iloc[:1]
    )

def main():
    # Example candidate data
    candidate_data = {
        "id": [1, 2, 3, 4, 5],
        "name": ["A", "B", "C", "D", "E"]
    }
    candidate_df = pd.DataFrame(candidate_data)

    # Example vote data
    vote_data = {
        "id": [1, 2, 3, 4, 5],
        "candidateId": [2, 4, 2, 3, 5]          # Candidate B gets 2 votes, others get 1 each
    }
    vote_df = pd.DataFrame(vote_data)

    # Get the winner
    winner = winning_candidate(candidate_df, vote_df)
    
    # Display the result
    print(winner)

if __name__ == "__main__":
    main()
