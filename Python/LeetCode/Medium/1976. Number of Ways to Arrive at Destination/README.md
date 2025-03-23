# 🛣️ LeetCode 1976: Number of Ways to Arrive at Destination

## 📌 Problem Overview

You're given a city map with `n` intersections numbered from `0` to `n - 1`, connected by **bi-directional roads**. Each road has a travel time. You want to find **how many distinct paths** exist to travel from intersection `0` to `n - 1` in the **shortest amount of time**.

All roads are given in the form `roads[i] = [u, v, time]`.

Return the **number of different shortest-time paths** from `0` to `n - 1`, modulo `10⁹ + 7`.

## ✅ Example 1

```python
Input: 
n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],
         [6,5,1],[2,5,1],[0,4,5],[4,6,2]]

Output: 4
```

### 🔍 Explanation:

There are **four ways** to reach node `6` from node `0` in **7 minutes**, all through different valid paths.  
Hence, the output is `4`.

## ✅ Example 2

```python
Input: 
n = 2
roads = [[1,0,10]]

Output: 1
```

### 🔍 Explanation:

There is only **one road** from 0 to 1. That’s the only valid path with the shortest time. So, we return `1`.

## 🛠️ Approach & Intuition

### 🔹 Dijkstra’s Algorithm with Path Count Tracking

- Use **Dijkstra's algorithm** to compute the **shortest time** to reach each node from node `0`.
- Track how many **different paths** lead to each node using `path_count[]`.
- For every shorter or equal path found:
  - If **shorter**, update shortest time and **reset** path count.
  - If **equal**, **add** to the number of known shortest paths.

## 🧠 Why This Works

Dijkstra ensures:
- Every node is processed in **order of increasing shortest time**.
- We avoid redundant paths and only track the **shortest ways** to reach `n - 1`.

## 🧪 Python Implementation

```python
from heapq import heappop, heappush
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007

        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        heap = [(0, 0)]  # (time, node)
        shortest_time = [float("inf")] * n
        path_count = [0] * n
        shortest_time[0] = 0
        path_count[0] = 1

        while heap:
            curr_time, node = heappop(heap)
            if curr_time > shortest_time[node]:
                continue

            for neighbor, time in graph[node]:
                total_time = curr_time + time

                if total_time < shortest_time[neighbor]:
                    shortest_time[neighbor] = total_time
                    path_count[neighbor] = path_count[node]
                    heappush(heap, (total_time, neighbor))
                elif total_time == shortest_time[neighbor]:
                    path_count[neighbor] = (path_count[neighbor] + path_count[node]) % MOD

        return path_count[n - 1]
```

## ⏱️ Time & Space Complexity

| Metric            | Complexity     |
|------------------|----------------|
| ⏳ Time           | O((N + E) log N) |
| 🧠 Space          | O(N + E)        |
| 📦 Data Structures | Min-Heap, Graph Adjacency List |


## 📂 File Structure

```
number_of_ways/
├── number_of_ways.py     # 💡 Python solution with main()
├── README.md             # 📘 Problem description, approach & explanation
```

## ✅ Key Takeaways

- ✅ Combines **Dijkstra’s shortest path** with **path counting**
- ✅ Ideal for **graph traversal problems** with optimality constraints
- ✅ Always remember to **modulo large results** as required
