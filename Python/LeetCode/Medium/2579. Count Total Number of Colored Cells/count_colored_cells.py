class Solution:
    """
    Solution to count the total number of colored cells in an infinite 2D grid after n minutes.
    """

    def coloredCells(self, n: int) -> int:
        """
        Computes the number of colored cells after n minutes.

        :param n: int - The number of minutes.
        :return: int - The total number of colored cells.
        """
        return 1 + 4 * n * (n - 1) // 2


def main():
    """
    Main function to test the coloredCells method with sample test cases.
    """
    solution = Solution()
    
    # Sample test cases
    test_cases = [1, 2, 3, 4, 5, 10]

    for n in test_cases:
        print(f"Input: {n} → Output: {solution.coloredCells(n)}")


if __name__ == "__main__":
    main()