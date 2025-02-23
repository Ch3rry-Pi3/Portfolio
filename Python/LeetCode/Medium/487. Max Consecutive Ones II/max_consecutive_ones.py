from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Finds the maximum number of consecutive 1's in a binary array
        when at most one 0 can be flipped to 1.

        Args:
            nums (List[int]): A binary list consisting of 0s and 1s.

        Returns:
            int: The maximum number of consecutive 1's achievable after flipping at most one 0.
        """

        longest_sequence = 0        # Stores the maximum sequence of consecutive 1's
        left, right = 0, 0          # Two-pointer window
        num_zeroes = 0              # Tracks the number of zeros in the window

        while right < len(nums):  
            if nums[right] == 0:            # Count zero if present
                num_zeroes += 1

            while num_zeroes == 2:          # If there are more than one zero, contract the window
                if nums[left] == 0:    
                    num_zeroes -= 1
                left += 1

            # Update the maximum sequence length
            longest_sequence = max(longest_sequence, right - left + 1)
            right += 1          # Expand the window

        return longest_sequence


if __name__ == "__main__":
    # Example usage
    solution = Solution()
    example_nums = [1, 0, 1, 1, 0, 1]
    print(solution.findMaxConsecutiveOnes(example_nums))        # Output: 4
