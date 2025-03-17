from collections import Counter
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        """
        Determines whether the given list of numbers can be divided into equal pairs.
        
        :param nums: List of integers with length 2 * n.
        :return: True if nums can be divided into pairs where elements in each pair are equal, otherwise False.
        """
        # Count frequency of each number in nums
        frequency = Counter(nums)

        # Check if all numbers appear an even number of times
        return all(count % 2 == 0 for count in frequency.values())

def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        [3, 2, 3, 2, 2, 2],         # Expected Output: True
        [1, 2, 3, 4],               # Expected Output: False
        [5, 5, 6, 6, 7, 7],         # Expected Output: True
        [1, 1, 1, 2, 2, 2],         # Expected Output: True
        [4, 4, 4, 4, 4, 4]          # Expected Output: True
    ]

    for nums in test_cases:
        result = solution.divideArray(nums)
        print(f"Input: {nums} -> Output: {result}")

if __name__ == "__main__":
    main()
