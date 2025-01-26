from typing import List

class Solution:
    """
    This class provides an implementation of the Two Sum problem using a hashmap (dictionary).
    
    The function finds two numbers in an array that add up to a given target and returns their indices.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two numbers in the list that add up to the target.

        :param nums: List of integers
        :param target: Target sum
        :return: Indices of the two numbers that add up to the target
        """
        prev_map = {}  # Dictionary to store number: index pairs

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]  # Return the indices of the two numbers
            
            prev_map[n] = i  # Store the current number with its index
        
        return []  # Return an empty list if no solution is found (though problem guarantees one)

    
def main():
    """
    Demonstrates finding two indices that sum to a target value.
    """
    solver = Solution()

    # Example cases from LeetCode
    test_cases = [
        ([2, 7, 11, 15], 9),    # Expected output: [0,1]
        ([3, 2, 4], 6),         # Expected output: [1,2]
        ([3, 3], 6)             # Expected output: [0,1]
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}")
        result = solver.twoSum(nums, target)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
