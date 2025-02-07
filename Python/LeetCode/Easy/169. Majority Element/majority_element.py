from typing import List

class Solution:
    """
    This class provides an implementation of the 'Majority Element' problem.

    The function `majorityElement` finds the element that appears more than ⌊ n/2 ⌋ times
    using the Boyer-Moore Voting Algorithm.
    """

    def majorityElement(self, nums: List[int]) -> int:
        """
        Determines the majority element in the given list.

        :param nums: List of integers.
        :return: The majority element (appears more than ⌊ n/2 ⌋ times).
        """
        candidate = None                                    # Stores the potential majority element
        count = 0                                           # Counter for tracking candidate frequency

        # Boyer-Moore Voting Algorithm
        for num in nums:
            if count == 0:
                candidate = num                             # Set new candidate
            
            count += 1 if num == candidate else -1          # Adjust count

        return candidate                                    # Majority element guaranteed to exist


def main():
    """
    Demonstrates testing the majorityElement function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [3, 2, 3],                      # Expected: 3
        [2, 2, 1, 1, 1, 2, 2],          # Expected: 2
        [1, 1, 1, 2, 3, 1, 1],          # Expected: 1
        [6, 5, 5],                      # Expected: 5
        [10, 10, 10, 2, 2, 2, 10],      # Expected: 10
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        result = solver.majorityElement(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
