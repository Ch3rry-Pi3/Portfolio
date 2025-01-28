from typing import List

class Solution:
    """
    This class provides an implementation of the 'Maximum Product Subarray' problem.
    
    The function finds the contiguous subarray that has the largest product and returns that product.
    """

    def maxProduct(self, nums: List[int]) -> int:
        """
        Finds the contiguous subarray with the largest product.

        :param nums: List of integers
        :return: Maximum product of any contiguous subarray
        """
        result = max(nums)                  # Start with the maximum value in nums to handle negative cases
        currentMin, currentMax = 1, 1       # Initialise min and max product to 1 (neutral value)

        for n in nums:
            tempMax = currentMax * n  # Store currentMax before modifying
            
            # Update currentMax and currentMin considering n
            currentMax = max(n * currentMax, n * currentMin, n)
            currentMin = min(tempMax, n * currentMin, n)

            # Update the result with the largest product found so far
            result = max(result, currentMax)

        return result


def main():
    """
    Demonstrates finding the maximum product subarray for multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [2, 3, -2, 4],              # Expected output: 6
        [-2, 0, -1],                # Expected output: 0
        [1, -2, -3, 4],             # Expected output: 12
        [-1, -3, -10, 0, 60],       # Expected output: 60
        [2, -5, 3, 1, -4, 0, -2],   # Expected output: 120
    ]

    for nums in test_cases:
        print(f"nums = {nums}")
        result = solver.maxProduct(nums)
        print(f"Maximum Product Subarray: {result}\n\n")


if __name__ == "__main__":
    main()
