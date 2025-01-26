from typing import List

class Solution:
    """
    This class provides an implementation of the maximum profit problem,
    where we find the best time to buy and sell stock to maximise profit.
    """

    def maxProfit(self, prices: List[int]) -> int:
        """
        Finds the maximum profit that can be achieved from buying and selling stock.

        :param prices: List of stock prices
        :return: Maximum possible profit
        """
        left, right = 0, 1  # left = buy, right = sell
        maxProfit = 0

        while right < len(prices):
            # Check if it's profitable
            if prices[left] < prices[right]:
                # Calculate profit
                profit = prices[right] - prices[left]
                # Update maxProfit
                maxProfit = max(maxProfit, profit) 

            else:
                # Move left pointer to right pointer's position
                left = right  # Move buy pointer to current sell position

            # Move right pointer forward
            right += 1

        return maxProfit


def main():
    """
    Demonstrates finding the maximum profit from stock prices.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [7, 1, 5, 3, 6, 4],     # Expected output: 5
        [7, 6, 4, 3, 1],        # Expected output: 0 (no profit)
        [2, 4, 1],              # Expected output: 2
        [3, 2, 6, 5, 0, 3]      # Expected output: 4
    ]

    for prices in test_cases:
        print(f"Stock prices: {prices}")
        result = solver.maxProfit(prices)
        print(f"Maximum Profit: {result}\n")


if __name__ == "__main__":
    main()
