class FibonacciOptimized:
    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        """Computes Fibonacci number using memoization (efficient)."""
        if n in self.memo:
            return self.memo[n]
        if n <= 1:
            return n
        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]

if __name__ == "__main__":
    solver = FibonacciOptimized()
    n = int(input("Enter a number: "))
    print(f"Fibonacci({n}) = {solver.fib(n)}")
