from typing import List

class Solution:
    """
    This class provides a solution for the Climbing Stairs problem.
    
    The problem follows a Fibonacci-like sequence where each step can be reached 
    from the previous step (n-1) or the step before that (n-2).
    
    The goal is to determine how many distinct ways there are to climb 'n' steps.
    """

    def climbStairs(self, n: int) -> int:
        """
        Computes the number of distinct ways to climb 'n' stairs.

        :param n: The total number of steps.
        :return: The number of unique ways to climb to the top.
        """
        # Base cases: Only one way to reach step 0 or step 1
        one, two = 1, 1

        # Iterating from the second-to-last step down to the first step
        for _ in range(n - 1):
            temp = one
            one = one + two         # Update the step count based on previous two steps
            two = temp              # Shift values forward
        
        return one


def main():
    """
    Runs test cases for the climbStairs function.
    """
    solver = Solution()
    
    test_cases = [
        2,          # Expected: 2
        3,          # Expected: 3
        4,          # Expected: 5
        5,          # Expected: 8
        6           # Expected: 13
    ]

    for n in test_cases:
        print(f"Input: n = {n}")
        result = solver.climbStairs(n)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
