from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        Finds the length of the longest 'nice' subarray.
        
        A subarray is 'nice' if the bitwise AND of every pair of elements
        in different positions is equal to 0.

        :param nums: List of positive integers.
        :return: Length of the longest nice subarray.
        """
        used_bits = 0           # Tracks bits used in current window
        window_start = 0        # Start position of current window
        max_length = 0          # Length of longest nice subarray found

        for window_end in range(len(nums)):
            # If current number shares bits with window, shrink window from left
            # until there's no bit conflict
            while used_bits & nums[window_end] != 0:
                used_bits ^= nums[window_start]  # Remove leftmost element's bits
                window_start += 1  # Shrink window from left

            # Add current number to the window
            used_bits |= nums[window_end]

            # Update max length if current window is longer
            max_length = max(max_length, window_end - window_start + 1)

        return max_length

def main():
    solution = Solution()

    # Test cases
    test_cases = [
        [1, 3, 8, 48, 10],          # Expected output: 3
        [3, 1, 5, 11, 13],          # Expected output: 1
        [2, 3, 5, 7, 11],           # Expected output: 1
        [4, 8, 16, 2, 1],           # Expected output: 5
        [1, 2, 4, 8, 16]            # Expected output: 5
    ]

    for nums in test_cases:
        result = solution.longestNiceSubarray(nums)
        print(f"Input: {nums} -> Output: {result}")

if __name__ == "__main__":
    main()
