from typing import *
import collections

class Solution:
    def countLargestGroup(self, n: int) -> int:
        """
        Groups numbers from 1 to n by the sum of their digits.
        Returns the number of groups with the largest size.
        """
        hashMap = collections.Counter()
        
        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            hashMap[digit_sum] += 1
        
        max_group_size = max(hashMap.values())
        largest_group_count = sum(1 for size in hashMap.values() if size == max_group_size)
        
        return largest_group_count


def main():
    solution = Solution()
    test_cases = [
        (13, 4),  # Example 1
        (2, 2),   # Example 2
        (24, 4),  # Additional test case
        (1, 1),   # Edge case: only one number
    ]
    
    for n, expected in test_cases:
        result = solution.countLargestGroup(n)
        print(f"Input: n = {n}\nExpected: {expected}, Got: {result}\n")


if __name__ == "__main__":
    main()
