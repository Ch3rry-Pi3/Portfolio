from typing import List

class Solution:
    """
    This class provides an in-place solution for moving zeroes to the end of an array
    while maintaining the relative order of non-zero elements.
    
    The approach uses the two-pointer technique, efficiently swapping elements
    when a non-zero element is found.
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all zeroes in the given list to the end while preserving the order
        of the non-zero elements.

        :param nums: List of integers to be modified in-place.
        """
        left = 0                            # Pointer for placing non-zero elements

        # Iterate through the list with the right pointer
        for right in range(len(nums)):
            if nums[right]:                 # If the element is non-zero
                # Swap the non-zero element with the left pointer position
                nums[left], nums[right] = nums[right], nums[left]
                left += 1                   # Move left pointer forward

def main():
    """
    Demonstrates testing the moveZeroes function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [0, 1, 0, 3, 12],       # Expected: [1, 3, 12, 0, 0]
        [0, 0, 1],              # Expected: [1, 0, 0]
        [2, 1, 3, 0, 4, 0]      # Expected: [2, 1, 3, 4, 0, 0]
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        solver.moveZeroes(nums)
        print(f"Output: {nums}\n")


if __name__ == "__main__":
    main()
