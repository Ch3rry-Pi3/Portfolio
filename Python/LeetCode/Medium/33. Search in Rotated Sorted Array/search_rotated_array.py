from typing import List

class Solution:
    """
    This class provides an implementation of the 'Search in Rotated Sorted Array' problem.
    
    The function finds the index of the target in a rotated sorted array using a binary search approach.
    """

    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array.

        :param nums: List of unique integers sorted in ascending order but rotated
        :param target: The integer value to search for
        :return: The index of the target in nums, or -1 if not found
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            
            # If the middle element is the target, return its index
            if target == nums[middle]:
                return middle
            
            # Determine if we are in the left-sorted portion
            if nums[left] <= nums[middle]:  
                # Check if target is outside the left-sorted range
                if target > nums[middle] or target < nums[left]:  
                    left = middle + 1       # Search right portion
                else:
                    right = middle - 1      # Search left portion
            
            # Otherwise, we are in the right-sorted portion
            else:  
                # Check if target is outside the right-sorted range
                if target < nums[middle] or target > nums[right]:  
                    right = middle - 1      # Search left portion
                else:
                    left = middle + 1       # Search right portion
        
        return -1  # Target not found


def main():
    """
    Demonstrates searching for a target in rotated sorted arrays for multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0),  # Expected output: 4
        ([4, 5, 6, 7, 0, 1, 2], 3),  # Expected output: -1
        ([1], 0),                    # Expected output: -1
        ([1, 3], 3),                 # Expected output: 1
        ([5, 1, 3], 3),              # Expected output: 2
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}")
        result = solver.search(nums, target)
        print(f"Target Index: {result}\n\n")


if __name__ == "__main__":
    main()
