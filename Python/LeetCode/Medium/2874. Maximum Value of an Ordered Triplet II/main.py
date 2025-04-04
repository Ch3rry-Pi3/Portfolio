from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        Returns the maximum value of the ordered triplet (i, j, k) 
        where i < j < k and (nums[i] - nums[j]) * nums[k] is maximized.
        """
        n = len(nums)
        res, imax, dmax = 0, 0, 0
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res

def main():
    solution = Solution()
    test_cases = [
        # (nums, expected)
        ([12, 6, 1, 2, 7], 77),
        ([1, 10, 3, 4, 19], 133),
        ([1, 2, 3], 0),
        ([100, 50, 25, 12, 6], 0),
        ([5, 5, 5, 5, 5], 0),
    ]

    for nums, expected in test_cases:
        result = solution.maximumTripletValue(nums)
        print(f"Input: {nums}\nExpected: {expected}, Got: {result}\n")

if __name__ == "__main__":
    main()
