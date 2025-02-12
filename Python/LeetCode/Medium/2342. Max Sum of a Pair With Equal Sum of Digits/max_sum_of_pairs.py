from typing import List

class Solution:
    def calculate_digit_sum(self, num: int) -> int:
        """
        Computes the sum of digits of a given number.

        Args:
            num (int): The input number.

        Returns:
            int: The sum of the digits of the number.
        """
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def maximumSum(self, nums: List[int]) -> int:
        """
        Finds the maximum sum of a pair of numbers in the list where both numbers have the same digit sum.

        Args:
            nums (List[int]): A list of positive integers.

        Returns:
            int: The maximum sum of a pair with the same digit sum, or -1 if no such pair exists.
        """
        digit_sum_pairs = []

        # Store numbers with their digit sums as pairs
        for number in nums:
            digit_sum = self.calculate_digit_sum(number)
            digit_sum_pairs.append((digit_sum, number))

        # Sort based on digit sums, and if equal, by number value
        digit_sum_pairs.sort()

        max_pair_sum = -1

        # Iterate through the sorted array to find the maximum sum of pairs
        for index in range(1, len(digit_sum_pairs)):
            current_digit_sum = digit_sum_pairs[index][0]
            previous_digit_sum = digit_sum_pairs[index - 1][0]

            # If two consecutive numbers have the same digit sum
            if current_digit_sum == previous_digit_sum:
                current_sum = digit_sum_pairs[index][1] + digit_sum_pairs[index - 1][1]
                max_pair_sum = max(max_pair_sum, current_sum)

        return max_pair_sum


if __name__ == "__main__":
    # Example test cases
    solution = Solution()
    test_cases = [
        ([18, 43, 36, 13, 7], 54),
        ([10, 12, 19, 14], -1),
    ]

    for nums, expected in test_cases:
        result = solution.maximumSum(nums)
        print(f"Input: {nums} | Expected: {expected} | Output: {result}")
