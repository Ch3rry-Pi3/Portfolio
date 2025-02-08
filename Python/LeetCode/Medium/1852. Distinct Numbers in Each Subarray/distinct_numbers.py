from typing import List

class Solution:
    """
    A class to find the number of distinct numbers in each subarray of length k.
    """

    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        """
        Computes the number of distinct elements in each subarray of size k.

        Args:
            nums (List[int]): The input list of integers.
            k (int): The size of the subarray.

        Returns:
            List[int]: A list containing the number of distinct elements in each subarray.
        """

        len_nums = len(nums)
        answer = [0] * (len_nums - k + 1)

        # Dictionary to track frequency of numbers in current window
        freq = {}

        # Initialise first window
        for num in nums[:k]:
            freq[num] = freq.get(num, 0) + 1
        answer[0] = len(freq)

        # Slide the window and update counts
        for pos in range(k, len_nums):
            # Remove leftmost element from the window
            left = nums[pos - k]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]

            # Add rightmost element to the window
            right = nums[pos]
            freq[right] = freq.get(right, 0) + 1

            # Store the count of distinct elements
            answer[pos - k + 1] = len(freq)

        return answer


def main():
    """
    Runs example test cases for the distinctNumbers function.
    """
    solution = Solution()

    # Example Test Cases
    test_cases = [
        ([1, 2, 3, 2, 2, 1, 3], 3, [3, 2, 2, 2, 3]),
        ([1, 1, 1, 1, 2, 3, 4], 4, [1, 2, 3, 4]),
        ([4, 4, 4, 4, 4], 2, [1, 1, 1, 1]),
    ]

    for nums, k, expected in test_cases:
        result = solution.distinctNumbers(nums, k)
        print(f"nums: {nums}, k: {k} → Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    main()
