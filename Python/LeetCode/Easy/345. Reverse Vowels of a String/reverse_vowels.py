class Solution:
    """
    This class provides an implementation of the 'Reverse Vowels of a String' problem.

    The function `reverseVowels` reverses only the vowels in a given string while keeping 
    the other characters in their original positions.
    """

    def reverseVowels(self, s: str) -> str:
        """
        Reverses only the vowels in the input string.

        :param s: Input string containing both vowels and consonants.
        :return: A string where the vowels are reversed, while other characters remain unchanged.
        """
        s = list(s)  # Convert string to a list for in-place modifications
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}         
        left, right = 0, len(s) - 1                         # Two-pointer approach

        # Swap vowels using two pointers
        while left < right:
            if s[left] not in vowels:
                left += 1                                   # Move left pointer forward if it's not a vowel
            elif s[right] not in vowels:
                right -= 1                                  # Move right pointer backward if it's not a vowel
            else:
                s[left], s[right] = s[right], s[left]       # Swap vowels
                left, right = left + 1, right - 1           # Move both pointers

        return "".join(s)                                   # Convert list back to string


def main():
    """
    Demonstrates testing the reverseVowels function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        "IceCreAm",             # Expected: "AceCrEIm"
        "leetcode",             # Expected: "leotcede"
        "hello",                # Expected: "holle"
        "aA",                   # Expected: "Aa"
        "xyz",                  # Expected: "xyz" (no vowels to reverse)
        "AEIOU",                # Expected: "UOIEA" (all vowels reversed)
    ]

    for s in test_cases:
        print(f"Input: \"{s}\"")
        result = solver.reverseVowels(s)
        print(f"Output: \"{result}\"\n")


if __name__ == "__main__":
    main()
