"""
LeetCode 1980: Find Unique Binary String

Given an array of n unique binary strings of length n, return a binary string of
length n that does NOT appear in the given list.

If multiple answers exist, return any of them.
"""

from typing import List

def findDifferentBinaryString(nums: List[str]) -> str:
    """
    Finds a binary string of length n that does not appear in nums.

    This solution constructs a unique binary string using the diagonal elements 
    of nums and flipping their bits.

    Args:
        nums (List[str]): A list of unique binary strings of length n.

    Returns:
        str: A binary string of length n that is not in nums.
    """
    n = len(nums)
    return "".join("1" if nums[i][i] == "0" else "0" for i in range(n))

if __name__ == "__main__":
    # Example cases
    example_1 = ["01", "10"]
    example_2 = ["00", "01"]
    example_3 = ["111", "011", "001"]

    print(findDifferentBinaryString(example_1))  # Output: "11" or "00"
    print(findDifferentBinaryString(example_2))  # Output: "11" or "10"
    print(findDifferentBinaryString(example_3))  # Output: "101" or another valid binary string
