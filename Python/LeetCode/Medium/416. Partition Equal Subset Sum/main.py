from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Determines if the given array can be partitioned into two subsets
        such that the sum of elements in both subsets is equal.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            bool: True if the array can be partitioned into two equal sum subsets, False otherwise.
        """
        # If the sum of elements is odd, it can't be split equally
        if sum(nums) % 2 != 0:
            return False

        # Initialize the set of possible sums
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        # Iterate through each number in the array from the end to the start
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                # If the current number makes the sum equal to the target, return True
                if (t + nums[i]) == target:
                    return True
                # Add both possibilities: including and excluding the current number
                nextDP.add(t + nums[i])
                nextDP.add(t)
            # Update dp for the next iteration
            dp = nextDP
        
        # Check if the target sum is in the set of possible sums
        return target in dp

def main():
    solution = Solution()
    test_cases = [
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
        ([1, 2, 5], False),
        ([2, 2, 3, 5], True),
        ([3, 3, 3, 4, 5], True),
    ]

    for nums, expected in test_cases:
        result = solution.canPartition(nums)
        print(f"Input: {nums}\nExpected: {expected}, Got: {result}\n")

if __name__ == "__main__":
    main()
