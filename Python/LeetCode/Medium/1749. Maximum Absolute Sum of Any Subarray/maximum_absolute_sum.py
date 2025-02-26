from typing import List

class Solution:
    """
    This class provides a solution to find the maximum absolute sum of any subarray.
    """

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        Computes the maximum absolute sum of any subarray in the given list.

        :param nums: List[int] - The input array of integers.
        :return: int - The maximum absolute sum of any subarray.
        """
        max_sum = min_sum = max_absolute = 0

        for num in nums:
            # Track running sums for max and min subarrays
            max_sum = max(0, max_sum + num)
            min_sum = min(0, min_sum + num)

            # Update the maximum absolute sum
            max_absolute = max(max_absolute, abs(max_sum), abs(min_sum))

        return max_absolute


def main():
    """
    Runs sample test cases to validate the solution.
    """
    solution = Solution()

    # Sample test cases
    test_cases = [
        ([-3, 2, 3, -4], 5),                # Expected Output: 5
        ([2, -5, 1, -4, 3, -2], 8),         # Expected Output: 8
    ]

    for nums, expected in test_cases:
        result = solution.maxAbsoluteSum(nums)
        print(f"Input: {nums} | Expected: {expected} | Got: {result}")
        assert result == expected, f"Test failed for input {nums}"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
