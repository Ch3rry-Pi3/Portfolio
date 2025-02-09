from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
        Counts the number of bad pairs in the given list.

        A pair (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The total number of bad pairs.
        """
        bad_pairs = 0
        diff_count = {}

        for pos in range(len(nums)):
            diff = pos - nums[pos]

            # Count the number of previous positions with the same difference
            good_pairs_count = diff_count.get(diff, 0)

            # Total possible pairs minus good pairs = bad pairs
            bad_pairs += pos - good_pairs_count

            # Update count of positions with this difference
            diff_count[diff] = good_pairs_count + 1

        return bad_pairs


def main():
    """
    Runs example test cases for the countBadPairs function.
    """
    solution = Solution()

    # Example Test Cases
    test_cases = [
        ([4, 1, 3, 3], 5),
        ([1, 2, 3, 4, 5], 0),
        ([3, 2, 1, 0], 6),
        ([0, 0, 0, 0], 6),
    ]

    for nums, expected in test_cases:
        result = solution.countBadPairs(nums)
        print(f"nums: {nums} → Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    main()
