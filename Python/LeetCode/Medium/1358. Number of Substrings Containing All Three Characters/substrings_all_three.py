from typing import List

class Solution:
    """
    LeetCode 1358: Number of Substrings Containing All Three Characters

    This class provides a method to count the number of substrings that contain
    at least one occurrence of the characters 'a', 'b', and 'c'.
    """

    def numberOfSubstrings(self, s: str) -> int:
        """
        Counts the number of substrings containing at least one occurrence of 'a', 'b', and 'c'.

        :param s: str - The input string consisting only of 'a', 'b', and 'c'.
        :return: int - The number of valid substrings.
        """
        # Track last seen positions of 'a', 'b', and 'c'
        last_pos = [-1] * 3
        total = 0

        for pos in range(len(s)):
            # Update last seen position for current character
            last_pos[ord(s[pos]) - ord("a")] = pos

            # Calculate valid substrings ending at this position
            # If any character is missing, min(last_pos) will be -1
            # Otherwise, min(last_pos) gives the leftmost required character position
            total += 1 + min(last_pos)

        return total


def main():
    """
    Runs sample test cases for the numberOfSubstrings function.
    """
    solution = Solution()

    # Sample test cases
    test_cases = [
        "abcabc",           # Expected output: 10
        "aaacb",            # Expected output: 3
        "abc",              # Expected output: 1
        "ababab",           # Expected output: 0
    ]

    for s in test_cases:
        print(f"Input: {s} → Output: {solution.numberOfSubstrings(s)}")


if __name__ == "__main__":
    main()
