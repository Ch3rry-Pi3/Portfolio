from typing import List

class Solution:
    """
    This class provides an implementation of the '3Sum' problem.
    
    The function finds all unique triplets in an array that sum to zero.
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds unique triplets in nums where the sum is zero.

        :param nums: List of integers
        :return: List of unique triplets that sum to zero
        """
        result = []  # Stores unique triplets
        nums.sort()  # Sort the input array to enable two-pointer approach

        for i, a in enumerate(nums):
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            # Use two-pointer technique for the remaining elements
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1  # Move right pointer left (reduce sum)
                elif threeSum < 0:
                    left += 1  # Move left pointer right (increase sum)
                else:
                    result.append([a, nums[left], nums[right]])  # Found valid triplet

                    # Move left pointer and avoid duplicates
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result


def main():
    """
    Demonstrates finding all unique 3Sum triplets for multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [-1, 0, 1, 2, -1, -4],  # Expected output: [[-1, -1, 2], [-1, 0, 1]]
        [0, 1, 1],  # Expected output: []
        [0, 0, 0],  # Expected output: [[0, 0, 0]]
        [-2, 0, 1, 1, 2],  # Expected output: [[-2, 0, 2], [-2, 1, 1]]
        [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],  # Expected output: Unique valid triplets
    ]

    for nums in test_cases:
        print(f"nums = {nums}")
        result = solver.threeSum(nums)
        print(f"3Sum Triplets: {result}\n")


if __name__ == "__main__":
    main()
