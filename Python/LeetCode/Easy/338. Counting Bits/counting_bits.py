from typing import List

class Solution:
    """
    This class provides an implementation of the 'Counting Bits' problem.

    The goal is to return an array where each index `i` contains the number of `1`s
    in the binary representation of `i`. This is solved efficiently using **dynamic programming (DP)**.
    """

    def countBits(self, n: int) -> List[int]:
        """
        Computes the number of `1` bits for each number from 0 to `n`.

        :param n: Integer representing the upper limit
        :return: List containing the count of 1 bits for each number in range [0, n]
        """
        dp = [0] * (n + 1)      # Initialise DP array with zeros
        offset = 1              # Offset tracks the most significant power of 2

        for i in range(1, n + 1):
            if offset * 2 == i:         # When `i` reaches a new power of 2, update offset
                offset = i

            dp[i] = 1 + dp[i - offset]  # Use DP relation: dp[i] = 1 + dp[i - offset]

        return dp


def main():
    """
    Demonstrates testing the countBits function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [2, 5, 10]

    for num in test_cases:
        print(f"Input: {num}")
        result = solver.countBits(num)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
