# 🌳 **LeetCode 1261: Find Elements in a Contaminated Binary Tree**  

## 📌 **Problem Overview**  
You are given a **contaminated binary tree**, where all node values are initially set to `-1`. The tree must be **recovered** using the following rules:

1. The root node's value is `0`.
2. If a node has a left child, its value is **`2 * node.val + 1`**.
3. If a node has a right child, its value is **`2 * node.val + 2`**.

After recovering the tree, the class should allow checking whether a specific **target value** exists in the recovered tree.

### **Class Definition**  
```python
class FindElements:
    def __init__(self, root: TreeNode):
        """ Initialses the object with a contaminated binary tree and recovers it. """

    def find(self, target: int) -> bool:
        """ Returns True if the target value exists in the recovered binary tree. """
```

## 🔍 **Understanding the Recovery Process**  

The tree follows **deterministic rules** to reconstruct its original values from the given contaminated state.

## 🖼 **Example 1**
### **Input Contaminated Tree**

![Example 1](images/example1.jpg)

**Operations**
```python
find_elements = FindElements([-1, null, -1])
find_elements.find(1)  # Returns False
find_elements.find(2)  # Returns True
```

**Output**
```
[null, false, true]
```

✅ **Explanation:**  
1. Recovering the tree follows the rules:
   - Root (`0`).
   - Right child (`2 * 0 + 2 = 2`).
   - Left child is `null`, so it remains empty.
2. The recovered tree allows `find(2)`, but `find(1)` is `False` because `1` is missing.

## 🖼 **Example 2**
### **Input Contaminated Tree**

![Example 2](images/example2.jpg)

**Operations**
```python
find_elements = FindElements([-1, -1, -1, -1, -1])
find_elements.find(1)  # Returns True
find_elements.find(3)  # Returns True
find_elements.find(5)  # Returns False
```

**Output**
```
[null, true, true, false]
```

✅ **Explanation:**  
1. The tree recovers as:
   ```
       0
      / \
     1   2
    / \
   3   4
   ```
2. `find(1)` ✅ **exists** (left child of root).  
3. `find(3)` ✅ **exists** (left child of `1`).  
4. `find(5)` ❌ **does not exist** in the recovered tree.

## 🖼 **Example 3**
### **Input Contaminated Tree**

![Example 3](images/example3.jpg)

**Operations**
```python
find_elements = FindElements([-1, null, -1, null, -1])
find_elements.find(2)  # Returns False
find_elements.find(3)  # Returns False
find_elements.find(4)  # Returns False
find_elements.find(5)  # Returns True
```

**Output**
```
[null, true, false, false, true]
```

✅ **Explanation:**  
1. The tree recovers as:
   ```
       0
        \
         5
          \
          11
   ```
2. `find(2)` ❌ **does not exist**.  
3. `find(3)` ❌ **does not exist**.  
4. `find(5)` ✅ **exists** (right child of root).  

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Depth-First Search (DFS)**
- The root always starts at `0`.
- **DFS traversal** assigns values recursively:
  - Left child → `2 * parent + 1`
  - Right child → `2 * parent + 2`
- **A HashSet (`set`) stores recovered values** for `O(1)` lookup in `find()`.

### 🔥 **Efficient Solution**
- **`__init__()`** → Recovers the tree in **O(N)** using DFS.
- **`find()`** → Checks for existence in **O(1)** using a `set`.

## 📝 **Implementation**  

```python
# contaminated_binary_tree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements:
    """
    A class that recovers a contaminated binary tree and allows searching
    for recovered values.

    Attributes:
        seen (set): A set storing all recovered values for efficient lookup.

    Methods:
        find(target: int) -> bool:
            Checks if the given target value exists in the recovered tree.
    """

    def __init__(self, root: TreeNode):
        """
        Initialises the object with a contaminated binary tree and recovers it.

        Args:
            root (TreeNode): The root node of the contaminated binary tree.

        The recovery process follows the given rules:
        - root.val = 0
        - If a node has a left child, its value is `2 * node.val + 1`
        - If a node has a right child, its value is `2 * node.val + 2`
        """
        self.seen = set()
        self._dfs(root, 0)          # Start recovering the tree from the root

    def find(self, target: int) -> bool:
        """
        Checks if the target value exists in the recovered binary tree.

        Args:
            target (int): The value to search for.

        Returns:
            bool: True if the target exists, False otherwise.
        """
        return target in self.seen

    def _dfs(self, node: TreeNode, value: int):
        """
        Recovers the binary tree using DFS traversal.

        Args:
            node (TreeNode): The current node being processed.
            value (int): The recovered value of the current node.
        """
        if node is None:
            return
        
        # Assign the recovered value and store it
        node.val = value
        self.seen.add(value)

        # Recursively recover left and right children
        self._dfs(node.left, value * 2 + 1)
        self._dfs(node.right, value * 2 + 2)

```

## ⏳ **Time Complexity Analysis**  

| Operation          | Complexity |
|--------------------|------------|
| **Tree Recovery**  | **O(N)** |
| **Find Operation** | **O(1)** |
| **Overall**        | **O(N) for setup, O(1) per query** ✅ |

> **N = number of nodes in the tree**  

### 🚀 **Why is this efficient?**  
- Uses **DFS for tree recovery** (O(N) traversal).  
- Uses **set for constant-time lookups** (O(1) search).  

## 📂 **Project Structure**  

```
1261. Find Elements in a Contaminated Binary Tree/
├── contaminated_binary_tree.py  # Python solution
├── README.md                    # Explanation and walkthrough
├── images/
│   ├── example1.jpg
│   ├── example2.jpg
│   ├── example3.jpg
```

## 🎯 **Key Takeaways**  
✔ **Recursive DFS for tree recovery** ensures correct structure.  
✔ **O(1) lookup using a hash set** makes `find()` ultra-fast.  
✔ **Understanding binary tree traversal** helps solve similar problems efficiently.  

🚀 **Mastering tree recovery and DFS will help in many LeetCode problems!** 🔥