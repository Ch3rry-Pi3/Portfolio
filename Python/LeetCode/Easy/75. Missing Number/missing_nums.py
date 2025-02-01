from typing import List

class Solution:
    """
    This class provides an implementation of the 'Missing Number' problem.

    The goal is to find the missing number in a sequence from 0 to `n` in an array that contains
    `n` distinct numbers.
    """

    def missingNumber(self, nums: List[int]) -> int:
        """
        Finds the missing number in the range [0, n] using a mathematical sum approach.

        :param nums: List of distinct numbers from the range [0, n]
        :return: The missing number in the sequence
        """
        result = len(nums)              # Initialise result as n (one value missing)

        for i in range(len(nums)):
            result += (i - nums[i])     # Adjust sum by adding index and subtracting value

        return result


def main():
    """
    Demonstrates testing the missingNumber function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [3, 0, 1],                      # Missing number = 2
        [0, 1],                         # Missing number = 2
        [9, 6, 4, 2, 3, 5, 7, 0, 1],    # Missing number = 8
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        result = solver.missingNumber(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
