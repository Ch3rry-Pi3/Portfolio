from typing import List

class Solution:
    """
    This class provides an implementation of the 'Combination Sum' problem.

    The function `combinationSum` finds all unique combinations of numbers from `candidates` 
    that sum up to `target`, where each number can be used an unlimited number of times.
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations where the sum equals `target` using numbers from `candidates`.
        
        :param candidates: List of distinct integers.
        :param target: Target sum for the combinations.
        :return: List of all unique combinations that sum to `target`.
        """
        results = []  # Stores valid combinations

        def dfs(remaining_sum: int, combination: List[int], cursor_start: int):
            """
            Depth-first search (DFS) helper function to explore combinations.
            
            :param remaining_sum: Remaining value to reach the target.
            :param combination: Current combination of numbers.
            :param cursor_start: Index to start the search (ensures numbers can be reused).
            """
            if remaining_sum == 0:
                # Found a valid combination, store a copy of it
                results.append(list(combination))
                return
            elif remaining_sum < 0:
                # If the sum exceeds target, stop searching
                return

            # Iterate over candidates starting from cursor_start
            for i in range(cursor_start, len(candidates)):
                # Add candidate[i] to the current combination
                combination.append(candidates[i])
                # Recursively explore further with the updated sum and same index (allow reuse)
                dfs(remaining_sum - candidates[i], combination, i)
                # Backtrack: Remove the last added number to explore other possibilities
                combination.pop()

        # Start DFS with an empty combination
        dfs(remaining_sum=target, combination=[], cursor_start=0)

        return results


def main():
    """
    Demonstrates testing the combinationSum function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        ([2, 3, 6, 7], 7),      # Expected: [[2,2,3], [7]]
        ([2, 3, 5], 8),         # Expected: [[2,2,2,2], [2,3,3], [3,5]]
        ([2], 1),               # Expected: []
        ([1], 1),               # Expected: [[1]]
        ([1], 2),               # Expected: [[1,1]]
    ]

    for candidates, target in test_cases:
        print(f"Input: candidates = {candidates}, target = {target}")
        result = solver.combinationSum(candidates, target)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
