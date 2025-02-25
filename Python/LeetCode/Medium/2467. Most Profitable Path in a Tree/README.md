# 🌳 **LeetCode 2467: Most Profitable Path in a Tree**

## 📌 **Problem Overview**

You are given an **undirected tree** with `n` nodes labeled from `0` to `n - 1`, rooted at node `0`. The tree is represented by an **edge list**, where `edges[i] = [aᵢ, bᵢ]` indicates a bidirectional edge between nodes `aᵢ` and `bᵢ`.

Each node has a **gate** that requires either:
- A **fee** to open if `amount[i]` is **negative**, or  
- A **cash reward** if `amount[i]` is **positive**.

Two players, **Alice** and **Bob**, traverse the tree simultaneously:
- Alice moves toward an **optimal leaf node**.
- Bob moves toward **node `0`**.
- If both reach the same node **at the same time**, they share the **fee** or **reward**.
- If Alice reaches a **leaf node**, she stops moving.
- If Bob reaches **node `0`**, he stops moving.

🔹 **Goal:** Find the **maximum net income Alice can have** if she follows the optimal path.

## 📝 **Example 1**
```python
Input: edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]
Output: 6
```
✅ **Explanation:**  
- Alice starts at `0`, Bob at `3`.  
- They both move to `1` and share the **reward (4/2 = 2)**. Alice's income becomes `-2 + 2 = 0`.  
- Bob stops at `0`, Alice moves to `4` and collects `6`.  
- **Final income: `6`**.

## 📝 **Example 2**
```python
Input: edges = [[0,1]], bob = 1, amount = [-7280,2350]
Output: -7280
```
✅ **Explanation:**  
- Alice opens **only node `0`**, paying `-7280`.  
- Bob moves from `1` to `0`, but Alice already opened `0`.  
- **Final income: `-7280`**.

## 🚀 **Approach & Intuition**

### 🔹 **Key Idea: Depth-First Search (DFS)**
- **Step 1:** Construct the tree using adjacency lists.
- **Step 2:** Compute **Bob's distance from each node** using DFS.
- **Step 3:** Use DFS again to compute Alice's **optimal income** by:
  - Moving toward the **most profitable leaf node**.
  - Handling shared costs/rewards at meeting nodes.

📌 **Why does this work?**  
- The **DFS traversal** ensures we find **all paths**, enabling an **optimal leaf selection**.

## 📝 **Implementation**

```python
from typing import List

class Solution:
    def __init__(self):
        """
        Initialises the tree structure and distance tracking.
        """
        self.tree = []
        self.distance_from_bob = []
        self.n = 0

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        """
        Computes the most profitable path Alice can take.
        
        :param edges: List[List[int]] - The edge list representing the tree.
        :param bob: int - The starting node of Bob.
        :param amount: List[int] - The income or cost at each node.
        :return: int - Maximum net income Alice can achieve.
        """
        self.n = len(amount)
        self.tree = [[] for _ in range(self.n)]
        self.distance_from_bob = [0] * self.n

        # Build adjacency list representation of the tree
        for edge in edges:
            self.tree[edge[0]].append(edge[1])
            self.tree[edge[1]].append(edge[0])

        return self._find_paths(0, 0, 0, bob, amount)

    def _find_paths(self, source: int, parent: int, time: int, bob: int, amount: List[int]) -> int:
        """
        DFS to find maximum income path.
        
        :param source: int - Current node in traversal.
        :param parent: int - Parent node in traversal.
        :param time: int - Current time step.
        :param bob: int - Bob's initial position.
        :param amount: List[int] - List of values at each node.
        :return: int - Maximum net income from this node.
        """
        max_income = 0
        max_child = float("-inf")

        # Compute distances from Bob
        if source == bob:
            self.distance_from_bob[source] = 0
        else:
            self.distance_from_bob[source] = self.n

        # Explore child nodes
        for neighbor in self.tree[source]:
            if neighbor != parent:
                max_child = max(
                    max_child,
                    self._find_paths(neighbor, source, time + 1, bob, amount),
                )
                self.distance_from_bob[source] = min(
                    self.distance_from_bob[source],
                    self.distance_from_bob[neighbor] + 1,
                )

        # Compute income based on Alice and Bob's arrival times
        if self.distance_from_bob[source] > time:
            max_income += amount[source]  # Alice gets full amount
        elif self.distance_from_bob[source] == time:
            max_income += amount[source] // 2  # Split reward

        return max_income if max_child == float("-inf") else max_income + max_child
```

## ⏳ **Time Complexity Analysis**

| Operation  | Complexity |
|------------|------------|
| **Building the tree**  | **O(n)** |
| **Bob's distance computation** | **O(n)** |
| **DFS for Alice’s max profit** | **O(n)** |
| **Overall Complexity** | **O(n)** ✅ |

🔹 **Why is this efficient?**  
- Each node is **visited exactly once** in DFS, leading to **linear runtime**.

## 📂 **Project Structure**

```
most_profitable_tree/
├── most_profitable_tree.py  # Python solution
├── README.md                 # Explanation and walkthrough
```

## 🎯 **Key Takeaways**
✔ **Graph traversal (DFS) ensures Alice finds an optimal path.**  
✔ **Precomputing Bob's distance enables efficient decision-making.**  
✔ **O(n) complexity ensures scalability to large trees.**  

🚀 **Master this approach for tree-based dynamic programming problems!** 🌳🔥
