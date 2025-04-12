from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place such that each element appears only once.
        Returns the number of unique elements.

        Args:
        nums (List[int]): The sorted input array with possible duplicates.

        Returns:
        int: The count of unique elements.
        """
        if not nums:
            return 0

        insertIndex = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insertIndex] = nums[i]
                insertIndex += 1

        return insertIndex


def main():
    solution = Solution()
    test_cases = [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
        ([1, 2, 3], 3),
        ([1, 1, 1, 1], 1),
        ([], 0)
    ]

    for nums, expected_k in test_cases:
        original = nums[:]
        k = solution.removeDuplicates(nums)
        print(f"Input: {original}")
        print(f"Output: k = {k}, nums = {nums[:k]} + {nums[k:]}")
        print(f"Expected k = {expected_k}")
        print("-" * 50)


if __name__ == "__main__":
    main()
 