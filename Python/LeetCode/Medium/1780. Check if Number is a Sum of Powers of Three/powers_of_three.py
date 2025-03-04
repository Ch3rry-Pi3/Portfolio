class Solution:
    """
    Solution to check if a number can be represented as a sum of distinct powers of three.
    """

    def checkPowersOfThree(self, n: int) -> bool:
        """
        Determines if n can be expressed as a sum of distinct powers of three.

        :param n: int - The number to check.
        :return: bool - True if possible, False otherwise.
        """
        while n > 0:
            # If n % 3 == 2, it requires duplicate powers of three (invalid case)
            if n % 3 == 2:
                return False
            # Move to the next higher power of three
            n //= 3
        return True


def main():
    """
    Main function to test the checkPowersOfThree method with sample test cases.
    """
    solution = Solution()
    
    # Sample test cases
    test_cases = [12, 91, 21, 27, 1, 3, 10]

    for n in test_cases:
        print(f"Input: {n} → Output: {solution.checkPowersOfThree(n)}")


if __name__ == "__main__":
    main()