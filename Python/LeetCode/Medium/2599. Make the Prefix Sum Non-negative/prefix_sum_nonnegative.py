import heapq
from typing import List

class Solution:
    """
    A class to find the minimum number of operations needed to make the prefix sum non-negative.
    """

    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        """
        Computes the minimum number of operations required to ensure all prefix sums are non-negative.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The minimum number of operations required.
        """

        operations = 0                  # Track the number of operations performed
        prefix_sum = 0                  # Running prefix sum
        min_heap = []                   # Min heap to store negative numbers

        for num in nums:
            # Push negative elements to the min heap
            if num < 0:
                heapq.heappush(min_heap, num)

            prefix_sum += num           # Update prefix sum

            # If the prefix sum becomes negative, remove the smallest negative number
            if prefix_sum < 0:
                prefix_sum -= heapq.heappop(min_heap)
                operations += 1         # Increment the operations count

        return operations


def main():
    """
    Runs example test cases for the makePrefSumNonNegative function.
    """
    solution = Solution()

    # Example Test Cases
    test_cases = [
        ([2, 3, -5, 4], 0),
        ([3, -5, -2, 6], 1),
        ([-1, -2, -3, -4], 4),
        ([10, -5, 3, -6, 2], 1),
        ([1, -2, -3, 5, 6], 2),
    ]

    for nums, expected in test_cases:
        result = solution.makePrefSumNonNegative(nums)
        print(f"nums: {nums} → Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    main()
