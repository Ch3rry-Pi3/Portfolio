from typing import List

class Solution:
    """
    This class provides an implementation of the 'Container With Most Water' problem.

    The goal is to find two lines that form a container with the largest possible water area.
    We solve this using a **two-pointer approach** to maximize efficiency (O(n) time complexity).
    """

    def maxArea(self, height: List[int]) -> int:
        """
        Computes the maximum amount of water that can be stored between two lines.

        :param height: List of heights representing vertical lines
        :return: Maximum water container area
        """
        result = 0  # Stores the maximum area found
        left, right = 0, len(height) - 1  # Two-pointer approach

        while left < right:
            # Calculate the area between left and right pointers
            area = (right - left) * min(height[left], height[right])
            result = max(result, area)  # Update max area if this one is greater

            # Move the pointer pointing to the smaller height (or both if equal)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result


def main():
    """
    Demonstrates testing the maxArea function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],  # Expected output: 49
        [1, 1],  # Expected output: 1
        [4, 3, 2, 1, 4],  # Expected output: 16
        [1, 2, 1],  # Expected output: 2
    ]

    for heights in test_cases:
        print(f"Height array: {heights}")
        result = solver.maxArea(heights)
        print(f"Max water container area: {result}\n")


if __name__ == "__main__":
    main()
