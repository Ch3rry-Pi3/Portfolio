from typing import List

def longest_subarray(nums: List[int]) -> int:
    """
    Finds the longest subarray of 1's after deleting exactly one element.
    
    Args:
        nums (List[int]): A binary list containing 0s and 1s.
    
    Returns:
        int: The length of the longest subarray of 1's after removing one element.
    """
    n = len(nums)                   # The size of the input array
    left = 0                        # The left pointer of the sliding window
    zeros = 0                       # Number of zeroes encountered
    max_length = 0                  # Maximum length of the subarray

    for right in range(n):
        if nums[right] == 0:
            zeros += 1              # Increment the count of zeroes

        # Adjust the window to maintain at most one zero in the subarray
        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1          # Decrement the count of zeroes
            left += 1               # Move the left pointer to the right

        # Calculate the length of the current subarray and update max_length
        max_length = max(max_length, right - left + 1 - zeros)

    # If the entire array is 1s, return size minus one; otherwise, return max_length
    return max_length - 1 if max_length == n else max_length

def main():
    """Runs example test cases for the longest_subarray function."""
    test_cases = [
        ([1, 1, 0, 1], 3),
        ([0, 1, 1, 0, 1, 1, 1, 0, 1], 5),
        ([1, 1, 1], 2),
        ([0, 0, 0], 0),
        ([1, 0, 1, 1, 1, 0, 1, 1], 5),
    ]

    for nums, expected in test_cases:
        result = longest_subarray(nums)
        print(f"nums: {nums} → Expected: {expected}, Got: {result}")

if __name__ == "__main__":
    main()
