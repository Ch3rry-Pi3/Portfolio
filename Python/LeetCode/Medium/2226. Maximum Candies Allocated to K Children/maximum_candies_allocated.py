from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
        Determines the maximum number of candies each child can receive 
        while ensuring that all k children receive the same number of candies.
        
        :param candies: List of integers representing available candy piles.
        :param k: Number of children.
        :return: Maximum number of candies each child can get.
        """
        if sum(candies) < k:
            return 0  # If total candies are less than k, distribution is impossible
        
        left, right = 1, max(candies)

        # Binary search for the largest number of candies each child can get
        while left < right:
            mid = (left + right + 1) // 2
            if self._can_allocate_candies(candies, k, mid):
                left = mid              # Try a higher number
            else:
                right = mid - 1         # Reduce the number

        return left

    def _can_allocate_candies(self, candies: List[int], k: int, num_of_candies: int) -> bool:
        """
        Helper function to check if it's possible to allocate candies such that 
        each child gets exactly 'num_of_candies' candies.
        
        :param candies: List of candy piles.
        :param k: Number of children.
        :param num_of_candies: Number of candies per child.
        :return: True if possible, False otherwise.
        """
        total_children_served = sum(pile // num_of_candies for pile in candies)
        return total_children_served >= k

def main():
    solution = Solution()

    test_cases = [
        ([5, 8, 6], 3),         # Expected Output: 5
        ([2, 5], 11),           # Expected Output: 0
        ([10, 15, 20], 5)       # Expected Output: 6
    ]

    for candies, k in test_cases:
        result = solution.maximumCandies(candies, k)
        print(f"Input: candies={candies}, k={k} -> Output: {result}")

if __name__ == "__main__":
    main()
