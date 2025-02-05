class Solution:
    """
    This class provides an implementation of the 'Check if One String Swap Can Make Strings Equal' problem.

    The function `areAlmostEqual` checks whether two strings can be made equal
    by performing at most one swap on exactly one of the strings.
    """

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Determines if two strings can be made equal with at most one swap.

        :param s1: First input string.
        :param s2: Second input string.
        :return: `True` if one swap can make the strings equal, otherwise `False`.
        """
        indexes = []                    # Stores indices where s1 and s2 differ

        # Identify indices where characters differ
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indexes.append(i)
            if len(indexes) > 2:        # More than two mismatches mean swap can't fix it
                return False

        # If exactly two indices differ, check if swapping makes them equal
        if len(indexes) == 2:
            i, j = indexes
            return s1[i] == s2[j] and s1[j] == s2[i]

        # If no differences exist, the strings are already equal
        return len(indexes) == 0


def main():
    """
    Demonstrates testing the areAlmostEqual function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        ("bank", "kanb"),           # Expected: True (swap 'b' and 'k')
        ("attack", "defend"),       # Expected: False (too many differences)
        ("kelb", "kelb"),           # Expected: True (strings are already equal)
        ("abcd", "abdc"),           # Expected: True (swap 'c' and 'd')
        ("abcd", "abcd"),           # Expected: True (already equal)
        ("abc", "def"),             # Expected: False (completely different)
    ]

    for s1, s2 in test_cases:
        print(f"Input: s1 = \"{s1}\", s2 = \"{s2}\"")
        result = solver.areAlmostEqual(s1, s2)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
