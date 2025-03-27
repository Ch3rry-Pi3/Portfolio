from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        """
        Return the minimum number of operations required to make all elements equal in the grid.
        Each operation can add or subtract x from any element.

        Args:
        grid (List[List[int]]): 2D list of integers representing the grid.
        x (int): The fixed amount that can be added or subtracted.

        Returns:
        int: Minimum number of operations, or -1 if impossible.
        """
        # Flatten the 2D grid into a 1D list
        nums_array = [num for row in grid for num in row]
        nums_array.sort()

        # Choose the median as the target value for minimum operations
        target = nums_array[len(nums_array) // 2]
        result = 0

        for number in nums_array:
            if (number - target) % x != 0:
                return -1  # Not possible to reach target uniformly
            result += abs(number - target) // x

        return result


def main():
    solution = Solution()

    test_cases = [
        ([[2, 4], [6, 8]], 2),     # Output: 4
        ([[1, 5], [2, 3]], 1),     # Output: 5
        ([[1, 2], [3, 4]], 2),     # Output: -1
        ([[1, 1, 1], [1, 1, 1]], 1),  # Output: 0
    ]

    for grid, x in test_cases:
        print(f"Grid: {grid}, x: {x} -> Output: {solution.minOperations(grid, x)}")


if __name__ == "__main__":
    main()
