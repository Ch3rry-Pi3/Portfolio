from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Finds the maximum number of consecutive 1s in a binary array
        if at most k 0s can be flipped.

        Args:
            nums (List[int]): The binary array (containing 0s and 1s).
            k (int): The maximum number of 0s that can be flipped.

        Returns:
            int: The maximum length of consecutive 1s possible.
        """
        left = 0

        for right in range(len(nums)):
            # Reduce k when we include a zero in the window
            k -= 1 - nums[right]

            # If k becomes negative, move left pointer to balance the window
            if k < 0:
                k += 1 - nums[left]
                left += 1

        return right - left + 1


def main():
    """
    Runs example test cases for the longestOnes function.
    """
    solution = Solution()

    # Example Test Cases
    test_cases = [
        ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
        ([0,0,1,1,1,0,0], 0, 3),
        ([0,0,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1], 3, 10),
        ([1,0,1,1,0,1,1,1,0,0,1,1,1], 2, 9),
    ]

    for nums, k, expected in test_cases:
        result = solution.longestOnes(nums, k)
        print(f"nums: {nums}, k: {k} → Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    main()
