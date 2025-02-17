import pandas as pd
import numpy as np

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the capital gain or loss for each stock based on buy and sell transactions.

    Args:
        stocks (pd.DataFrame): A DataFrame containing stock transaction details with columns:
                               - "stock_name" (str): Name of the stock.
                               - "operation" (str): "Buy" or "Sell".
                               - "operation_day" (int): Day of the transaction.
                               - "price" (int): Price of the transaction.

    Returns:
        pd.DataFrame: A DataFrame with columns:
                      - "stock_name" (str): Name of the stock.
                      - "capital_gain_loss" (int): Net gain or loss after transactions.
    """
    return (
        stocks
        .sort_values(by=["stock_name", "operation_day"])                                            # Sort transactions for correct order
        .assign(price=lambda x: np.where(x["operation"] == "Buy", -x["price"], x["price"]))         # Convert "Buy" to negative
        .groupby("stock_name", as_index=False)                                                      # Group by stock
        .agg(capital_gain_loss=("price", "sum"))                                                    # Sum up gains and losses
    )

def main():
    """
    Main function to test the capital_gainloss function with the provided example data.
    """
    # Example input data
    data = {
        "stock_name": [
            "Leetcode", "Corona Masks", "Leetcode", "Handbags",
            "Corona Masks", "Corona Masks", "Corona Masks",
            "Handbags", "Handbags"
        ],
        "operation": [
            "Buy", "Buy", "Sell", "Buy",
            "Sell", "Buy", "Sell",
            "Sell", "Sell"
        ],
        "operation_day": [1, 2, 5, 17, 3, 4, 5, 29, 10],
        "price": [1000, 10, 9000, 30000, 1010, 1000, 500, 7000, 10000]
    }

    # Create a DataFrame
    stocks_df = pd.DataFrame(data)

    # Compute capital gains and losses
    result = capital_gainloss(stocks_df)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()
