from typing import List

class Solution:
    """
    This class provides a solution to find the longest Fibonacci-like subsequence.
    """

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        Computes the length of the longest Fibonacci-like subsequence in arr.

        :param arr: List[int] - The input list of strictly increasing positive integers.
        :return: int - The length of the longest Fibonacci-like subsequence.
        """
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        max_len = 0

        for curr in range(2, n):
            start, end = 0, curr - 1

            while start < end:
                pair_sum = arr[start] + arr[end]

                if pair_sum > arr[curr]:
                    end -= 1
                elif pair_sum < arr[curr]:
                    start += 1
                else:
                    # Found a valid Fibonacci-like subsequence
                    dp[end][curr] = dp[start][end] + 1
                    max_len = max(dp[end][curr], max_len)
                    end -= 1
                    start += 1

        return max_len + 2 if max_len else 0


def main():
    """
    Runs sample test cases to validate the solution.
    """
    solution = Solution()

    # Sample test cases
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8], 5),          # Expected Output: 5
        ([1, 3, 7, 11, 12, 14, 18], 3),         # Expected Output: 3
    ]

    for arr, expected in test_cases:
        result = solution.lenLongestFibSubseq(arr)
        print(f"Input: {arr} | Expected: {expected} | Got: {result}")
        assert result == expected, f"Test failed for input {arr}"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
