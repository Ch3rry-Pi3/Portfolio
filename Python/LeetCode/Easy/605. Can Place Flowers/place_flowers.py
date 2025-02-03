from typing import List

class Solution:
    """
    This class provides a method to determine if a given number of flowers can be placed 
    in a flowerbed without violating the no-adjacent-flowers rule.
    """

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Determines whether 'n' flowers can be planted in the flowerbed without violating 
        the no-adjacent-flowers rule.

        :param flowerbed: List[int] - A list representing the flowerbed, where:
                         - 0 means an empty plot
                         - 1 means an occupied plot
        :param n: int - The number of flowers to plant.
        :return: bool - True if 'n' flowers can be placed, otherwise False.
        """
        # Add virtual empty plots at both ends to simplify edge cases
        f = [0] + flowerbed + [0]

        # Iterate through the flowerbed, skipping the first and last (virtual) plots
        for i in range(1, len(f) - 1):
            # Check if the current plot and its neighbors are empty
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                # Plant a flower and reduce the count of flowers left to plant
                f[i] = 1
                n -= 1
            
            # If all required flowers have been planted, return True early
            if n <= 0:
                return True

        return n <= 0               # Return True if all flowers have been placed, otherwise False


def main():
    """
    Demonstrates testing the canPlaceFlowers function with sample test cases.
    """
    solver = Solution()

    test_cases = [
        ([1, 0, 0, 0, 1], 1),  # Expected: True
        ([1, 0, 0, 0, 1], 2),  # Expected: False
        ([0, 0, 1], 1),        # Expected: True
        ([0, 0, 0, 0, 0], 2)   # Expected: True
    ]

    for flowerbed, n in test_cases:
        print(f"Input: flowerbed = {flowerbed}, n = {n}")
        result = solver.canPlaceFlowers(flowerbed, n)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
