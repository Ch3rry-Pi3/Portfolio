from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Finds the pivot index in an array where the sum of all numbers strictly
        to the left equals the sum of all numbers strictly to the right.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The leftmost pivot index if it exists, otherwise -1.
        """

        # Calculate the total sum of the array
        total_sum = sum(nums)

        # Initialise left sum as 0
        left_sum = 0

        # Iterate over each index and check pivot condition
        for i, num in enumerate(nums):
            # If left sum equals the right sum (total_sum - left_sum - num), return index
            if left_sum == (total_sum - left_sum - num):
                return i

            # Update left sum by adding the current element
            left_sum += num

        # If no pivot index is found, return -1
        return -1


def main():
    # Example test cases
    solution = Solution()
    test_cases = [
        ([1, 7, 3, 6, 5, 6], 3),
        ([1, 2, 3], -1),
        ([2, 1, -1], 0),
    ]

    for nums, expected in test_cases:
        result = solution.pivotIndex(nums)
        print(f"Input: {nums} | Expected: {expected} | Output: {result}")


if __name__ == "__main__":
    main()
