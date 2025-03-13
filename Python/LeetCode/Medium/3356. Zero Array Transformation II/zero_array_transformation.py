from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        Finds the minimum number of queries required to transform nums into a Zero Array.

        :param nums: List[int] - The input array of integers.
        :param queries: List[List[int]] - A list of queries, where each query is [l, r, val].
        :return: The minimum number of queries required to make nums a Zero Array, or -1 if impossible.
        """
        n = len(nums)
        total_sum = 0
        k = 0
        difference_array = [0] * (n + 1)

        # Iterate through nums
        for index in range(n):
            # Process queries while the current index of nums is not zero
            while total_sum + difference_array[index] < nums[index]:
                k += 1

                # If all queries are exhausted and nums is not a Zero Array, return -1
                if k > len(queries):
                    return -1

                left, right, val = queries[k - 1]

                # Apply range update using a difference array technique
                if right >= index:
                    difference_array[max(left, index)] += val
                    difference_array[right + 1] -= val

            # Update the running prefix sum at the current index
            total_sum += difference_array[index]

        return k


def main():
    solution = Solution()

    test_cases = [
        ([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]]),
        ([4, 3, 2], [[1, 3, 2], [0, 2, 1]]),
        ([5, 5, 5], [[0, 2, 2], [0, 1, 3], [1, 2, 1]])
    ]

    for nums, queries in test_cases:
        result = solution.minZeroArray(nums, queries)
        print(f"Input: nums={nums}, queries={queries} -> Output: {result}")


if __name__ == "__main__":
    main()
