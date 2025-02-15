import pandas as pd

def get_the_question(survey_log: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the question with the highest answer rate.

    Args:
        survey_log (pd.DataFrame): A DataFrame containing survey interaction logs with columns:
                                   - "id" (int): Unique record ID
                                   - "action" (str): "show", "answer", or "skip"
                                   - "question_id" (int): Question ID
                                   - "answer_id" (int, nullable): ID of the answer if action is "answer", else NULL
                                   - "q_num" (int): Order of the question in the session
                                   - "timestamp" (int): Action timestamp

    Returns:
        pd.DataFrame: A DataFrame containing the question ID with the highest answer rate.
    """
    return (
        survey_log
        .groupby("question_id", as_index=False)
        .agg(answer_rate=("action", lambda x: (x == "answer").sum() / (x == "show").sum()))
        .rename(columns={"question_id": "survey_log"})
        .sort_values(by=["answer_rate", "survey_log"], ascending=[False, True])
        .loc[:, ["survey_log"]]
        .head(1)
    )

def main():
    # Example survey log data
    survey_data = {
        "id": [1, 2, 3, 4],
        "action": ["show", "answer", "show", "skip"],
        "question_id": [285, 285, 369, 369],
        "answer_id": [None, 12424, None, None],
        "q_num": [1, 1, 1, 1],
        "timestamp": [124, 125, 126, 127]
    }
    survey_df = pd.DataFrame(survey_data)

    # Get the highest answer rate question
    result = get_the_question(survey_df)

    # Display the result
    print(result)

if __name__ == "__main__":
    main()
