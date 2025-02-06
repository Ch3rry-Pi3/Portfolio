from typing import List

class Solution:
    """
    This class provides an implementation of the 'Word Break' problem.

    The function `wordBreak` determines if a given string `s` can be segmented 
    into words found in a given dictionary using dynamic programming.
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Determines if the string `s` can be segmented into words from `wordDict`.

        :param s: Input string.
        :param wordDict: List of valid words.
        :return: True if `s` can be segmented using words from `wordDict`, otherwise False.
        """
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True                           # Base case: An empty substring is always a valid segmentation

        # Iterate backwards through the string
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]          # If the suffix is valid, mark dp[i] as True
                if dp[i]:                           # If we found a valid segmentation, no need to check further
                    break

        return dp[0]  # The result is stored at the beginning of the DP array


def main():
    """
    Demonstrates testing the wordBreak function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        ("leetcode", ["leet", "code"]),                             # Expected: True
        ("applepenapple", ["apple", "pen"]),                        # Expected: True
        ("catsandog", ["cats", "dog", "sand", "and", "cat"]),       # Expected: False
        ("aaaaaaa", ["aaa", "aaaa"]),                               # Expected: True
        ("aaaaaaa", ["aa", "aaa"]),                                 # Expected: True
    ]

    for s, wordDict in test_cases:
        print(f"Input: s = \"{s}\", wordDict = {wordDict}")
        result = solver.wordBreak(s, wordDict)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
