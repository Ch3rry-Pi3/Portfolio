# 🌳 **LeetCode 261: Graph Valid Tree**

## 📌 **Overview**
This project solves **LeetCode Problem 261: Graph Valid Tree** using **Depth-First Search (DFS)** to detect cycles and ensure connectivity.

### **Problem Statement**
You are given an **undirected graph** with `n` nodes labeled `0` to `n - 1` and a list of `edges`. Each edge connects two nodes, meaning the graph is bidirectional.

Return **`true`** if the given graph is a **valid tree**, otherwise return **`false`**.

🔹 **Constraints:**
- `1 <= n <= 2000`
- `0 <= edges.length <= 2000`
- `edges[i] = [a, b]`, where `0 <= a, b < n`
- No duplicate edges exist.

## 🎯 **Example Walkthrough**
### **Example 1**
![Example 1](images/example1.jpg)
```python
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Explanation:
- This graph is connected and has no cycles, so it is a valid tree.
```

### **Example 2**
![Example 2](images/example2.jpg)
```python
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
Explanation:
- This graph contains a **cycle** (1-2-3-1), so it is not a valid tree.
```

## 🚀 **Understanding the Problem**
### **What is a Tree?**
A valid tree is a **connected acyclic graph** with `n` nodes and exactly `n - 1` edges. That means:
1. **No loops (cycles)**
2. **Must be fully connected** (all nodes are reachable from any other node)
3. **An empty graph (`n = 0`) is a valid tree**

### **Key Observations**
✔ If the graph has **more than `n - 1` edges**, it **must** contain a cycle → **Return `False`**.
✔ If the graph has **fewer than `n - 1` edges**, it must be **disconnected** → **Return `False`**.
✔ If the graph has **exactly `n - 1` edges**, and is **fully connected**, it **must be a tree** → **Return `True`**.

## 📝 **Step-by-Step Algorithm**
### **1️⃣ Build an Adjacency List**
We first build an **adjacency list** to represent the graph:
```python
adj = { i: [] for i in range(n) }
for n1, n2 in edges:
    adj[n1].append(n2)
    adj[n2].append(n1)
```
Each node key maps to a list of its **neighboring nodes**.

### **2️⃣ Depth-First Search (DFS) for Cycle Detection**
- Start DFS from **node `0`**.
- Track visited nodes in a **set** (`visit_set`).
- Pass a **`previous`** value to prevent revisiting the immediate parent (avoiding false cycle detection).
- If we visit an already visited node **not marked as `previous`**, we found a cycle → **Return `False`**.

### **3️⃣ Connectivity Check**
- After DFS completes, check if the **number of visited nodes equals `n`**.
- If all nodes are connected → **Valid Tree**.
- If any node is unvisited → **Disconnected Graph → Not a Tree**.

## 📝 **Example Walkthrough**
Let's walk through the process for:
```python
n = 5, edges = [[0,1], [0,2], [0,3], [1,4]]
```
### **Step 1: Build Adjacency List**
```
{ 0: [1, 2, 3],
  1: [0, 4],
  2: [0],
  3: [0],
  4: [1] }
```
### **Step 2: Perform DFS**
| Step | Node | Visited Set | Parent | Action |
|------|------|-------------|--------|--------|
| 1    | 0    | `{0}`       | `-1`    | Start DFS |
| 2    | 1    | `{0, 1}`    | `0`    | Move to neighbor 1 |
| 3    | 4    | `{0, 1, 4}` | `1`    | Move to neighbor 4 |
| 4    | 4    | `{0, 1, 4}` | `1`    | Backtrack (end of path) |
| 5    | 2    | `{0, 1, 4, 2}` | `0` | Move to neighbor 2 |
| 6    | 3    | `{0, 1, 4, 2, 3}` | `0` | Move to neighbor 3 |
| 7    | 3    | `{0, 1, 4, 2, 3}` | `0` | Backtrack (end of path) |

Since all nodes are **visited** and **no cycle was detected**, **return `True`** ✅.

## **Implementation**
```python
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Determines if the given graph forms a valid tree.

        :param n: Number of nodes
        :param edges: List of undirected edges
        :return: True if the graph is a valid tree, False otherwise
        """
        if len(edges) != n - 1:
            return False  # Must have exactly n - 1 edges

        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit_set = set()
        def dfs(node, parent):
            if node in visit_set:
                return False  # Cycle detected

            visit_set.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue  # Ignore edge leading back to parent
                if not dfs(neighbor, node):
                    return False  # Found a cycle

            return True

        return dfs(0, -1) and len(visit_set) == n
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|-----------------|
| **Brute Force Check** | **O(n²)** ❌ | **O(n)** ❌ |
| **DFS + Adjacency List** | **O(n + e)** ✅ | **O(n + e)** ✅ |

- **DFS runs in `O(n + e)`, where `n` is nodes and `e` is edges.**
- **We visit each node once and traverse each edge once.**

## 🏗 **Project Structure**
```
261. Graph Valid Tree/
├── graph_valid_tree.py   # Efficient O(n + e) solution using DFS
├── README.md             # Detailed explanation
├── images/
    ├── example1.jpg
    ├── example2.jpg
```

**🚀 Master Graph Valid Tree problem with DFS!**

