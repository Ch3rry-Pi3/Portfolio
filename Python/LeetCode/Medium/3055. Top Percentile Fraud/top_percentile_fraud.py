import pandas as pd

def top_percentile_fraud(fraud: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies the top 5% of fraudulent claims per state based on fraud scores.

    Args:
        fraud (pd.DataFrame): Contains claim data with columns:
            - "policy_id" (int): The unique ID of the insurance policy.
            - "state" (str): The state in which the policy is registered.
            - "fraud_score" (float): The fraud likelihood score.

    Returns:
        pd.DataFrame: A table containing:
            - "policy_id" (int): The ID of the policy flagged as fraudulent.
            - "state" (str): The state associated with the policy.
            - "fraud_score" (float): The fraud score of the policy.
        
        The result is filtered to only include the top 5% of fraudulent claims in each state.
        The table is sorted by:
            1. "state" (ascending order),
            2. "fraud_score" (descending order),
            3. "policy_id" (ascending order).
    """
    return (
        fraud
        # Compute the percentile rank for fraud scores within each state
        .assign(percentile=lambda x: x.groupby("state")["fraud_score"].rank(method="dense", pct=True))
        # Filter for the top 5% fraudulent claims
        .query("percentile >= 0.95")
        # Drop the percentile column since it's no longer needed
        .drop(columns="percentile")
        # Sort by state (asc), fraud_score (desc), policy_id (asc)
        .sort_values(["state", "fraud_score", "policy_id"], ascending=[True, False, True])
    )


if __name__ == "__main__":
    # Example usage
    fraud_data = pd.DataFrame({
        "policy_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        "state": ["California", "California", "California", "New York", "New York", "New York", 
                  "Texas", "Texas", "Texas", "Florida", "Florida", "Florida", "Florida", "Florida"],
        "fraud_score": [0.92, 0.68, 0.17, 0.94, 0.81, 0.77, 0.98, 0.95, 0.97, 0.98, 0.78, 0.94, 0.88, 0.66]
    })

    print(top_percentile_fraud(fraud_data))
