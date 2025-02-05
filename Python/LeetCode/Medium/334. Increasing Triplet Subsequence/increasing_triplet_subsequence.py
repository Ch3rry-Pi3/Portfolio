from typing import List

class Solution:
    """
    This class provides an implementation of the 'Increasing Triplet Subsequence' problem.

    The function `increasingTriplet` checks whether there exists an increasing triplet 
    (three increasing elements in order) in the given list.
    """

    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Determines if there exists an increasing subsequence of length 3.

        :param nums: List of integers.
        :return: `True` if an increasing triplet exists, otherwise `False`.
        """
        num_i = num_j = float('inf')    # Initialise two smallest elements

        # Iterate through the array to find an increasing triplet
        for num in nums:
            if num <= num_i:
                num_i = num             # Update the smallest value
            elif num <= num_j:
                num_j = num             # Update the second smallest value
            else:   
                return True             # A valid increasing triplet is found

        return False                    # No increasing triplet found


def main():
    """
    Demonstrates testing the increasingTriplet function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [1, 2, 3, 4, 5],                # Expected: True (1,2,3 forms an increasing triplet)
        [5, 4, 3, 2, 1],                # Expected: False (No increasing sequence)
        [2, 1, 5, 0, 4, 6],             # Expected: True (1, 4, 6 forms an increasing triplet)
        [20, 100, 10, 12, 5, 13],       # Expected: True (10, 12, 13 forms an increasing triplet)
        [1, 1, 1, 1],                   # Expected: False (No increasing sequence)
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        result = solver.increasingTriplet(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
