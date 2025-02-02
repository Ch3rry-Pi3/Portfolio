from typing import List

class Solution:
    """
    A class to reverse the bits of a given 32-bit unsigned integer.
    """

    def reverseBits(self, n: int) -> int:
        """
        Reverses the bits of a given 32-bit unsigned integer.

        :param n: An integer representing a 32-bit unsigned value.
        :return: The integer obtained after reversing its bits.
        """
        result = 0  # This will store the reversed binary representation.

        for i in range(32):             # Loop through all 32 bits.
            result = result << 1        # Shift result left by 1 to make space for the new bit.
            bit = n & 1                 # Extract the least significant bit of n.
            result += bit               # Append the extracted bit to the result.
            n = n >> 1                  # Shift n to the right to process the next bit.

        return result

def main():
    """Demonstrates the reverseBits function with a sample input."""
    solution = Solution()
    
    # Example input: Binary representation of 43261596 (00000010100101000001111010011100)
    n = 43261596
    reversed_bits = solution.reverseBits(n)
    
    print(f"Original: {bin(n)} ({n})")
    print(f"Reversed: {bin(reversed_bits)} ({reversed_bits})")

if __name__ == "__main__":
    main()
