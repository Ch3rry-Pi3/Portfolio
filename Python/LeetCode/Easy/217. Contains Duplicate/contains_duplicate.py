from typing import List

class Solution:
    """
    This class provides an implementation of the 'Contains Duplicate' problem.
    
    The function checks whether any element appears at least twice in the list.
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Determines if an array contains duplicate elements.

        :param nums: List of integers
        :return: True if any number appears at least twice, otherwise False
        """
        hashset = set()  # Using a set for O(1) lookup time

        for n in nums:
            if n in hashset:
                return True  # Found a duplicate, return immediately
            hashset.add(n)  # Add element to the set
        
        return False  # No duplicates found


def main():
    """
    Demonstrates checking for duplicates in multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [1, 2, 3, 1],       # Expected output: True (1 appears twice)
        [1, 2, 3, 4],       # Expected output: False (all elements are unique)
        [1, 1, 1, 3, 3, 4], # Expected output: True (multiple duplicates)
        [],                 # Expected output: False (empty list)
        [10]                # Expected output: False (only one element)
    ]

    for nums in test_cases:
        print(f"nums = {nums}")
        result = solver.containsDuplicate(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
