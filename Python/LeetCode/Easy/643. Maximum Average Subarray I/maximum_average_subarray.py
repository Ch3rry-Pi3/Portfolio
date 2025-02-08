from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Finds the maximum average of any contiguous subarray of length k.

        Args:
            nums (List[int]): List of integers.
            k (int): Length of the subarray.

        Returns:
            float: Maximum average value of a contiguous subarray of length k.
        """
        # Initialise the sum of the first k elements
        current_sum = max_sum = sum(nums[:k])

        # Use sliding window to find the maximum sum for any subarray of length k
        for i in range(len(nums) - k):
            current_sum += nums[i + k] - nums[i]
            max_sum = max(max_sum, current_sum)

        # Return the maximum average
        return max_sum / k


def main():
    """
    Runs example test cases for the findMaxAverage function.
    """
    solution = Solution()

    # Example Test Cases
    test_cases = [
        ([1, 12, -5, -6, 50, 3], 4, 12.75000),
        ([5], 1, 5.00000),
        ([0, 1, 1, 3, 3], 2, 2.00000),
    ]

    for nums, k, expected in test_cases:
        result = solution.findMaxAverage(nums, k)
        print(f"nums: {nums}, k: {k} → Expected: {expected}, Got: {result:.5f}")


if __name__ == "__main__":
    main()
