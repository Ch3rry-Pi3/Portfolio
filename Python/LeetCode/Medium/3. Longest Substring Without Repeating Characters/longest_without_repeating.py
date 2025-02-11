class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.
        """

        n = len(s)
        ans = 0  # Stores the maximum length of substring without repeating characters
        char_to_next_index = {}         # Dictionary to store the next index of each character

        i = 0  # Left pointer of the sliding window

        # Iterate through the string using the right pointer (j)
        for j in range(n):
            # If the character is already in the dictionary, update left pointer
            if s[j] in char_to_next_index:
                i = max(char_to_next_index[s[j]], i)

            # Update the maximum length found so far
            ans = max(ans, j - i + 1)

            # Store the next index of the character
            char_to_next_index[s[j]] = j + 1

        return ans


def main():
    """Runs example test cases for the function."""
    solution = Solution()

    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("abcdef", 6),
        ("dvdf", 3),
    ]

    for s, expected in test_cases:
        result = solution.lengthOfLongestSubstring(s)
        print(f"Input: {s} → Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    main()
