from typing import List

class Solution:
    """
    This class provides an implementation of the 'Reverse String' problem.

    The function `reverseString` reverses a given array of characters in-place, ensuring O(1) extra memory usage.
    """

    def reverseString(self, s: List[str]) -> None:
        """
        Reverses the given list of characters in-place.

        :param s: List of characters representing a string.
        :return: None (modifies `s` in-place).
        """
        left, right = 0, len(s) - 1                     # Initialise two pointers

        # Swap characters while the left index is less than the right index
        while left < right:
            s[left], s[right] = s[right], s[left]       # Swap characters
            left, right = left + 1, right - 1           # Move pointers inward


def main():
    """
    Demonstrates testing the reverseString function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        ["h", "e", "l", "l", "o"],                      # Expected: ["o", "l", "l", "e", "h"]
        ["H", "a", "n", "n", "a", "h"],                 # Expected: ["h", "a", "n", "n", "a", "H"]
        ["A", "B", "C", "D"],                           # Expected: ["D", "C", "B", "A"]
        ["a"],                                          # Expected: ["a"] (single character remains the same)
        [],                                             # Expected: [] (empty list remains empty)
    ]

    for s in test_cases:
        print(f"Input: {s}")
        solver.reverseString(s)
        print(f"Output: {s}\n")                         # Since it's modified in-place


if __name__ == "__main__":
    main()
