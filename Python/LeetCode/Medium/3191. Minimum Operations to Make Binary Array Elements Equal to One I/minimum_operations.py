from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Computes the minimum number of operations required to make all elements in nums equal to 1.
        If it is impossible, returns -1.

        :param nums: A binary array (list of 0s and 1s).
        :return: The minimum number of operations or -1 if it's impossible.
        """
        n = len(nums)
        count = 0

        # Iterate through the array, flipping groups of three where needed
        for i in range(n - 2):
            if nums[i] == 0:
                # Flip the current element and the next two
                nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                nums[i + 2] = 1 if nums[i + 2] == 0 else 0
                count += 1  # Increment the number of operations

        # If the last two elements are still 0, it's impossible
        if nums[n - 2] == 0 or nums[n - 1] == 0:
            return -1

        return count

def main():
    """
    Driver function to test the minOperations function with sample inputs.
    """
    solution = Solution()

    # Example test cases
    test_cases = [
        ([0, 1, 1, 1, 0, 0], 3),
        ([0, 1, 1, 1], -1),
        ([1, 1, 1], 0),
        ([0, 0, 0, 0, 0, 0], -1),
        ([1, 0, 0, 1, 0, 0, 1], 3)
    ]

    for nums, expected in test_cases:
        result = solution.minOperations(nums.copy())  # Use copy to avoid modifying original
        print(f"Input: {nums} -> Output: {result} (Expected: {expected})")

if __name__ == "__main__":
    main()
