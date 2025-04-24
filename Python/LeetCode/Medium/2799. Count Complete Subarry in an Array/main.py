from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        """
        Returns the number of complete subarrays.
        A complete subarray has the same number of distinct elements
        as the entire array.
        """
        res = 0
        cnt = {}
        n = len(nums)
        right = 0
        distinct = len(set(nums))  # Number of unique elements in entire array

        for left in range(n):
            if left > 0:
                remove = nums[left - 1]
                cnt[remove] -= 1
                if cnt[remove] == 0:
                    cnt.pop(remove)

            while right < n and len(cnt) < distinct:
                add = nums[right]
                cnt[add] = cnt.get(add, 0) + 1
                right += 1

            if len(cnt) == distinct:
                res += n - right + 1

        return res


def main():
    solution = Solution()
    test_cases = [
        ([1, 3, 1, 2, 2], 4),
        ([5, 5, 5, 5], 10),
        ([1, 2, 3, 4], 10),
        ([2], 1),
        ([1, 1, 1], 6),
    ]

    for nums, expected in test_cases:
        result = solution.countCompleteSubarrays(nums)
        print(f"Input: {nums}\nExpected: {expected}, Got: {result}\n")


if __name__ == "__main__":
    main()
