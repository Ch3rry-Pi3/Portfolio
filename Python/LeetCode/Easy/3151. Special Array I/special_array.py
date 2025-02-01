from typing import List

class Solution:
    """
    This class provides an implementation of the 'Special Array I' problem.

    An array is considered **special** if every pair of adjacent elements 
    contains two numbers with different parity (one even, one odd).
    
    The method `isArraySpecial` checks if a given list of integers meets 
    this condition and returns `True` if it does, otherwise `False`.
    """

    def isArraySpecial(self, nums: List[int]) -> bool:
        """
        Determines whether the given array is special.

        :param nums: List of integers to check.
        :return: `True` if the array is special, otherwise `False`.
        """
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:  # If adjacent numbers have the same parity
                return False
        
        return True


def main():
    """
    Demonstrates testing the isArraySpecial function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [1],             # Expected: True
        [2, 1, 4],       # Expected: True
        [4, 3, 1, 6]     # Expected: False
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        result = solver.isArraySpecial(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
