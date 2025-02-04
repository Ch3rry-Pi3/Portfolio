class Solution:
    """
    This class provides an implementation of the 'Reverse Words in a String' problem.

    The function `reverseWords` takes an input string, removes extra spaces, and returns 
    the words in reverse order, ensuring only a single space separates them.
    """

    def reverseWords(self, s: str) -> str:
        """
        Reverses the order of words in a given string.

        :param s: Input string containing words separated by spaces.
        :return: A string with words reversed and properly spaced.
        """
        s = s.strip()                           # Remove leading and trailing spaces
        words = s.split()                       # Split string into words, automatically handling multiple spaces
        reversed_words = words[::-1]            # Reverse the list of words
        return " ".join(reversed_words)         # Join words with a single space


def main():
    """
    Demonstrates testing the reverseWords function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        "the sky is blue",          # Expected: "blue is sky the"
        "  hello world  ",          # Expected: "world hello"
        "a good   example",         # Expected: "example good a"
        "  multiple   spaces   ",   # Expected: "spaces multiple"
        "one-word",                 # Expected: "one-word"
        "  ",                       # Expected: "" (empty string after trimming)
    ]

    for s in test_cases:
        print(f"Input: \"{s}\"")
        result = solver.reverseWords(s)
        print(f"Output: \"{result}\"\n")


if __name__ == "__main__":
    main()
