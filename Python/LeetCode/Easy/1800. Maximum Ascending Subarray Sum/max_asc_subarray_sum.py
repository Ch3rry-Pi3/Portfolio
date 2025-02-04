from typing import List

class Solution:
    """
    This class provides an implementation of the 'Maximum Ascending Subarray Sum' problem.

    The function `maxAscendingSum` finds the maximum possible sum of an ascending subarray in `nums`.
    """

    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        Determines the maximum sum of a contiguous ascending subarray.

        :param nums: List of positive integers.
        :return: The maximum sum of any strictly increasing subarray.
        """
        current = nums[0]                   # Initialise current subarray sum
        result = current                    # Initialise maximum found sum

        # Iterate through the array, tracking ascending subarrays
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:       # Continue ascending subarray
                current += nums[i]
            else:                           # Reset sum if order breaks
                current = nums[i]

            result = max(result, current)   # Update max sum found

        return result


def main():
    """
    Demonstrates testing the maxAscendingSum function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [10, 20, 30, 5, 10, 50],            # Expected: 65
        [10, 20, 30, 40, 50],               # Expected: 150
        [12, 17, 15, 13, 10, 11, 12],       # Expected: 33
        [5, 5, 5, 5],                       # Expected: 5 (no increasing subarray)
        [1, 2, 3, 4, 5, 6],                 # Expected: 21 (entire array is ascending)
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        result = solver.maxAscendingSum(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
