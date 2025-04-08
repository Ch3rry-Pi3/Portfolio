from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Returns the minimum number of operations needed to make all elements in the array distinct.
        To achieve this, we remove 3 elements from the beginning of the array any number of times.
        
        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The minimum number of operations required.
        """
        seen = [False] * 128
        for i in range(len(nums) - 1, -1, -1):
            if seen[nums[i]]:
                return i // 3 + 1
            seen[nums[i]] = True
        return 0


def main():
    solution = Solution()
    test_cases = [
        ([1, 2, 3, 4, 2, 3, 5, 7], 2),   # Example 1
        ([4, 5, 6, 4], 2),               # Example 2
        ([6, 7, 8, 9], 0),               # Example 3
        ([1, 1, 1, 1], 1),               # Edge case: all elements the same
        ([1], 0),                        # Edge case: single element
        ([], 0),                         # Edge case: empty list
    ]

    for nums, expected in test_cases:
        result = solution.minimumOperations(nums)
        print(f"Input: {nums}\nExpected: {expected}, Got: {result}\n")


if __name__ == "__main__":
    main()
