from typing import List

class Solution:
    """
    Solution to find the minimum number of swaps required to group all 1's together in a binary array.
    """

    def minSwaps(self, data: List[int]) -> int:
        """
        Uses a sliding window approach to determine the minimum number of swaps 
        needed to group all 1's together in any contiguous subarray.

        :param data: List[int] - A binary array containing 0's and 1's.
        :return: int - The minimum number of swaps required.
        """
        ones = sum(data)  # Total number of 1's in the array
        cnt_one = max_one = 0
        left = right = 0

        while right < len(data):
            # Add the rightmost element to the window count
            cnt_one += data[right]
            right += 1

            # Maintain a window of size 'ones'
            if right - left > ones:
                # Remove the leftmost element from the window count
                cnt_one -= data[left]
                left += 1

            # Track the maximum number of 1's found in any window
            max_one = max(max_one, cnt_one)

        # Minimum swaps needed to group all 1's together
        return ones - max_one


def main():
    """
    Runs sample test cases for the minSwaps function.
    """
    solution = Solution()

    # Sample test cases
    test_cases = [
        [1, 0, 1, 0, 1],                        # Expected output: 1
        [0, 0, 1, 0],                           # Expected output: 0
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],         # Expected output: 3
    ]

    for test in test_cases:
        print(f"Input: {test} → Output: {solution.minSwaps(test)}")


if __name__ == "__main__":
    main()
