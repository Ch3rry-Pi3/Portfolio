class Solution:
    """
    This class provides an implementation of the 'Roman to Integer' problem.

    The function `romanToInt` converts a given Roman numeral string into an integer.
    """

    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral string to an integer.

        :param s: A string representing a Roman numeral.
        :return: Integer equivalent of the Roman numeral.
        """
        roman = {
            "I": 1, "V": 5, "X": 10, "L": 50, 
            "C": 100, "D": 500, "M": 1000
        }

        result = 0  # Stores the final integer result

        # Traverse the string, checking if subtraction is needed
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]  # Subtract when a smaller numeral appears before a larger one
            else:
                result += roman[s[i]]  # Otherwise, add the numeral value

        return result


def main():
    """
    Demonstrates testing the romanToInt function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        "III",     # Expected: 3 (1 + 1 + 1)
        "IV",      # Expected: 4 (5 - 1)
        "IX",      # Expected: 9 (10 - 1)
        "LVIII",   # Expected: 58 (50 + 5 + 1 + 1 + 1)
        "MCMXCIV", # Expected: 1994 (1000 + 900 + 90 + 4)
    ]

    for s in test_cases:
        print(f"Input: \"{s}\"")
        result = solver.romanToInt(s)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
