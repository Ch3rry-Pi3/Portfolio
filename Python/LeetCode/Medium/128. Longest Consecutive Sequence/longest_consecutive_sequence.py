from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive elements sequence in an unsorted list.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The length of the longest consecutive sequence.
        """
        if not nums:
            return 0

        # Sort the numbers
        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            # Ignore duplicates
            if nums[i] != nums[i - 1]:
                # If consecutive, increase streak count
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    # Update longest streak and reset current streak
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)


def main():
    """
    Runs example test cases for the longestConsecutive function.
    """
    solution = Solution()

    # Example Test Cases
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([9, 1, 4, 7, 3, -2, -1, 0, 2, 5, 8, 6], 10),
        ([1, 2, 0, 1], 3),
        ([], 0),
    ]

    for nums, expected in test_cases:
        result = solution.longestConsecutive(nums)
        print(f"nums: {nums} → Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    main()
