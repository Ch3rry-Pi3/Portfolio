import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Finds the minimum number of operations needed to make all elements 
        in the array greater than or equal to k.

        In each operation:
        1. Remove the two smallest numbers x and y from the heap.
        2. Add a new number calculated as min(x, y) * 2 + max(x, y).
        3. Repeat until all elements in the array are ≥ k.

        Parameters:
        nums (List[int]): A list of integers.
        k (int): The threshold value.

        Returns:
        int: The minimum number of operations needed.
        """
        # Convert the list into a min-heap for efficient retrieval of the smallest elements
        heapq.heapify(nums)

        num_operations = 0
        while nums[0] < k:
            # Extract the two smallest elements
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            # Compute the new value and push it back into the heap
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))

            # Increment operation count
            num_operations += 1

        return num_operations


def main():
    """
    Main function to demonstrate the minOperations function with sample inputs.
    """
    solution = Solution()

    # Sample test cases
    test_cases = [
        ([2, 11, 10, 1, 3], 10),
        ([1, 1, 2, 4, 9], 20),
        ([5, 7, 8], 10),
        ([1, 2], 5),
    ]

    for nums, k in test_cases:
        result = solution.minOperations(nums, k)
        print(f"Input: nums = {nums}, k = {k} → Output: {result}")


# Run the script only if executed directly
if __name__ == "__main__":
    main()
