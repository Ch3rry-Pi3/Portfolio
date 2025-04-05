from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        Calculate the sum of all subset XOR totals.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The sum of XOR totals for every subset of nums.
        """
        
        def XOR_sum(nums: List[int], index: int, current_XOR: int) -> int:
            """
            Recursive helper function to calculate the sum of XOR totals.

            Args:
                nums (List[int]): The list of integers.
                index (int): The current index in the list.
                current_XOR (int): The current XOR result.

            Returns:
                int: Sum of XOR totals for subsets including and excluding the current element.
            """
            # Base case: when all elements in nums are considered
            if index == len(nums):
                return current_XOR
            
            # Calculate sum of subset XOR with the current element included
            with_element = XOR_sum(nums, index + 1, current_XOR ^ nums[index])
            
            # Calculate sum of subset XOR without the current element
            without_element = XOR_sum(nums, index + 1, current_XOR)
            
            # Return the sum of both possibilities
            return with_element + without_element

        return XOR_sum(nums, 0, 0)


def main():
    solution = Solution()
    test_cases = [
        ([1, 3], 6),
        ([5, 1, 6], 28),
        ([3, 4, 5, 6, 7, 8], 480),
        ([0], 0),
        ([1, 2, 3], 12)
    ]

    for nums, expected in test_cases:
        result = solution.subsetXORSum(nums)
        print(f"Input: {nums}\nExpected: {expected}, Got: {result}\n")


if __name__ == "__main__":
    main()
