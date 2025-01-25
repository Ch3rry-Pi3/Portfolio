class FibonacciRecursive:
    """
    This class provides an implementation of the Fibonacci sequence
    using a naive recursive approach.
    
    The function computes the nth Fibonacci number recursively,
    which is inefficient for large values of n.
    """

    def fib(self, n: int) -> int:
        """
        Computes the nth Fibonacci number recursively.

        :param n: A non-negative integer representing the position in the Fibonacci sequence.
        :return: The nth Fibonacci number.
        """
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


def main():
    """Runs the Fibonacci function with user input."""
    solver = FibonacciRecursive()
    n = int(input("Enter a number: "))
    print(f"Fibonacci({n}) = {solver.fib(n)}")


if __name__ == "__main__":
    main()