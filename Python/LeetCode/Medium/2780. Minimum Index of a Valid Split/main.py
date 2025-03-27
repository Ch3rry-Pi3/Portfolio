from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        """
        Returns the minimum index of a valid split in the array such that
        both parts share the same dominant element.
        """
        # Phase 1: Find the dominant element using Boyer-Moore Voting Algorithm
        candidate = nums[0]
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = num
                count = 1

        # Phase 2: Count how many times the candidate appears in the array
        total_count = nums.count(candidate)

        # Phase 3: Try to split and check validity
        left_count = 0
        for index in range(len(nums)):
            if nums[index] == candidate:
                left_count += 1

            right_count = total_count - left_count

            if left_count * 2 > index + 1 and right_count * 2 > len(nums) - index - 1:
                return index

        return -1


def main():
    solution = Solution()
    test_cases = [
        ([1, 2, 2, 2], 2),
        ([2, 1, 3, 1, 1, 7, 1, 2, 1], 4),
        ([3, 3, 3, 3, 7, 2, 2], -1),
        ([1, 1], 0),
        ([1], -1),
    ]

    for nums, expected in test_cases:
        result = solution.minimumIndex(nums)
        print(f"Input: {nums}\nExpected: {expected}, Got: {result}\n")


if __name__ == "__main__":
    main()
