from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Finds two numbers in a sorted list that sum up to the target.

        Args:
            numbers (List[int]): A 1-indexed sorted array of integers.
            target (int): The target sum.

        Returns:
            List[int]: The indices of the two numbers, incremented by one.
        """
        # Initialise two pointers
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            # If the sum matches the target, return the indices (1-based)
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum > target:
                # Move the right pointer left to reduce the sum
                right -= 1
            else:
                # Move the left pointer right to increase the sum
                left += 1

        # Return an invalid result (not expected, as per problem constraints)
        return [-1, -1]


if __name__ == "__main__":
    solution = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(f"Indices: {solution.twoSum(numbers, target)}")
