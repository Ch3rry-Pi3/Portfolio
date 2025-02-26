from typing import List

class Solution:
    """
    This class provides a solution for counting subarrays with an odd sum.
    """

    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        Returns the number of subarrays with an odd sum.

        :param arr: List[int] - The input array of integers.
        :return: int - The count of subarrays with an odd sum modulo 10^9 + 7.
        """
        MOD = int(1e9 + 7)  # Modulo value to prevent integer overflow
        n = len(arr)

        # Convert each element to 0 (even) or 1 (odd)
        arr = [num % 2 for num in arr]

        # dp_even[i]: Number of subarrays with an even sum ending at index i
        # dp_odd[i]: Number of subarrays with an odd sum ending at index i
        dp_even, dp_odd = [0] * n, [0] * n

        # Initialise the last element
        if arr[n - 1] == 0:
            dp_even[n - 1] = 1
        else:
            dp_odd[n - 1] = 1

        # Traverse the array in reverse to calculate dp values
        for i in range(n - 2, -1, -1):
            if arr[i] == 1:
                # Odd element contributes to odd subarrays
                dp_odd[i] = (1 + dp_even[i + 1]) % MOD
                # Even element continues the pattern
                dp_even[i] = dp_odd[i + 1]
            else:
                # Even element contributes to even subarrays
                dp_even[i] = (1 + dp_even[i + 1]) % MOD
                # Odd element continues the pattern
                dp_odd[i] = dp_odd[i + 1]

        # Sum all the odd subarrays and return the result
        return sum(dp_odd) % MOD


def main():
    """
    Runs sample test cases to validate the solution.
    """
    solution = Solution()

    # Sample test cases
    test_cases = [
        ([1, 3, 5], 4),                     # Expected Output: 4
        ([2, 4, 6], 0),                     # Expected Output: 0
        ([1, 2, 3, 4, 5, 6, 7], 16)         # Expected Output: 16
    ]

    for arr, expected in test_cases:
        result = solution.numOfSubarrays(arr)
        print(f"Input: {arr} | Expected: {expected} | Got: {result}")
        assert result == expected, f"Test failed for input {arr}"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
