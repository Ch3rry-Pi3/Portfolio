from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        Finds the largest divisible subset from a list of distinct positive integers.

        Args:
            nums (List[int]): A list of distinct positive integers.

        Returns:
            List[int]: The largest divisible subset.
        """
        # The container that holds all intermediate solutions.
        # key: the largest element in a valid subset.
        subsets = {-1: set()}
        
        # Sort the input numbers to build subsets incrementally.
        for num in sorted(nums):
            # Find the largest subset that num can extend.
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}
        
        # Return the largest subset found.
        return list(max(subsets.values(), key=len))


def main():
    solution = Solution()
    test_cases = [
        ([1, 2, 3], [[1, 2], [1, 3]]),              # Expected output can be [1, 2] or [1, 3]
        ([1, 2, 4, 8], [[1, 2, 4, 8]]),             # Expected output [1, 2, 4, 8]
        ([4, 8, 10, 240], [[4, 8, 240]]),           # Expected output [4, 8, 240]
        ([3, 6, 12, 24], [[3, 6, 12, 24]]),         # Expected output [3, 6, 12, 24]
        ([5, 9, 18, 54], [[9, 18, 54]]),            # Expected output [9, 18, 54]
    ]

    for nums, expected in test_cases:
        result = solution.largestDivisibleSubset(nums)
        print(f"Input: {nums}\nExpected: {expected}, Got: {result}\n")


if __name__ == "__main__":
    main()
