from typing import List

class Solution:
    """
    This class provides an implementation of the 'To Lower Case' problem.

    The function `toLowerCase` converts all uppercase letters in a string to lowercase 
    without using the built-in `lower()` function.
    """

    def toLowerCase(self, s: str) -> str:
        """
        Converts all uppercase letters in the given string to lowercase.

        :param s: Input string containing uppercase and lowercase letters.
        :return: Lowercase version of the input string.
        """
        is_upper = lambda x: 'A' <= x <= 'Z'            # Checks if a character is uppercase
        to_lower = lambda x: chr(ord(x) + 32)           # Converts an uppercase letter to lowercase

        # Convert uppercase letters while keeping other characters unchanged
        return ''.join([to_lower(x) if is_upper(x) else x for x in s])


def main():
    """
    Demonstrates testing the toLowerCase function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        "Hello",            # Expected: "hello"
        "here",             # Expected: "here"
        "LOVELY",           # Expected: "lovely"
        "Python3",          # Expected: "python3"
        "123ABC!",          # Expected: "123abc!"
    ]

    for s in test_cases:
        print(f"Input: {s}")
        result = solver.toLowerCase(s)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
