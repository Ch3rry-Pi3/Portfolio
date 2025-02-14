class Solution:
    def repeatedCharacter(self, s: str) -> str:
        """
        Finds the first letter in the given string `s` that appears twice.

        Args:
            s (str): Input string containing only lowercase English letters.

        Returns:
            str: The first letter that appears twice.
        """

        seen_letters = set()

        for char in s:
            if char in seen_letters:
                return char
            seen_letters.add(char)

        return ""  # This case won't occur as per the problem statement.
        

def main():
    """Example usage of the `repeatedCharacter` function."""
    
    solution = Solution()
    
    # Example test cases
    test_cases = ["abccbaacz", "abcdd", "aabbcc", "abcdef"]

    for test in test_cases:
        print(f"Input: '{test}' → First repeated letter: '{solution.repeatedCharacter(test)}'")

if __name__ == "__main__":
    main()
