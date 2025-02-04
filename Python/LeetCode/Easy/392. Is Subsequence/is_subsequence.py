class Solution:
    """
    This class provides an implementation of the 'Is Subsequence' problem.

    The function `isSubsequence` checks whether string `s` is a subsequence of string `t`.
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Determines if `s` is a subsequence of `t`.

        :param s: The string to check as a subsequence.
        :param t: The target string.
        :return: `True` if `s` is a subsequence of `t`, otherwise `False`.
        """
        pointer_s = pointer_t = 0  # Initialise two pointers

        # Traverse `t` while checking for characters in `s`
        while pointer_s < len(s) and pointer_t < len(t):
            if s[pointer_s] == t[pointer_t]:                    # If characters match, move `s` pointer
                pointer_s += 1
            pointer_t += 1                                      # Always move `t` pointer

        return pointer_s == len(s)                              # `s` must be fully matched to be a subsequence


def main():
    """
    Demonstrates testing the isSubsequence function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        ("abc", "ahbgdc"),          # Expected: True
        ("axc", "ahbgdc"),          # Expected: False
        ("", "ahbgdc"),             # Expected: True (empty string is a subsequence of any string)
        ("b", "abc"),               # Expected: True
        ("abcdef", "abcdef"),       # Expected: True (identical strings)
        ("abc", "acb"),             # Expected: False (order matters)
    ]

    for s, t in test_cases:
        print(f"Input: s = \"{s}\", t = \"{t}\"")
        result = solver.isSubsequence(s, t)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
