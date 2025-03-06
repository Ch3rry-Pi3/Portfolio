from typing import List

class Solution:
    """
    Solution to find the missing and repeated values in an n x n grid.
    """

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """
        Identifies the missing and repeated values in the n x n grid.

        :param grid: List[List[int]] - The n x n matrix containing numbers in range [1, n²].
        :return: List[int] - A list [repeated, missing].
        """
        n = len(grid)
        freq = {}

        # Count occurrences of each number
        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1

        # Find missing and repeated numbers
        missing, repeat = None, None

        for num in range(1, n * n + 1):
            if num not in freq:
                missing = num
            elif freq[num] == 2:
                repeat = num

        return [repeat, missing]


def main():
    """
    Main function to test the findMissingAndRepeatedValues method with sample test cases.
    """
    solution = Solution()
    
    # Sample test cases
    test_cases = [
        [[1, 3], [2, 2]],                           # Expected output: [2, 4]
        [[9, 1, 7], [8, 9, 2], [3, 4, 6]],          # Expected output: [9, 5]
    ]

    for grid in test_cases:
        print(f"Input: {grid} → Output: {solution.findMissingAndRepeatedValues(grid)}")


if __name__ == "__main__":
    main()
