# 🧮 LeetCode 2685: Count the Number of Complete Components

## 📌 Problem Overview

You are given:
- An integer `n` representing the number of vertices in an **undirected graph** labeled from `0` to `n - 1`.
- A list of edges `edges`, where each edge connects two vertices `u` and `v`.

Your task is to **count the number of connected components** in the graph that are **complete**.

### 🔍 Definitions

- A **connected component** is a subgraph in which every vertex is reachable from any other vertex in the same component.
- A **complete component** is a connected component in which **every pair of distinct vertices** is directly connected by an edge.

## ✅ Examples

### Example 1

```
Input: 
n = 6, 
edges = [[0,1],[0,2],[1,2],[3,4]]

Output: 
3
```

**Explanation:**
- The component {0,1,2} is complete (each node is connected to every other).
- The component {3,4} is also complete.
- Node 5 is isolated, and by definition, a single node is considered complete.
- Total complete components = 3 ✅

### Example 2

```
Input: 
n = 6, 
edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]

Output: 
1
```

**Explanation:**
- The component {0,1,2} is complete.
- The component {3,4,5} is not complete (no edge between 4 and 5).
- Node 5 is not isolated; it’s part of an incomplete component.
- Total complete components = 1 ✅

## 🧠 Approach & Intuition

We approach this problem using a **graph traversal strategy** and count each component's:
- Number of nodes
- Number of edges

Then, we validate whether that component is complete using the formula:

$$
\text{edges in a complete graph} = \frac{v \times (v - 1)}{2}
$$

Where `v` is the number of nodes in the component.

### ✨ Alternate Implementation Strategy (Used Here)

Instead of traditional DFS/BFS traversal:
1. Build **adjacency lists** with **self-loops** to handle singleton nodes.
2. Use a `defaultdict` to count frequency of identical sorted adjacency sets.
3. A component is **complete** if:
   ```
   len(neighbors) == number of vertices that share the same neighbor set
   ```

## 🧪 Test Coverage

```python
Test Case 1:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3

Test Case 2:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
```

## 🧾 Python Implementation

```python
from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for vertex in range(n):
            graph[vertex] = [vertex]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        component_freq = defaultdict(int)
        for vertex in range(n):
            neighbors = tuple(sorted(graph[vertex]))
            component_freq[neighbors] += 1

        return sum(
            1
            for neighbors, freq in component_freq.items()
            if len(neighbors) == freq
        )
```

## ⏱ Time and Space Complexity

| Metric              | Complexity |
|---------------------|------------|
| 🕓 Time Complexity   | O(n + e)   |
| 🧠 Space Complexity  | O(n)       |

Where `n` is the number of vertices and `e` is the number of edges.

## 🎯 Key Takeaways

✅ Clever use of **frequency dictionaries**  
✅ Smart encoding of neighbor relationships using tuples  
✅ Avoids graph traversal by using neighbor set uniqueness  