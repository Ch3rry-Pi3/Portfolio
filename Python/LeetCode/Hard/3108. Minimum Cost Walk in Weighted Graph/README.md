# 🌉 **LeetCode 3108: Minimum Cost Walk in Weighted Graph**  

## 📌 **Problem Overview**  

You are given an **undirected weighted graph** with `n` vertices labeled from **0 to n - 1**.  

Each edge in the graph is represented as `[u, v, w]`, meaning that there is an **edge between nodes `u` and `v` with weight `w`**.  

You are also given multiple queries where each query is `[s, t]`, representing a request to find the **minimum cost** of walking from node `s` to node `t`.

The **cost of a walk** from `s` to `t` is calculated as **the bitwise AND (`&`) of all edge weights** encountered in the walk.

If no walk exists between `s` and `t`, return **-1** for that query.

## ✅ **Example 1**  

```python
Input: 
n = 5
edges = [[0, 1, 7], [1, 3, 7], [1, 2, 11]]
queries = [[0, 3], [3, 4]]

Output: [-1, -1]
```

### **Explanation:**  
- The first query `(0 → 3)` has a possible path:  
  **0 → 1 → 3** with weights **[7, 7]**.  
  - Bitwise AND: `7 & 7 = 7`
  - Another possible path: **0 → 1 → 2 → 1 → 3**  
  - Bitwise AND: `7 & 11 & 7 = 1`  
  - The minimum cost is **1**, so the answer is `1`.  

- The second query `(3 → 4)` has **no valid path**, so the answer is `-1`.

## ✅ **Example 2**  

```python
Input: 
n = 3
edges = [[0, 2, 15], [2, 1, 1]]
queries = [[1, 2]]

Output: [0]
```

### **Explanation:**  
- The only query `(1 → 2)` has a path:  
  **1 → 2 → 0**  
  - Weights encountered: **[1, 15]**  
  - Bitwise AND: `1 & 15 = 0`  
  - The answer is `0`.

## 🛠 **Approach & Intuition**  

### 🔹 **Key Concepts**
1. **Union-Find (Disjoint Set Union - DSU)**  
   - Helps in **identifying connected components** in the graph.
   - Uses **Path Compression** to speed up find operations.
   - Uses **Union by Rank** to merge smaller trees under larger ones efficiently.

2. **Bitwise AND (`&`) Computation**  
   - Once connected components are determined, **precompute** the **minimum cost per component** using bitwise AND on edge weights.

3. **Query Processing**  
   - If two nodes belong to **different components**, return `-1`.
   - Otherwise, return the **precomputed AND cost** of that component.

## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    def __init__(self):
        """
        Initialises the solution with parent and depth arrays.
        - `parent`: Tracks the representative (root) of each node's connected component.
        - `depth`: Stores the depth of each connected component to optimize union operations.
        """
        self.parent = []
        self.depth = []
    
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        Computes the minimum cost of walking from `s` to `t` in an undirected graph.

        :param n: Number of vertices labeled from 0 to n-1.
        :param edges: A list of edges where each edge is represented as [u, v, w].
                      - `u` and `v` are the connected vertices.
                      - `w` is the weight of the edge.
        :param queries: A list of queries where each query is [s, t].
                        - `s` is the start vertex.
                        - `t` is the end vertex.
        :return: A list of integers where each value is the minimum cost for the respective query.
        """
        self.parent = [-1] * n  # Initially, each node is its own parent (disjoint set)
        self.depth = [0] * n  # Tracks the depth of each component
        component_cost = [-1] * n  # Tracks the bitwise AND cost for each component

        # Step 1: Union-Find to connect components
        for u, v, _ in edges:
            self._union(u, v)

        # Step 2: Compute the bitwise AND cost for each component
        for u, v, w in edges:
            root = self._find(u)
            component_cost[root] &= w  # Update the cost by performing AND operation

        # Step 3: Process queries
        answer = []
        for s, t in queries:
            # If s and t are in different components, return -1
            if self._find(s) != self._find(t):
                answer.append(-1)
            else:
                # Return the precomputed AND cost of the component
                answer.append(component_cost[self._find(s)])

        return answer

    def _find(self, node: int) -> int:
        """
        Find function with path compression:
        - Returns the representative (root) of the set containing `node`.
        - Applies path compression to speed up future queries.

        :param node: The node whose root is to be found.
        :return: The root of the component.
        """
        if self.parent[node] == -1:
            return node
        self.parent[node] = self._find(self.parent[node])  # Path compression
        return self.parent[node]

    def _union(self, node1: int, node2: int) -> None:
        """
        Union function to merge two components using union by rank:
        - Ensures that the shallower tree is merged under the deeper one.

        :param node1: First node.
        :param node2: Second node.
        """
        root1 = self._find(node1)
        root2 = self._find(node2)

        if root1 == root2:
            return  # Already in the same component

        # Union by rank (depth)
        if self.depth[root1] < self.depth[root2]:
            root1, root2 = root2, root1  # Swap to ensure root1 is deeper

        self.parent[root2] = root1  # Merge root2 into root1

        if self.depth[root1] == self.depth[root2]:
            self.depth[root1] += 1  # Increment depth if both were equal

```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Union-Find Initialization** | **O(n)** ✅ |
| **Union & Find Operations (Path Compression)** | **O(α(n)) ≈ O(1)** ✅ |
| **Bitwise AND Computation** | **O(m)** ✅ |
| **Query Processing** | **O(q)** ✅ |
| **Overall Complexity** | **O(n + m + q)** ✅ |

🔹 **Why is this optimal?**  
- **Union-Find with path compression** ensures near **constant time operations**.  
- **Precomputing the bitwise AND per component** allows **O(1) query lookups**.  

## 🎯 **Key Takeaways**  
✔ **Union-Find (DSU) is powerful** for handling connectivity in graphs.  
✔ **Path compression + rank optimization** ensures optimal performance.  
✔ **Precomputing bitwise AND per component** makes queries **fast**.  

🚀 **Master this approach for graph-related problems!** 🔥