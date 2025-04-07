from typing import List
from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        Finds the shortest distance from an empty land (0) to all buildings (1) in a grid.
        Returns -1 if no such point exists.
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        totalBuildings = 0
        buildings = []

        # Step 1: Identify building positions and initialize empty land cells
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    buildings.append((i, j))
                    totalBuildings += 1
                if grid[i][j] == 0:
                    grid[i][j] = [0, 0]  # Transform 0 cells into [buildings_count, total_distance]

        def bfs(start):
            """ Perform BFS from a building to calculate distances to empty lands """
            initialRow, initialCol = start
            q = deque([(initialRow, initialCol, 0)])
            visited = set([(initialRow, initialCol)])
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

            while q:
                row, col, distance = q.popleft()
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    if 0 <= newRow < ROWS and 0 <= newCol < COLS and (newRow, newCol) not in visited:
                        if grid[newRow][newCol] == 0 or isinstance(grid[newRow][newCol], list):
                            grid[newRow][newCol][0] += 1                # Increment buildings count
                            grid[newRow][newCol][1] += distance + 1      # Increment travel distance
                            q.append((newRow, newCol, distance + 1))
                            visited.add((newRow, newCol))

        # Step 2: Perform BFS from each building
        for building in buildings:
            bfs(building)

        # Step 3: Find the minimum travel distance from all empty lands that are accessible from all buildings
        shortestDistance = float('inf')
        for i in range(ROWS):
            for j in range(COLS):
                if isinstance(grid[i][j], list) and grid[i][j][0] == totalBuildings:
                    shortestDistance = min(shortestDistance, grid[i][j][1])

        return shortestDistance if shortestDistance != float('inf') else -1

def main():
    solution = Solution()
    test_cases = [
        ([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]], 7),
        ([[1, 0]], 1),
        ([[1, 1]], -1),
        ([[0, 2], [1, 0]], -1)
    ]

    for grid, expected in test_cases:
        result = solution.shortestDistance(grid)
        print(f"Input Grid: {grid}\nExpected: {expected}, Got: {result}\n")

if __name__ == "__main__":
    main()
