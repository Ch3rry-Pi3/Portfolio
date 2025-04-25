from typing import Tuple

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """
        Returns the number of symmetric integers between low and high (inclusive).
        A symmetric integer has an even number of digits and the sum of the first
        half equals the sum of the second half.
        """
        res = 0
        for a in range(low, high + 1):
            if a < 100 and a % 11 == 0:
                res += 1
            elif 1000 <= a < 10000:
                left = a // 1000 + (a % 1000) // 100
                right = (a % 100) // 10 + a % 10
                if left == right:
                    res += 1
        return res


def main():
    solution = Solution()
    test_cases: list[Tuple[int, int, int]] = [
        (1, 100, 9),
        (1200, 1230, 4),
        (10, 10, 0),
        (1000, 1001, 0),
        (1000, 9999, 90),  # From 1001 to 9999 there are 90 symmetric integers
    ]

    for low, high, expected in test_cases:
        result = solution.countSymmetricIntegers(low, high)
        print(f"Input: low={low}, high={high}\nExpected: {expected}, Got: {result}\n")


if __name__ == "__main__":
    main()
