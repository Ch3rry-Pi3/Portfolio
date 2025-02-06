class Solution:
    """
    This class provides an implementation of the 'Length of Last Word' problem.

    The function `lengthOfLastWord` returns the length of the last word in a given string.
    A word is defined as a maximal substring consisting of non-space characters only.
    """

    def lengthOfLastWord(self, s: str) -> int:
        """
        Determines the length of the last word in a string.

        :param s: A string containing words and spaces.
        :return: Length of the last word in the string.
        """
        i, length = len(s) - 1, 0

        # Ignore trailing spaces at the end of the string
        while i >= 0 and s[i] == " ":
            i -= 1
        
        # Count characters until a space or the start of the string is reached
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        
        return length


def main():
    """
    Demonstrates testing the lengthOfLastWord function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        "Hello World",                          # Expected: 5 ("World")
        "   fly me   to   the moon  ",          # Expected: 4 ("moon")
        "luffy is still joyboy",                # Expected: 6 ("joyboy")
        "Python",                               # Expected: 6 ("Python")
        "  spaces ",                            # Expected: 6 ("spaces")
        "   ",                                  # Expected: 0 (No words)
    ]

    for s in test_cases:
        print(f"Input: \"{s}\"")
        result = solver.lengthOfLastWord(s)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
