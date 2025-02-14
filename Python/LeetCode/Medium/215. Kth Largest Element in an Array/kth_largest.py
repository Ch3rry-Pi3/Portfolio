import heapq
from typing import List

class Solution:
    """
    A class to find the K-th largest element in an array using a min-heap.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the K-th largest element in an array.

        Args:
            nums (List[int]): A list of integers.
            k (int): The position (1-based) of the largest element to find.

        Returns:
            int: The K-th largest element in the array.
        """
        # Min-heap to store the k largest elements
        heap = []

        # Iterate through each number in the array
        for num in nums:
            heapq.heappush(heap, num)       # Push the number into the heap
            if len(heap) > k:               # If heap size exceeds k, pop the smallest element
                heapq.heappop(heap)

        # The root of the heap is the K-th largest element
        return heap[0]


def main():
    """Example usage of the `findKthLargest` function."""
    
    solution = Solution()

    # Example test cases
    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2),                # Expected output: 5
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),       # Expected output: 4
    ]

    for nums, k in test_cases:
        print(f"Input: nums={nums}, k={k} → K-th largest: {solution.findKthLargest(nums, k)}")

if __name__ == "__main__":
    main()
