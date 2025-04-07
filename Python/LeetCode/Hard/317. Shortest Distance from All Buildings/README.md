# 🧾 **LeetCode 317: Shortest Distance from All Buildings**  

## 📌 **Problem Overview**  

You are given a grid of values `0`, `1`, or `2`, where:  
- `0` represents **empty land** that you can pass through freely.  
- `1` represents a **building** that you cannot pass through.  
- `2` represents an **obstacle** that you cannot pass through.  

Your task is to find the **shortest total travel distance** to all buildings from an empty land.  
- You can only move **up, down, left, or right**.  
- If it is not possible to build a house that reaches all buildings, return `-1`.  

### **Objective:**  
Return the **shortest travel distance** from an empty land to all buildings.  
If no valid location exists, return `-1`.  



## ✅ **Example**  

### **Input:**  
```
grid = [[1, 0, 2, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]]
```

### **Output:**  
```
7
```

### **Explanation:**  
Given three buildings at `(0,0)`, `(0,4)`, `(2,2)`, and an obstacle at `(0,2)`.  
The optimal point to build a house is `(1,2)`, as the **total travel distance** of `3+3+1=7` is minimal.  



## 🛠 **Approach & Intuition**  

### 🔍 **Step-by-Step:**  
1. **Identify Building Positions:**  
   - Traverse the grid and collect all coordinates of buildings (`1`).  
   - Count the **total number of buildings**.  

2. **BFS for Distance Calculation:**  
   - For each building, perform **Breadth-First Search (BFS)** to calculate distances to each reachable empty land (`0`).  
   - Keep track of:
     - **Number of buildings visited** from each land point.  
     - **Total distance** from each land point to all visited buildings.  

3. **Calculate Minimum Distance:**  
   - Check each empty land point to see if it is reachable from **all buildings**.  
   - Return the **minimum travel distance** among valid points.  
   - If no such point exists, return `-1`.  



## 📝 **Python Implementation**  

```python
from typing import List
from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        totalBuildings, buildings = 0, []

        # Step 1: Identify building positions
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    buildings.append((i, j))
                    totalBuildings += 1
                if grid[i][j] == 0:
                    grid[i][j] = [0, 0]

        def bfs(start):
            """ BFS to calculate distance from one building """
            q = deque([(*start, 0)])
            visited = set([start])
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            while q:
                row, col, distance = q.popleft()
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    if 0 <= newRow < ROWS and 0 <= newCol < COLS and (newRow, newCol) not in visited:
                        if grid[newRow][newCol] == 0 or isinstance(grid[newRow][newCol], list):
                            grid[newRow][newCol][0] += 1
                            grid[newRow][newCol][1] += distance + 1
                            q.append((newRow, newCol, distance + 1))
                            visited.add((newRow, newCol))

        # Step 2: BFS from each building
        for building in buildings:
            bfs(building)

        # Step 3: Find the minimum distance from valid empty land
        shortestDistance = float('inf')
        for i in range(ROWS):
            for j in range(COLS):
                if isinstance(grid[i][j], list) and grid[i][j][0] == totalBuildings:
                    shortestDistance = min(shortestDistance, grid[i][j][1])

        return shortestDistance if shortestDistance != float('inf') else -1
```



## 📂 **Project Structure**  

```
shortest_distance_from_all_buildings/
├── main.py       # Python solution with example usage
├── README.md     # Problem description and explanation
```



## 💡 **Edge Cases Considered:**  
1. **Grid with no buildings or obstacles.**  
2. **Buildings that are unreachable.**  
3. **Obstacles blocking all paths.**  
4. **Edge cases where only one building exists.**  



## 🚀 **Why This Works:**  
- Efficient use of **BFS** to find the shortest path from each building.  
- Accumulates distances only from valid paths, reducing unnecessary calculations.  
- Uses **deque** for efficient queue operations in BFS.  
- Keeps track of visited nodes to prevent infinite loops.  



## ✅ **Test Cases:**  
- **Basic Case:** Grid with multiple buildings and obstacles.  
- **Edge Case:** Grid where no empty land can reach all buildings.  
- **Single Building:** Only one building present.  
- **Obstructed Paths:** Obstacles completely block potential paths.  