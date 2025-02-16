class Solution:
    def can_partition(self, num: int, target: int) -> bool:
        """
        Recursively checks if the given number's square can be partitioned
        into contiguous substrings that sum up to the target value.

        Args:
            num (int): The square of a number.
            target (int): The original number to match by partitioning.

        Returns:
            bool: True if a valid partition exists, False otherwise.
        """
        # Invalid partition found
        if target < 0 or num < target:
            return False

        # Valid partition found
        if num == target:
            return True

        # Recursively check all partitions for a valid partition
        return (
            self.can_partition(num // 10, target - num % 10)
            or self.can_partition(num // 100, target - num % 100)
            or self.can_partition(num // 1000, target - num % 1000)
        )

    def punishmentNumber(self, n: int) -> int:
        """
        Calculates the punishment number for a given integer n.

        The punishment number is the sum of the squares of numbers in the range
        [1, n] whose squared values can be partitioned into contiguous substrings
        summing to the original number.

        Args:
            n (int): The upper limit of the range.

        Returns:
            int: The punishment number.
        """
        punishment_num = 0

        # Iterate through numbers in range [1, n]
        for current_num in range(1, n + 1):
            square_num = current_num * current_num

            # Check if valid partition can be found and add squared number if so
            if self.can_partition(square_num, current_num):
                punishment_num += square_num

        return punishment_num


if __name__ == "__main__":
    solution = Solution()
    test_value = 10  # Example input
    print(f"Punishment number of {test_value}: {solution.punishmentNumber(test_value)}")
