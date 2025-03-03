from typing import List

class Solution:
    """
    Solution for partitioning an array according to a given pivot value.
    """

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """
        Rearranges nums such that:
        - All elements less than pivot appear first (in original order).
        - All elements equal to pivot appear next.
        - All elements greater than pivot appear last (in original order).

        :param nums: List[int] - The input array.
        :param pivot: int - The pivot value that elements are compared against.
        :return: List[int] - The rearranged array.
        """
        # Lists to store partitioned elements
        less_than_pivot = []
        equal_to_pivot = []
        greater_than_pivot = []

        # Partition elements into three categories
        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)
            elif num == pivot:
                equal_to_pivot.append(num)
            else:
                greater_than_pivot.append(num)

        # Concatenate the partitions to get the final result
        return less_than_pivot + equal_to_pivot + greater_than_pivot


def main():
    """
    Main function to test the pivotArray method with sample test cases.
    """
    solution = Solution()
    
    # Sample test cases
    test_cases = [
        ([9, 12, 5, 10, 14, 3, 10], 10),    # Expected output: [9, 5, 3, 10, 10, 12, 14]
        ([-3, 4, 3, 2], 2),                 # Expected output: [-3, 2, 4, 3]
        ([1, 2, 3, 4, 5], 3),               # Expected output: [1, 2, 3, 4, 5]
        ([5, 3, 1, 3, 2], 3)                # Expected output: [1, 2, 3, 3, 5]
    ]

    for nums, pivot in test_cases:
        print(f"Input: {nums}, Pivot: {pivot} → Output: {solution.pivotArray(nums, pivot)}")


if __name__ == "__main__":
    main()
