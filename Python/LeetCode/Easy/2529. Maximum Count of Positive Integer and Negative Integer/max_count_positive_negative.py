from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        """
        Returns the maximum count between the number of positive integers
        and the number of negative integers in a sorted non-decreasing array.

        :param nums: List[int] - A non-decreasing sorted list of integers.
        :return: int - The maximum count among positive and negative numbers.
        """
        positive_count = 0
        negative_count = 0

        # Count positive and negative numbers
        for num in nums:
            if num > 0:
                positive_count += 1
            elif num < 0:
                negative_count += 1

        return max(positive_count, negative_count)

def main():
    solution = Solution()
    
    # Example test cases
    test_cases = [
        ([-2, -1, -1, 1, 2, 3], 3),
        ([-3, -2, -1, 0, 1, 2], 3),
        ([5, 20, 66, 1314], 4),
        ([-5, -4, -3, -2, -1], 5),
        ([0, 0, 0, 0], 0),
    ]

    for nums, expected in test_cases:
        result = solution.maximumCount(nums)
        print(f"Input: {nums} -> Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    main()
