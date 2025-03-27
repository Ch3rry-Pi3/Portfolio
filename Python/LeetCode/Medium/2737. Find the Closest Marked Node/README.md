Absolutely! Here's your **beautifully formatted README** for the problem **"2737. Find the Closest Marked Node"** 🚀



# 📍 LeetCode 2737: Find the Closest Marked Node

## 🧩 Problem Summary

You are given:
- An integer `n` — the number of nodes in a **0-indexed directed weighted graph**.
- A list of `edges`, where `edges[i] = [uᵢ, vᵢ, wᵢ]` represents a **directed edge** from node `uᵢ` to node `vᵢ` with weight `wᵢ`.
- An integer `s` — the **starting node**.
- A list `marked` — a list of **marked nodes**.

Your goal is to determine the **minimum distance** from the starting node `s` to **any node in `marked`**, using **Dijkstra’s algorithm**.

🔁 If there is no path to any marked node, return **-1**.



## ✅ Examples

### Example 1

```python
Input: n = 4,
       edges = [[0,1,1],[1,2,3],[2,3,2],[0,3,4]],
       s = 0,
       marked = [2, 3]

Output: 4
```

### Explanation:
- Paths from node 0 to marked nodes:
  - 0 → 1 → 2 → 3 = 1 + 3 + 2 = 6
  - 0 → 1 → 2 = 1 + 3 = 4
  - 0 → 3 = 4  
- Closest marked node is node 2 with a distance of **4**.



### Example 2

```python
Input: n = 5,
       edges = [[0,1,2],[0,2,4],[1,3,1],[2,3,3],[3,4,2]],
       s = 1,
       marked = [0, 4]

Output: 3
```



### Example 3

```python
Input: n = 4,
       edges = [[0,1,1],[1,2,3],[2,3,2]],
       s = 3,
       marked = [0, 1]

Output: -1
```

### Explanation:
- There are no outgoing paths from node 3 to reach any marked nodes.



## 🧠 Approach & Intuition

### 🔍 Dijkstra’s Algorithm (Min-Heap)
- Use a **priority queue** (min-heap) to always expand the **shortest-known distance** node.
- Track visited distances in a `dist` dictionary.
- Stop as soon as a **marked node** is popped from the queue (since it’s the closest).



## 🧾 Code Walkthrough

```python
from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        """
        Returns the minimum distance from node s to any marked node using Dijkstra's algorithm.
        """
        mark_set = set(marked)
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))

        dist = {s: 0}
        min_heap = [(0, s)]

        while min_heap:
            distance, node = heapq.heappop(min_heap)

            if node in mark_set:
                return dist[node]

            for next_node, weight in adj[node]:
                new_dist = distance + weight
                if new_dist < dist.get(next_node, float("inf")):
                    dist[next_node] = new_dist
                    heapq.heappush(min_heap, (new_dist, next_node))

        return -1
```


## ⏱️ Time & Space Complexity

| Aspect              | Complexity      |
||--|
| Time Complexity     | O((E + V) log V) |
| Space Complexity    | O(E + V)         |

✅ Efficient due to **Dijkstra’s algorithm with a min-heap**  
✅ Supports **early stopping** upon reaching the nearest marked node



## 📌 Key Takeaways

- ✅ **Dijkstra's algorithm** is perfect for finding shortest paths in weighted graphs.
- ✅ Always use `heapq` with a distance dictionary for performance.
- ✅ Converting `marked` into a `set()` enables **fast lookup**.
