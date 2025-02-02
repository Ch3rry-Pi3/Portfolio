from typing import List

class Solution:
    """
    This class provides a method to find the greatest common divisor (GCD) of two strings.
    """

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Determines the greatest common divisor (GCD) of two strings.

        A string X is considered a divisor of string Y if Y can be formed by repeating X multiple times.
        The function finds the longest possible string that divides both str1 and str2.

        :param str1: First input string.
        :param str2: Second input string.
        :return: The longest common divisor string.
        """

        length1, length2 = len(str1), len(str2)

        def is_divisor(length: int) -> bool:
            """
            Checks if a substring of the given length can be a divisor of both strings.

            :param length: The length of the potential divisor.
            :return: True if it is a valid divisor, False otherwise.
            """
            # If length is not a factor of both string lengths, return False immediately
            if length1 % length or length2 % length:
                return False

            # Determine how many times the substring must repeat to form each string
            factor1, factor2 = length1 // length, length2 // length

            # Check if repeating the substring forms both str1 and str2
            return str1[:length] * factor1 == str1 and str1[:length] * factor2 == str2

        # Iterate from the longest possible divisor to 1
        for length in range(min(length1, length2), 0, -1):
            if is_divisor(length):
                return str1[:length]

        return ""


def main():
    """
    Demonstrates testing the gcdOfStrings function with sample test cases.
    """
    solver = Solution()

    test_cases = [
        ("ABCABC", "ABC"),          # Expected: "ABC"
        ("ABABAB", "ABAB"),         # Expected: "AB"
        ("LEET", "CODE"),           # Expected: ""
        ("ABCDEF", "ABC"),          # Expected: ""
    ]

    for str1, str2 in test_cases:
        print(f"Input: str1 = {str1}, str2 = {str2}")
        result = solver.gcdOfStrings(str1, str2)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
