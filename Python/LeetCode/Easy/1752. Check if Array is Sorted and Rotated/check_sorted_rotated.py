from typing import List

class Solution:
    """
    This class provides an implementation of the 'Check if Array Is Sorted and Rotated' problem.

    The function `check` determines whether a given array was originally sorted in 
    non-decreasing order and then rotated some number of positions (including zero).

    The method checks if there exists a way to rotate the array back to a sorted sequence.
    """

    def check(self, nums: List[int]) -> bool:
        """
        Determines whether the given array is a rotated version of a sorted array.

        :param nums: List of integers.
        :return: `True` if the array is sorted and rotated, otherwise `False`.
        """
        N = len(nums)
        count = 1                   # Keeps track of consecutive non-decreasing elements

        # Iterate through the array in a circular manner (2 * N iterations to check all rotations)
        for i in range(1, 2 * N):
            if nums[(i - 1) % N] <= nums[i % N]:  
                count += 1          # Maintain increasing order
            else:
                count = 1           # Reset count if order breaks

            if count == N:          # If we found a full cycle maintaining order
                return True
        
        return N == 1               # Single-element arrays are trivially sorted and rotated


def main():
    """
    Demonstrates testing the check function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [3, 4, 5, 1, 2],  # Expected: True
        [2, 1, 3, 4],     # Expected: False
        [1, 2, 3],        # Expected: True
        [6, 10, 6],       # Expected: True (Duplicate elements allowed)
        [1],              # Expected: True (Single element is always sorted)
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        result = solver.check(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
