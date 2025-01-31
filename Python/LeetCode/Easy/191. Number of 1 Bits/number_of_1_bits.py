class Solution:
    """
    This class provides an implementation of the 'Number of 1 Bits' problem.

    The goal is to count the number of `1` bits in the binary representation of an integer (Hamming Weight).
    We use a **bitwise approach** for optimal efficiency (`O(log n)` time complexity).
    """

    def hammingWeight(self, n: int) -> int:
        """
        Counts the number of `1` bits in the binary representation of `n`.

        :param n: Unsigned integer
        :return: Number of 1 bits (Hamming Weight)
        """
        result = 0

        while n:
            result += n % 2     # Add 1 if the least significant bit (LSB) is 1
            n = n >> 1          # Right shift `n` to process the next bit

        return result


def main():
    """
    Demonstrates testing the hammingWeight function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        11,         # Binary: 1011 → Expected output: 3
        128,        # Binary: 10000000 → Expected output: 1
        2147483645, # Binary: 1111111111111111111111111111101 → Expected output: 30
    ]

    for num in test_cases:
        print(f"Input: {num} (Binary: {bin(num)[2:]})")
        result = solver.hammingWeight(num)
        print(f"Number of 1 bits: {result}\n")


if __name__ == "__main__":
    main()
