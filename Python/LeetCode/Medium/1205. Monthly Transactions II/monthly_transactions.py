import pandas as pd


def monthly_transactions(transactions: pd.DataFrame, chargebacks: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the monthly transaction summary for each country.

    This function calculates the number of approved transactions, their total amount,
    and the number and total amount of chargebacks for each month and country.

    Args:
        transactions (pd.DataFrame): DataFrame containing transaction details with columns:
            - "id" (int): Unique transaction ID.
            - "country" (str): Country where the transaction occurred.
            - "state" (str): Transaction state ("approved" or "declined").
            - "amount" (int): Transaction amount.
            - "trans_date" (datetime): Transaction date.
        
        chargebacks (pd.DataFrame): DataFrame containing chargeback details with columns:
            - "trans_id" (int): Reference to transaction ID.
            - "trans_date" (datetime): Chargeback transaction date.

    Returns:
        pd.DataFrame: A DataFrame with the following columns:
            - "month" (str): Year-Month in "YYYY-MM" format.
            - "country" (str): Country where the transaction occurred.
            - "approved_count" (int): Count of approved transactions.
            - "approved_amount" (int): Sum of approved transaction amounts.
            - "chargeback_count" (int): Count of chargebacks.
            - "chargeback_amount" (int): Sum of chargeback amounts.
    """
    # Merge transactions with chargebacks to align data
    df = transactions.merge(chargebacks, left_on="id", right_on="trans_id", how="left")

    # Extract month from transaction and chargeback dates
    df["month_transaction"] = df["trans_date_x"].dt.strftime("%Y-%m")
    df["month_chargeback"] = df["trans_date_y"].dt.strftime("%Y-%m")

    # Compute approved transactions per month and country
    df1 = (
        df[df["state"] == "approved"]
        .groupby(["month_transaction", "country"], as_index=False)
        .agg(
            approved_count=("amount", "count"),
            approved_amount=("amount", "sum"),
        )
        .rename(columns={"month_transaction": "month"})
    )

    # Compute chargebacks per month and country
    df2 = (
        df.groupby(["month_chargeback", "country"], as_index=False)
        .agg(
            chargeback_count=("amount", "count"),
            chargeback_amount=("amount", "sum"),
        )
        .rename(columns={"month_chargeback": "month"})
    )

    # Merge both tables and fill missing values with zero
    df3 = df1.merge(df2, how="outer", on=["month", "country"]).fillna(0)

    return df3


def main():
    # Example data for Transactions table
    transactions_data = {
        "id": [101, 102, 103, 104, 105],
        "country": ["US", "US", "US", "US", "US"],
        "state": ["approved", "declined", "approved", "declined", "approved"],
        "amount": [1000, 2000, 3000, 4000, 5000],
        "trans_date": pd.to_datetime(
            ["2019-05-18", "2019-05-19", "2019-06-10", "2019-06-13", "2019-06-15"]
        ),
    }
    transactions = pd.DataFrame(transactions_data)

    # Example data for Chargebacks table
    chargebacks_data = {
        "trans_id": [102, 101, 105],
        "trans_date": pd.to_datetime(["2019-05-29", "2019-06-30", "2019-09-18"]),
    }
    chargebacks = pd.DataFrame(chargebacks_data)

    # Compute and display the result
    result = monthly_transactions(transactions, chargebacks)
    print(result)


if __name__ == "__main__":
    main()
