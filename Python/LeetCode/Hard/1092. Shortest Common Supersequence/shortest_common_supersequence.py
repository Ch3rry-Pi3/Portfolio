class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        Finds the shortest string that has both str1 and str2 as subsequences.

        :param str1: First input string.
        :param str2: Second input string.
        :return: Shortest common supersequence string.
        """
        str1_length = len(str1)
        str2_length = len(str2)

        # Initialise DP table for storing the length of the shortest supersequence
        dp = [[0 for _ in range(str2_length + 1)] for _ in range(str1_length + 1)]

        # Base cases: when one of the strings is empty
        for row in range(str1_length + 1):
            dp[row][0] = row  # If str2 is empty, use only str1 characters

        for col in range(str2_length + 1):
            dp[0][col] = col  # If str1 is empty, use only str2 characters

        # Fill DP table using bottom-up approach
        for row in range(1, str1_length + 1):
            for col in range(1, str2_length + 1):
                if str1[row - 1] == str2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1  # Matching character
                else:
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1  # Take min +1

        # Backtracking to construct the shortest common supersequence
        super_sequence = []
        row, col = str1_length, str2_length

        while row > 0 and col > 0:
            if str1[row - 1] == str2[col - 1]:
                super_sequence.append(str1[row - 1])  # Matching character
                row -= 1
                col -= 1
            elif dp[row - 1][col] < dp[row][col - 1]:
                super_sequence.append(str1[row - 1])  # Take character from str1
                row -= 1
            else:
                super_sequence.append(str2[col - 1])  # Take character from str2
                col -= 1

        # Append remaining characters if any
        while row > 0:
            super_sequence.append(str1[row - 1])
            row -= 1

        while col > 0:
            super_sequence.append(str2[col - 1])
            col -= 1

        # Reverse to get the correct order
        return "".join(super_sequence[::-1])


# Main function for testing
def main():
    solution = Solution()

    # Test cases
    test_cases = [("abac", "cab"), ("aaaaaaaa", "aaaaaaa"), ("geek", "eke")]

    for str1, str2 in test_cases:
        result = solution.shortestCommonSupersequence(str1, str2)
        print(f"Shortest common supersequence of '{str1}' and '{str2}' is: '{result}'")


if __name__ == "__main__":
    main()
