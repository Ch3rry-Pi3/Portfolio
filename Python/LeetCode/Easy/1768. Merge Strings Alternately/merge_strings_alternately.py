from typing import List

class Solution:
    """
    This class provides an implementation of merging two strings alternately.
    
    Given two strings, `word1` and `word2`, the function merges them by alternating 
    characters from each string. If one string is longer, the remaining characters 
    are appended to the end of the merged string.
    """

    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merges two strings alternately, starting with word1.

        :param word1: First string
        :param word2: Second string
        :return: Merged string
        """
        i, j = 0, 0                     # Pointers for word1 and word2
        result = []                     # List to store merged characters

        # Merge characters from both strings alternately
        while i < len(word1) and j < len(word2):
            result.append(word1[i])     # Append from word1
            result.append(word2[j])     # Append from word2
            i += 1
            j += 1

        # Append remaining characters from the longer string
        result.append(word1[i:])        # Remaining part of word1
        result.append(word2[j:])        # Remaining part of word2

        return "".join(result)          # Convert list to string


def main():
    """
    Demonstrates testing the mergeAlternately function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        ("abc", "pqr"),                 # Expected: "apbqcr"
        ("ab", "pqrs"),                 # Expected: "apbqrs"
        ("abcd", "pq"),                 # Expected: "apbqcd"
    ]

    for word1, word2 in test_cases:
        print(f"Input: word1 = {word1}, word2 = {word2}")
        result = solver.mergeAlternately(word1, word2)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
