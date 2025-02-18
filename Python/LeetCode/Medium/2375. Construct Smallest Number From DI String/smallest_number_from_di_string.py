class Solution:
    """
    This class provides a solution to construct the lexicographically smallest number 
    that satisfies a given DI string pattern.
    
    The DI pattern consists of 'I' (increasing) and 'D' (decreasing), and the generated 
    number must follow these rules while using digits 1-9 exactly once.
    """

    def smallestNumber(self, pattern: str) -> str:
        """
        Generates the lexicographically smallest valid number that satisfies 
        the given DI pattern.

        :param pattern: A string consisting of 'I' (increasing) and 'D' (decreasing).
        :return: The smallest lexicographical valid number as a string.
        """

        result = []         # Stores the final output sequence
        stack = []          # Stack to help generate the smallest sequence

        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))        # Push the next number onto the stack

            # When we reach 'I' or the end of the pattern, pop the stack to form the result
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())

        return "".join(result)


def main():
    """
    Main function to demonstrate the smallestNumber function.
    """

    solution = Solution()

    # Example test cases
    test_cases = [
        ("IIIIDDD", "123549876"),
        ("DDD", "4321"),
        ("IDID", "13254"),
        ("DDIIDI", "3216547")
    ]

    for pattern, expected in test_cases:
        output = solution.smallestNumber(pattern)
        print(f"Pattern: {pattern} -> Smallest Number: {output} (Expected: {expected})")


if __name__ == "__main__":
    main()
