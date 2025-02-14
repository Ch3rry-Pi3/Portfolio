from typing import List

class Solution:
    """
    A class to find the closest number to zero in a list.
    If multiple numbers have the same distance to zero, the largest number is returned.
    """

    def findClosestNumber(self, nums: List[int]) -> int:
        """
        Finds the closest number to zero from a given list.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The number closest to zero. If multiple numbers have the same 
                 distance, return the larger number.
        """
        # Initialise 'closest' with the first element in the list
        closest = nums[0]

        # Iterate through the list to find the closest number to zero
        for num in nums:
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num

        return closest


def main():
    """Example usage of the `findClosestNumber` function."""

    solution = Solution()

    # Example test cases
    test_cases = [
        ([-4, -2, 1, 4, 8], 1),         # Expected output: 1
        ([2, -1, 1], 1),                # Expected output: 1
        ([-5, -3, -1, -6], -1),         # Expected output: -1
        ([0, 5, -5, 3, -3], 0),         # Expected output: 0
    ]

    for nums, expected in test_cases:
        result = solution.findClosestNumber(nums)
        print(f"Input: {nums} → Closest to zero: {result} (Expected: {expected})")

if __name__ == "__main__":
    main()
