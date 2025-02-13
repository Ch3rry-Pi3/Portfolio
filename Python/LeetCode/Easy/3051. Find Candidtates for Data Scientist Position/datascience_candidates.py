import pandas as pd

def find_candidates(candidates: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies candidates who possess all three required skills: 
    'Python', 'Tableau', and 'PostgreSQL'.

    Parameters:
    candidates (pd.DataFrame): A DataFrame containing candidate skill information with columns:
                               - 'candidate_id' (int): Unique identifier for each candidate.
                               - 'skill' (str): Name of the skill.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'candidate_id' (int): Candidates who have all three required skills.
                  The result is sorted in ascending order by 'candidate_id'.
    """
    # Filter candidates who have one of the required skills
    filtered_candidates = candidates[candidates["skill"].isin(["Python", "Tableau", "PostgreSQL"])]

    # Count the number of required skills each candidate has
    skill_counts = filtered_candidates.groupby("candidate_id")["skill"].nunique().reset_index()

    # Select candidates who have all three required skills
    qualified_candidates = skill_counts[skill_counts["skill"] == 3][["candidate_id"]]

    return qualified_candidates


def main():
    """
    Main function to demonstrate the find_candidates function with a sample dataset.
    """
    # Sample candidates data
    candidates_data = {
        "candidate_id": [101, 101, 101, 102, 102, 103, 103, 103, 104, 104, 105],
        "skill": ["Python", "Tableau", "PostgreSQL", "Python", "Tableau", 
                  "Python", "PostgreSQL", "Tableau", "Python", "Tableau", "PostgreSQL"]
    }

    # Convert dictionary to DataFrame
    candidates_df = pd.DataFrame(candidates_data)

    # Find candidates with all required skills
    result = find_candidates(candidates_df)

    # Display result
    print(result)


# Run the script only if executed directly
if __name__ == "__main__":
    main()
