from typing import List

class Solution:
    """
    This class provides a method to determine the minimum number of coins needed to make up a given amount.
    """
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Determines the minimum number of coins required to make up the given amount.

        :param coins: List of available coin denominations.
        :param amount: The target amount to be formed.
        :return: Minimum number of coins needed, or -1 if it's not possible.
        """
        
        # Initialise DP array with an impossible large value (amount + 1) to represent unreachable states.
        dp = [amount + 1] * (amount + 1)    # e.g., amount = 5 -> [6, 6, 6, 6, 6, 6]
        dp[0] = 0                           # Base case: 0 coins needed to make amount 0 -> [0, 6, 6, 6, 6, 6]

        # Iterate through all amounts from 1 to the target amount
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    # Update the dp table by considering the minimum coins required
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # If dp[amount] is still the initialised value, return -1 indicating no solution
        return dp[amount] if dp[amount] != amount + 1 else -1


def main():
    """
    Demonstrates testing the coinChange function with sample test cases.
    """
    solver = Solution()

    test_cases = [
        ([1, 2, 5], 11),   # Expected: 3 (5 + 5 + 1)
        ([2], 3),          # Expected: -1 (Not possible)
        ([1], 0),          # Expected: 0 (No coins needed)
        ([1, 2, 5], 7),    # Expected: 2 (5 + 2)
    ]

    for coins, amount in test_cases:
        print(f"Input: coins = {coins}, amount = {amount}")
        result = solver.coinChange(coins, amount)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
