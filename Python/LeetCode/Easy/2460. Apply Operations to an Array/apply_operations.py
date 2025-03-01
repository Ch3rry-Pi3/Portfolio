from typing import List

class Solution:
    """
    Solution class for applying operations on an array.
    """

    def applyOperations(self, nums: List[int]) -> List[int]:
        """
        Applies the given operations on the nums array.

        - If two adjacent elements are equal, multiply the first by 2 and set the second to 0.
        - Shift all non-zero elements to the front, maintaining order.

        :param nums: List[int] - The input array of non-negative integers.
        :return: List[int] - The transformed array.
        """
        n = len(nums)
        write_index = 0  # Pointer to place non-zero elements

        for index in range(n):
            # Step 1: Merge adjacent equal elements if they are non-zero
            if index < n - 1 and nums[index] == nums[index + 1] and nums[index] != 0:
                nums[index] *= 2
                nums[index + 1] = 0

            # Step 2: Shift non-zero elements to the front
            if nums[index] != 0:
                if index != write_index:
                    nums[index], nums[write_index] = nums[write_index], nums[index]
                write_index += 1

        return nums


def main():
    """
    Main function to test the applyOperations method with sample test cases.
    """
    solution = Solution()
    
    # Sample test cases
    test_cases = [
        [1, 2, 2, 1, 1, 0],         # Expected output: [1, 4, 2, 0, 0, 0]
        [0, 1],                     # Expected output: [1, 0]
        [2, 2, 0, 4, 4, 8],         # Expected output: [4, 8, 8, 0, 0, 0]
        [0, 0, 0, 0]                # Expected output: [0, 0, 0, 0]
    ]

    for nums in test_cases:
        print(f"Input: {nums} → Output: {solution.applyOperations(nums)}")


if __name__ == "__main__":
    main()
