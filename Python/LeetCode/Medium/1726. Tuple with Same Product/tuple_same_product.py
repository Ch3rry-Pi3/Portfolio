from typing import List
from collections import defaultdict

class Solution:
    """
    This class provides an implementation of the 'Tuple with Same Product' problem.

    The function `tupleSameProduct` counts the number of valid tuples (a, b, c, d)
    such that a * b = c * d, where a, b, c, and d are distinct elements of nums.
    """

    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        Computes the number of valid tuples satisfying the condition a * b = c * d.

        :param nums: List of distinct positive integers.
        :return: The total number of valid tuples.
        """
        product_cnt = defaultdict(int)                          # Tracks occurrences of product pairs
        pair_cnt = defaultdict(int)                             # Tracks the count of valid pairs

        # Generate all possible product pairs
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                pair_cnt[product] += product_cnt[product]       # Store valid pair count
                product_cnt[product] += 1                       # Count occurrences of this product

        # Compute final result by multiplying valid pairs by 8 (per problem requirement)
        result = sum(8 * cnt for cnt in pair_cnt.values())

        return result


def main():
    """
    Demonstrates testing the tupleSameProduct function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [2, 3, 4, 6],           # Expected: 8
        [1, 2, 4, 5, 10],       # Expected: 16
        [1, 3, 9, 27],          # Expected: 0 (no valid pairs)
        [2, 4, 6, 8, 12],       # Expected: 40
        [3, 6, 9, 12, 18],      # Expected: 40
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        result = solver.tupleSameProduct(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
