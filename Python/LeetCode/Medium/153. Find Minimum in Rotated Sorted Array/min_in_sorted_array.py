from typing import List

class Solution:
    """
    This class provides an implementation of the 'Find Minimum in Rotated Sorted Array' problem.
    
    The function finds the minimum element in a rotated sorted array using a binary search approach.
    """

    def findMin(self, nums: List[int]) -> int:
        """
        Finds the minimum element in a rotated sorted array.

        :param nums: List of unique integers sorted in ascending order but rotated
        :return: The minimum element in the array
        """
        result = nums[0]  # Initialize result with the first element
        left, right = 0, len(nums) - 1

        while left <= right:
            # If the array is already sorted, return the leftmost element
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            
            middle = (left + right) // 2  # Find the middle index
            result = min(result, nums[middle])  # Update result with the middle element
            
            # Determine which half to search next
            if nums[middle] >= nums[left]:  # Left half is sorted, search right half
                left = middle + 1
            else:  # Right half is sorted, search left half
                right = middle - 1
        
        return result


def main():
    """
    Demonstrates finding the minimum element in rotated sorted arrays for multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [3, 4, 5, 1, 2],  # Expected output: 1
        [4, 5, 6, 7, 0, 1, 2],  # Expected output: 0
        [11, 13, 15, 17],  # Expected output: 11
        [2, 1],  # Expected output: 1
        [1],  # Expected output: 1
    ]

    for nums in test_cases:
        print(f"nums = {nums}")
        result = solver.findMin(nums)
        print(f"Minimum Element: {result}\\n")


if __name__ == "__main__":
    main()
