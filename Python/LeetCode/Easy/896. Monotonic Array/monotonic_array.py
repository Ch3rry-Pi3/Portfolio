from typing import List

class Solution:
    """
    This class provides an implementation of the 'Monotonic Array' problem.

    The function `isMonotonic` checks whether a given array is monotonic,
    meaning it is either entirely non-increasing or non-decreasing.
    """

    def isMonotonic(self, nums: List[int]) -> bool:
        """
        Determines if the given array is monotonic.

        :param nums: List of integers.
        :return: `True` if `nums` is monotonic, otherwise `False`.
        """
        # Reverse the list if it is decreasing
        if nums[-1] - nums[0] < 0:
            nums.reverse()

        # Check if the array is non-decreasing
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:           # A decreasing pair breaks monotonicity
                return False

        return True                             # If no violations were found, the array is monotonic


def main():
    """
    Demonstrates testing the isMonotonic function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [1, 2, 2, 3],           # Expected: True (Monotonic increasing)
        [6, 5, 4, 4],           # Expected: True (Monotonic decreasing)
        [1, 3, 2],              # Expected: False (Not monotonic)
        [1, 1, 1, 1],           # Expected: True (All elements are the same)
        [10, 20, 30],           # Expected: True (Strictly increasing)
        [30, 20, 10],           # Expected: True (Strictly decreasing)
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        result = solver.isMonotonic(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
