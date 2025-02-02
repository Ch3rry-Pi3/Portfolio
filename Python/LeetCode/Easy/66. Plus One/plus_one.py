from typing import List

class Solution:
    """
    Solution class for the 'Plus One' problem.

    This method increments an integer represented as a list of digits by 1, handling cases like carry propagation.
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Increments the given list of digits by one.

        :param digits: List of integers representing a number.
        :return: A new list representing the incremented number.
        """
        digits = digits[::-1]           # Reverse the list to handle least significant digit first
        carry, i = 1, 0                 # Start with carry set to 1 since we are adding one

        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0       # Set current digit to 0 if it's 9, propagate carry
                else:
                    digits[i] += 1      # Simply increment the digit if it's not 9
                    carry = 0           # Carry handled, so stop
            else:
                digits.append(1)        # If carry still remains, add a new digit at the end
                carry = 0

            i += 1                      # Move to the next digit

        return digits[::-1]             # Reverse back to original order

def main():
    """
    Demonstrates the plusOne function on multiple test cases.
    """
    solver = Solution()

    test_cases = [
        [1, 2, 3],              # Expected: [1, 2, 4]
        [4, 3, 2, 1],           # Expected: [4, 3, 2, 2]
        [9],                    # Expected: [1, 0]
        [9, 9, 9],              # Expected: [1, 0, 0, 0]
    ]

    for digits in test_cases:
        print(f"Input: {digits}")
        result = solver.plusOne(digits)
        print(f"Output: {result}\n")

if __name__ == "__main__":
    main()
