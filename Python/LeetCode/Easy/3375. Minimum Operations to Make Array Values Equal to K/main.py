from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Returns the minimum number of operations required to make every element
        in nums equal to k. If it's not possible, returns -1.

        An operation consists of selecting a valid integer h such that all elements
        strictly greater than h in the array are equal, and then setting all values
        greater than h to h.

        Args:
            nums (List[int]): The input array of integers.
            k (int): The target value.

        Returns:
            int: The minimum number of operations required, or -1 if impossible.
        """
        seen = set()
        for num in nums:
            if num < k:
                return -1
            elif num > k:
                seen.add(num)
        return len(seen)


def main():
    solution = Solution()
    test_cases = [
        ([5, 2, 5, 4, 5], 2, 2),
        ([2, 1, 2], 2, -1),
        ([9, 7, 5, 3], 1, 4),
        ([3, 3, 3], 3, 0),
        ([4, 5, 6, 7], 3, 4),
    ]

    for nums, k, expected in test_cases:
        result = solution.minOperations(nums, k)
        print(f"Input: nums={nums}, k={k}\nExpected: {expected}, Got: {result}\n")


if __name__ == "__main__":
    main()
