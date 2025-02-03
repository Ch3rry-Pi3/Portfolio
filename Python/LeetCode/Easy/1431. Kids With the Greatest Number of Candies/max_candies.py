from typing import List

class Solution:
    """
    This class provides a method to determine which kids can have the greatest 
    number of candies if given extra candies.
    """

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Determines whether each kid can have the greatest number of candies if given extra candies.

        :param candies: List of integers representing the number of candies each child has.
        :param extraCandies: Integer representing extra candies available to be distributed.
        :return: List of booleans where True means the child can have the most candies.
        """

        # Find the maximum number of candies a kid currently has
        max_candy = max(candies)

        # Iterate through the list and check if a kid can have the most candies
        return [candy + extraCandies >= max_candy for candy in candies]


def main():
    """
    Demonstrates testing the kidsWithCandies function with sample test cases.
    """
    solver = Solution()

    test_cases = [
        ([2, 3, 5, 1, 3], 3),   # Expected: [True, True, True, False, True]
        ([4, 2, 1, 1, 2], 1),   # Expected: [True, False, False, False, False]
        ([12, 1, 12], 10)       # Expected: [True, False, True]
    ]

    for candies, extra in test_cases:
        print(f"Input: candies = {candies}, extraCandies = {extra}")
        result = solver.kidsWithCandies(candies, extra)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
