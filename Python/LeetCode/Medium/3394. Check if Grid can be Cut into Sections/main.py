from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        """
        Determine whether two horizontal or two vertical cuts can be made on an n x n grid
        such that each resulting section contains at least one rectangle and every rectangle
        is fully contained in one section.

        Args:
            n (int): The size of the grid (n x n).
            rectangles (List[List[int]]): List of rectangles defined by [startx, starty, endx, endy].

        Returns:
            bool: True if such cuts exist, False otherwise.
        """

        def _check_cuts(rectangles: List[List[int]], dim: int) -> bool:
            """
            Check if two valid cuts can be made along a specified dimension.

            Args:
                rectangles (List[List[int]]): The input rectangles.
                dim (int): Dimension index to check cuts on (0 for x, 1 for y).

            Returns:
                bool: True if at least two cut points (gaps) are found.
            """
            gap_count = 0
            rectangles.sort(key=lambda rect: rect[dim])
            furthest_end = rectangles[0][dim + 2]

            for i in range(1, len(rectangles)):
                if furthest_end <= rectangles[i][dim]:
                    gap_count += 1
                furthest_end = max(furthest_end, rectangles[i][dim + 2])

            return gap_count >= 2

        return _check_cuts(rectangles, 0) or _check_cuts(rectangles, 1)


def main():
    sol = Solution()

    test_cases = [
        (5, [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]),  # True
        (4, [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]),  # True
        (4, [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]])  # False
    ]

    for idx, (n, rectangles) in enumerate(test_cases, 1):
        result = sol.checkValidCuts(n, rectangles)
        print(f"Test Case {idx}: {result}")

if __name__ == "__main__":
    main()
