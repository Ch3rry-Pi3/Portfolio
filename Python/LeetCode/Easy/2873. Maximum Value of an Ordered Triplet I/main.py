from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        Returns the maximum value of an ordered triplet (i, j, k) such that:
        i < j < k and (nums[i] - nums[j]) * nums[k] is maximized.
        If all triplets have a negative value, returns 0.
        """
        n = len(nums)
        res, imax, dmax = 0, 0, 0
        
        # Traverse through the list to calculate the maximum triplet value
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        
        return res


def main():
    solution = Solution()
    test_cases = [
        ([12, 6, 1, 2, 7], 77),   # Example 1
        ([1, 10, 3, 4, 19], 133), # Example 2
        ([1, 2, 3], 0),           # Example 3
        ([5, 3, 6, 1, 4], 15),    # Custom test case
        ([7, 2, 8, 3, 5], 24),    # Custom test case
    ]

    for nums, expected in test_cases:
        result = solution.maximumTripletValue(nums)
        print(f"Input: {nums}\nExpected: {expected}, Got: {result}\n")


if __name__ == "__main__":
    main()
