from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        Count the number of good triplets in the array where the triplet (i, j, k) satisfies:
        - 0 <= i < j < k < len(arr)
        - |arr[i] - arr[j]| <= a
        - |arr[j] - arr[k]| <= b
        - |arr[i] - arr[k]| <= c

        Args:
        arr (List[int]): Input array of integers.
        a (int): Maximum allowed absolute difference between arr[i] and arr[j].
        b (int): Maximum allowed absolute difference between arr[j] and arr[k].
        c (int): Maximum allowed absolute difference between arr[i] and arr[k].

        Returns:
        int: Number of good triplets.
        """
        n = len(arr)
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (
                        abs(arr[i] - arr[j]) <= a
                        and abs(arr[j] - arr[k]) <= b
                        and abs(arr[i] - arr[k]) <= c
                    ):
                        cnt += 1
        return cnt


def main():
    solution = Solution()
    
    # Example test cases
    test_cases = [
        ([3, 0, 1, 1, 9, 7], 7, 2, 3, 4),
        ([1, 1, 2, 2, 3], 0, 0, 1, 0),
        ([1, 2, 3, 4, 5], 2, 3, 4, 4),
    ]

    for arr, a, b, c, expected in test_cases:
        result = solution.countGoodTriplets(arr, a, b, c)
        print(f"Input: arr={arr}, a={a}, b={b}, c={c}")
        print(f"Expected: {expected}, Got: {result}\n")


if __name__ == "__main__":
    main()
