from collections import Counter
from typing import List

class Solution:
    """
    Solution class to check if an array can be split into two parts 
    with distinct elements.
    """

    def isPossibleToSplit(self, nums: List[int]) -> bool:
        """
        Determines whether the given array can be split into two equal-length 
        subarrays containing distinct elements.

        The approach uses a frequency counter:
        - If any element appears more than twice, it is impossible to split the array.
        - Otherwise, a valid split is always possible.

        Args:
            nums (List[int]): The input array of even length.

        Returns:
            bool: True if the array can be split, False otherwise.
        """

        # Count the occurrences of each element
        counter = Counter(nums)

        # Check if any element appears more than twice
        for frequency in counter.values():
            if frequency > 2:
                return False

        return True


if __name__ == "__main__":
    # Example usage
    solution = Solution()

    # Example cases
    example_1 = [1, 1, 2, 2, 3, 4]
    example_2 = [1, 1, 1, 1]

    print(solution.isPossibleToSplit(example_1))        # Output: True
    print(solution.isPossibleToSplit(example_2))        # Output: False
