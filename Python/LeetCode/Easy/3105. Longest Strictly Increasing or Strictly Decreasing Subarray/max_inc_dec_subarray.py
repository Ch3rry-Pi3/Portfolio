from typing import List

class Solution:
    """
    This class provides an implementation of the 'Longest Strictly Increasing or Strictly Decreasing Subarray' problem.

    The function `longestMonotonicSubarray` finds the length of the longest contiguous subarray that is either
    strictly increasing or strictly decreasing.
    """

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        Determines the length of the longest strictly increasing or strictly decreasing subarray.

        :param nums: List of integers.
        :return: Length of the longest monotonic subarray.
        """
        current = result = 1  # Tracks current subarray length and max length found
        increasing = 0  # 1 for increasing, -1 for decreasing, 0 for neutral (start)

        # Iterate through the list to find the longest monotonic subarray
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:                               # Case 1: Increasing sequence
                current = current + 1 if increasing == 1 else 2     # Extend or reset count
                increasing = 1                                      # Mark increasing trend
            elif nums[i] < nums[i - 1]:                             # Case 2: Decreasing sequence
                current = current + 1 if increasing == -1 else 2    # Extend or reset count
                increasing = -1                                     # Mark decreasing trend
            else:                                                   # Case 3: Equal values, reset tracking
                current = 1
                increasing = 0                                      # Reset trend indicator

            result = max(result, current)                           # Update max length if needed

        return result


def main():
    """
    Demonstrates testing the longestMonotonicSubarray function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [1, 4, 3, 3, 2],            # Expected: 2
        [3, 3, 3, 3],               # Expected: 1
        [3, 2, 1],                  # Expected: 3
        [1, 2, 3, 2, 1],            # Expected: 3
        [5, 6, 7, 8, 9]             # Expected: 5
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        result = solver.longestMonotonicSubarray(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
