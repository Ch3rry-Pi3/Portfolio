from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Solves the House Robber problem using dynamic programming.

        Args:
            nums (List[int]): A list of non-negative integers representing the amount of money at each house.

        Returns:
            int: The maximum amount of money that can be robbed without alerting the police.
        """
        # Initialize variables to track the maximum profit
        rob1, rob2 = 0, 0

        # Iterate through each house's money
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        # Return the maximum amount robbed
        return rob2


def main():
    """
    Runs example test cases for the rob function.
    """
    solution = Solution()

    # Example Test Cases
    test_cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([5, 1, 1, 5], 10),
        ([100, 1, 1, 100], 200),
        ([0], 0),
    ]

    for nums, expected in test_cases:
        result = solution.rob(nums)
        print(f"nums: {nums} → Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    main()
