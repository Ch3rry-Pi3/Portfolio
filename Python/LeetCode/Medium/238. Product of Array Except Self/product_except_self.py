from typing import List

class Solution:
    """
    This class provides an implementation of the 'Product of Array Except Self' problem.

    The function returns an array such that each element at index `i` is equal to the product 
    of all the elements of `nums` except `nums[i]`, without using division.
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Computes the product of all elements except self in an array.

        :param nums: List of integers
        :return: List of integers where each element is the product of all others except itself
        """
        result = [1] * len(nums)

        # Compute prefix product for each element
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Compute postfix product and multiply it to result
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


def main():
    """
    Demonstrates computing the product of array except self for multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [1, 2, 3, 4],      # Expected output: [24, 12, 8, 6]
        [-1, 1, 0, -3, 3], # Expected output: [0, 0, 9, 0, 0]
        [4, 5, 1, 8, 2],   # Expected output: [80, 64, 320, 40, 160]
        [10, 3, 5, 6, 2],  # Expected output: [180, 600, 360, 300, 900]
    ]

    for nums in test_cases:
        print(f"nums = {nums}")
        result = solver.productExceptSelf(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
