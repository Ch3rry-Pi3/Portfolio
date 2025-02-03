from typing import List

class Solution:
    """
    This class provides an implementation of the 'Can Make Arithmetic Progression From Sequence' problem.

    The function `canMakeArithmeticProgression` determines whether the elements of a given array
    can be rearranged to form an arithmetic progression.
    """

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        Determines if the given array can be rearranged to form an arithmetic progression.

        :param arr: List of integers.
        :return: `True` if the array can be rearranged into an arithmetic progression, otherwise `False`.
        """
        minimum = min(arr)          # Find the minimum element
        maximum = max(arr)          # Find the maximum element
        n = len(arr)

        # Calculate common difference
        diff = (maximum - minimum) // (n - 1)
        nums = set(arr)             # Convert list to set for quick lookups

        # Special case: If all elements are the same, the sequence is trivially arithmetic
        if diff == 0:
            return len(nums) == 1
        
        # Check if each expected element in the arithmetic progression exists in the set
        for i in range(minimum, maximum + 1, diff):
            if i not in nums:
                return False        # Missing element, cannot form arithmetic progression

        return True                 # All elements found, valid arithmetic progression


def main():
    """
    Demonstrates testing the canMakeArithmeticProgression function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [3, 5, 1],          # Expected: True (can be rearranged to [1,3,5])
        [1, 2, 4],          # Expected: False (no valid arithmetic progression)
        [7, 3, 5],          # Expected: True (can be rearranged to [3,5,7])
        [1, 1, 1, 1],       # Expected: True (all elements are the same)
        [10, 20, 30]        # Expected: True (already in arithmetic progression)
    ]

    for arr in test_cases:
        print(f"Input: {arr}")
        result = solver.canMakeArithmeticProgression(arr)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
