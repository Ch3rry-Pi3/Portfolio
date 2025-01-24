class FibonacciRecursive:
    def fib(self, n: int) -> int:
        """Computes Fibonacci number recursively (inefficient)."""
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

if __name__ == "__main__":
    solver = FibonacciRecursive()
    n = int(input("Enter a number: "))
    print(f"Fibonacci({n}) = {solver.fib(n)}")