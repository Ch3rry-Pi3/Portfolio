from typing import List

def calPoints(operations: List[str]) -> int:
    """
    Computes the sum of all scores on the record after applying operations.
    
    :param operations: List of operations to apply.
    :return: Sum of all scores after applying the operations.
    """
    stack = []
    
    for op in operations:
        if op == "C":
            stack.pop()
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))
    
    return sum(stack)

def main():
    """Runs example test cases for the calPoints function."""
    test_cases = [
        (["5", "2", "C", "D", "+"], 30),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
        (["1", "C"], 0)
    ]
    
    for i, (ops, expected) in enumerate(test_cases, 1):
        result = calPoints(ops)
        print(f"Test Case {i}: {'Passed' if result == expected else 'Failed'} (Output: {result}, Expected: {expected})")

if __name__ == "__main__":
    main()
