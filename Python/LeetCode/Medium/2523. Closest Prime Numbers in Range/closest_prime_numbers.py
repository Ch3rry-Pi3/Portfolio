from typing import List, Tuple

class Solution:
    """
    Solution to find the closest pair of prime numbers in a given range.
    """

    def _sieve(self, upper_limit: int) -> List[bool]:
        """
        Implements the Sieve of Eratosthenes to find prime numbers up to a given limit.

        :param upper_limit: int - The upper bound for prime number checking.
        :return: List[bool] - Boolean list where True represents a prime number.
        """
        sieve = [True] * (upper_limit + 1)
        sieve[0] = sieve[1] = False         # 0 and 1 are not prime

        for number in range(2, int(upper_limit**0.5) + 1):
            if sieve[number]:
                for multiple in range(number * number, upper_limit + 1, number):
                    sieve[multiple] = False
        return sieve

    def closestPrimes(self, left: int, right: int) -> Tuple[int, int]:
        """
        Finds the closest pair of prime numbers within the given range.

        :param left: int - Lower bound of the range.
        :param right: int - Upper bound of the range.
        :return: Tuple[int, int] - The closest prime pair, or (-1, -1) if no valid pair exists.
        """
        # Step 1: Compute all prime numbers up to 'right'
        sieve_array = self._sieve(right)

        # Step 2: Filter primes within the given range
        prime_numbers = [num for num in range(left, right + 1) if sieve_array[num]]

        # Step 3: Find the closest prime pair
        if len(prime_numbers) < 2:
            return -1, -1       # If there are fewer than two primes, return [-1, -1]

        min_difference = float("inf")
        closest_pair = (-1, -1)

        for index in range(1, len(prime_numbers)):
            difference = prime_numbers[index] - prime_numbers[index - 1]
            if difference < min_difference:
                min_difference = difference
                closest_pair = (prime_numbers[index - 1], prime_numbers[index])

        return closest_pair


def main():
    """
    Runs sample test cases for the closest prime numbers function.
    """
    solution = Solution()

    # Sample test cases
    test_cases = [(10, 19), (4, 6), (1, 100), (100, 200)]

    for left, right in test_cases:
        print(f"Input: left={left}, right={right} → Output: {solution.closestPrimes(left, right)}")


if __name__ == "__main__":
    main()
