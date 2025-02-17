from typing import List

class Solution:
    """
    This class provides an implementation of the 'Squares of a Sorted Array' problem.
    
    The function `sortedSquares` takes an integer array `nums`, squares each number, 
    and returns a new array sorted in non-decreasing order.
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Returns an array of the squares of each number in `nums`, sorted in non-decreasing order.

        Uses a two-pointer approach for an O(n) solution.

        :param nums: List of integers sorted in non-decreasing order.
        :return: List of squared values, sorted in non-decreasing order.
        """
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                square = nums[left]
                left += 1
            else:
                square = nums[right]
                right -= 1
            result[i] = square * square

        return result


def main():
    """
    Demonstrates the use of the Solution class by testing `sortedSquares`
    with example inputs.
    """
    solution = Solution()

    # Example test cases
    nums1 = [-4, -1, 0, 3, 10]
    nums2 = [-7, -3, 2, 3, 11]

    # Compute and display results
    print("Input:", nums1)
    print("Output:", solution.sortedSquares(nums1))  # Expected: [0, 1, 9, 16, 100]

    print("\nInput:", nums2)
    print("Output:", solution.sortedSquares(nums2))  # Expected: [4, 9, 9, 49, 121]


if __name__ == "__main__":
    main()
