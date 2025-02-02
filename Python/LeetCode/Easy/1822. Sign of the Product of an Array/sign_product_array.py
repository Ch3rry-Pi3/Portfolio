from typing import List

class Solution:
    """
    This class provides an implementation of the 'Sign of the Product of an Array' problem.
    
    The `arraySign` method determines the sign of the product of an integer array without
    computing the product explicitly.
    """

    def arraySign(self, nums: List[int]) -> int:
        """
        Determines the sign of the product of all elements in the array.

        :param nums: List of integers.
        :return: 
            - 1 if the product is positive.
            - -1 if the product is negative.
            - 0 if the product is zero.
        """
        negatives = 0                               # Count of negative numbers

        for n in nums:
            if n == 0:                              # If any number is zero, the product is zero
                return 0
            negatives += (1 if n < 0 else 0)        # Count negative numbers

        return -1 if negatives % 2 else 1           # Even negatives = positive, odd negatives = negative


def main():
    """
    Demonstrates testing the arraySign function on multiple test cases.
    """
    solver = Solution()

    test_cases = [
        ([-1, -2, -3, -4, 3, 2, 1], 1),   # Product is positive (144)
        ([1, 5, 0, 2, -3], 0),            # Product is zero
        ([-1, 1, -1, 1, -1], -1)          # Product is negative (-1)
    ]

    for nums, expected in test_cases:
        result = solver.arraySign(nums)
        print(f"Input: {nums} -> Output: {result} | Expected: {expected}")


if __name__ == "__main__":
    main()
