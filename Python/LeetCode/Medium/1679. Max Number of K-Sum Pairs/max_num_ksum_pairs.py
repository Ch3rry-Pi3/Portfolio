from typing import List
from collections import defaultdict

class Solution:
    """
    This class provides an implementation of the 'Max Number of K-Sum Pairs' problem.

    The function `maxOperations` finds the maximum number of operations where 
    we remove two numbers that sum up to `k`.
    """

    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Determines the maximum number of operations where two elements sum to `k`.

        :param nums: List of integers.
        :param k: Target sum for pairs.
        :return: Maximum number of operations possible.
        """
        count_map = defaultdict(int)                # Dictionary to store counts of seen numbers
        pairs = 0                                   # Counter for valid k-sum pairs

        # Iterate through the numbers
        for num in nums:
            complement = k - num                    # Find the complement needed to form sum `k`

            if count_map[complement] > 0:           # Check if complement exists
                pairs += 1                          # Increment pair count
                count_map[complement] -= 1          # Use up one occurrence of the complement
            else:
                count_map[num] += 1                 # Store the number in the dictionary

        return pairs                                # Return total number of valid k-sum pairs


def main():
    """
    Demonstrates testing the maxOperations function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        ([1, 2, 3, 4], 5),              # Expected: 2
        ([3, 1, 3, 4, 3], 6),           # Expected: 1
        ([2, 2, 2, 2, 2], 4),           # Expected: 2
        ([1, 2, 3, 4, 5, 6], 7),        # Expected: 3
        ([4, 4, 4, 4], 8),              # Expected: 2
    ]

    for nums, k in test_cases:
        print(f"Input: nums = {nums}, k = {k}")
        result = solver.maxOperations(nums, k)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
