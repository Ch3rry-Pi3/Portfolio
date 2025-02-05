from typing import List

class Solution:
    """
    This class provides a method to compute the Longest Common Subsequence (LCS)
    between two strings using dynamic programming.
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Determines the length of the longest common subsequence between two given strings.

        A subsequence is a sequence that appears in the same relative order but not necessarily contiguous.
        The longest common subsequence is the longest sequence that appears in both strings.

        :param text1: First input string.
        :param text2: Second input string.
        :return: Length of the longest common subsequence.
        """

        # Initialise a 2D DP table filled with zeroes.
        # The table has dimensions (len(text1) + 1) x (len(text2) + 1)
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        # Iterate backwards through both strings to build the DP table
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):

                # If characters match, extend the subsequence by 1
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                
                # Otherwise, take the maximum value from previous computed results
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # The top-left cell (dp[0][0]) contains the final result
        return dp[0][0]


def main():
    """
    Demonstrates testing the longestCommonSubsequence function with sample test cases.
    """
    solver = Solution()

    test_cases = [
        ("abcde", "ace"),   # Expected: 3 ("ace")
        ("abc", "abc"),     # Expected: 3 ("abc")
        ("abc", "def"),     # Expected: 0 (No common subsequence)
        ("abcde", "aebdc"), # Expected: 3 ("abc" or "abd")
    ]

    for text1, text2 in test_cases:
        print(f"Input: text1 = '{text1}', text2 = '{text2}'")
        result = solver.longestCommonSubsequence(text1, text2)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
