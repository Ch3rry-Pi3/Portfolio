from typing import List

class Solution:
    """
    This class provides a method to determine the length of the longest strictly increasing subsequence in a list.
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Computes the length of the longest increasing subsequence (LIS) in the given list.

        The LIS is a subsequence where elements are strictly increasing, and the goal is to find the maximum length.

        :param nums: List of integers representing the sequence.
        :return: Length of the longest increasing subsequence.
        """
        
        # Edge case: If the list is empty, return 0
        if not nums:
            return 0

        # Initialise a DP array where each index starts with a subsequence length of 1
        lis = [1] * len(nums)

        # Iterate from the last element towards the beginning
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):           # Compare with elements ahead
                if nums[i] < nums[j]:  
                    # Update the LIS length at index i based on future values
                    lis[i] = max(lis[i], 1 + lis[j])

        # Return the maximum value from the LIS array
        return max(lis)


def main():
    """
    Demonstrates testing the lengthOfLIS function with sample test cases.
    """
    solver = Solution()

    test_cases = [
        [10, 9, 2, 5, 3, 7, 101, 18],       # Expected: 4
        [0, 1, 0, 3, 2, 3],                 # Expected: 4
        [7, 7, 7, 7, 7, 7, 7],              # Expected: 1
        [1, 2, 3, 4, 5],                    # Expected: 5
        [5, 4, 3, 2, 1],                    # Expected: 1
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        result = solver.lengthOfLIS(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
