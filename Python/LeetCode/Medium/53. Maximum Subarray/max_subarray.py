from typing import List

class Solution:
    """
    This class provides an implementation of the 'Maximum Subarray' problem 
    using Kadane’s Algorithm, which runs in O(n) time complexity.
    """

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the contiguous subarray with the largest sum.

        :param nums: List of integers
        :return: Maximum sum of any contiguous subarray
        """
        maxSub = nums[0]    # Stores the maximum subarray sum found
        currentSum = 0      # Tracks the running sum of the current subarray

        for n in nums:
            if currentSum < 0:
                currentSum = 0  # Reset current sum if it becomes negative
            currentSum += n
            maxSub = max(maxSub, currentSum)  # Update max sum found
        
        return maxSub


def main():
    """
    Demonstrates finding the maximum subarray sum for multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],  # Expected output: 6
        [1],                              # Expected output: 1
        [5, 4, -1, 7, 8],                 # Expected output: 23
        [-1, -2, -3, -4],                 # Expected output: -1 (single largest negative)
        [8, -19, 5, -4, 20],              # Expected output: 21
    ]

    for nums in test_cases:
        print(f"nums = {nums}")
        result = solver.maxSubArray(nums)
        print(f"Maximum Subarray Sum: {result}\n")


if __name__ == "__main__":
    main()
