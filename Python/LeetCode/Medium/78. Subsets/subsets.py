from typing import List

class Solution:
    """
    This class provides a solution to generate all possible subsets of a given list of unique integers.
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Returns all possible subsets (the power set) of a given list of unique integers.

        :param nums: List of unique integers.
        :return: List of all possible subsets.
        """

        n = len(nums)
        result, solution = [], []

        def backtrack(i: int):
            """
            Backtracking function to generate all subsets.

            :param i: Current index in the nums list.
            """
            if i == n:
                result.append(solution[:])          # Store a copy of the current subset
                return

            # Exclude the current element and move to the next
            backtrack(i + 1)

            # Include the current element
            solution.append(nums[i])
            backtrack(i + 1)

            # Backtrack by removing the last element
            solution.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    # Example usage
    solution = Solution()

    # Test cases
    print(solution.subsets([1, 2, 3]))          # Expected: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(solution.subsets([0]))                # Expected: [[], [0]]
