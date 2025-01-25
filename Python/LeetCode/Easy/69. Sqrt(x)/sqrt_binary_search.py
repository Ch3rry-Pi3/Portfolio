class Solution:
    """
    This class provides an implementation of the square root function using binary search.
    The function computes the integer square root of a given non-negative integer x.
    """

    def mySqrt(self, x: int) -> int:
        """
        Computes the square root of x rounded down to the nearest integer
        using binary search.

        :param x: A non-negative integer
        :return: The integer square root of x
        """
        left, right = 0, x
        result = 0

        while left <= right:
            middle = left + ((right - left) // 2)
            if middle * middle > x:
                right = middle - 1
            elif middle * middle < x:
                left = middle + 1
                result = middle
            else:
                return middle
        return result


def main():
    """Runs the square root function with user input."""
    solver = Solution()
    x = int(input("Enter a number: "))
    print(f"Square root of {x} (rounded down) = {solver.mySqrt(x)}")


if __name__ == "__main__":
    main()