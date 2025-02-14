from typing import List

class Solution:
    """
    A class to find the longest common prefix among an array of strings.
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix in a list of strings.

        Args:
            strs (List[str]): A list of strings.

        Returns:
            str: The longest common prefix. If there is no common prefix, returns an empty string.
        """
        # Edge case: If the list is empty, return an empty string
        if not strs:
            return ""

        # Find the minimum length of all strings in the list
        min_length = min(len(s) for s in strs)

        # Iterate character by character up to the minimum length found
        for i in range(min_length):
            # Compare the character at position 'i' across all strings
            if any(s[i] != strs[0][i] for s in strs):
                return strs[0][:i]

        # If we complete the loop, return the full prefix up to 'min_length'
        return strs[0][:min_length]


def main():
    """Example usage of the `longestCommonPrefix` function."""

    solution = Solution()

    # Example test cases
    test_cases = [
        (["flower", "flow", "flight"], "fl"),                               # Expected output: "fl"
        (["dog", "racecar", "car"], ""),                                    # Expected output: ""
        (["interspecies", "interstellar", "interstate"], "inters"),         # Expected output: "inters"
        (["a"], "a"),                                                       # Expected output: "a"
        (["abc", "abc", "abc"], "abc"),                                     # Expected output: "abc"
    ]

    for strs, expected in test_cases:
        result = solution.longestCommonPrefix(strs)
        print(f"Input: {strs} → Longest Common Prefix: {result} (Expected: {expected})")


if __name__ == "__main__":
    main()
