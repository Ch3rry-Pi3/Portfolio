# 🧾 **LeetCode 1123: Lowest Common Ancestor of Deepest Leaves**  

## 📌 **Problem Overview**  

Given the **root** of a binary tree, find the **lowest common ancestor (LCA)** of its deepest leaves.  

### **Key Concepts:**  
1. **Node Definition:**  
   - A node in a binary tree is a **leaf** if it has **no children**.  

2. **Depth Calculation:**  
   - The **depth** of the root of the tree is **0**.  
   - If the depth of a node is **d**, the depth of each of its children is **d + 1**.  

3. **Lowest Common Ancestor (LCA):**  
   - The LCA of a set **S** of nodes is the **node A** with the **largest depth** such that every node in **S** is in the subtree with root **A**.  

### **Objective:**  
Return the **lowest common ancestor** of the deepest leaves.  



## ✅ **Example**  

### **Input:**  
```
root = [3,5,1,6,2,0,8,null,null,7,4]
```

### **Output:**  
```
2
```

### **Explanation:**  
The **deepest leaves** are nodes **7** and **4**.  
Their **LCA** is the node with value **2**.  



## 🛠 **Approach & Intuition**  

### 🔍 **Step-by-Step:**  
1. **Depth-First Search (DFS):**  
   - Use DFS to calculate the **depth** of each subtree.  
   - Recursively find the **LCA** by comparing depths of the left and right subtrees.  

2. **Condition Handling:**  
   - If **left depth** > **right depth**: Return **left subtree LCA**.  
   - If **right depth** > **left depth**: Return **right subtree LCA**.  
   - If **equal**, the current node is the **LCA**.  

3. **Base Case:**  
   - If the current node is **null**, return `(0, None)` representing **depth** and **node**.  



## 📝 **Python Implementation**  

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Returns the lowest common ancestor (LCA) of the deepest leaves of the binary tree.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            TreeNode: The LCA of the deepest leaves.
        """
        def dfs(root):
            if not root:
                return 0, None

            left = dfs(root.left)
            right = dfs(root.right)

            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right[0]:
                return right[0] + 1, right[1]
            return left[0] + 1, root

        return dfs(root)[1]
```



## 📂 **Project Structure**  

```
lowest_common_ancestor/
├── main.py       # Python solution with example usage
├── README.md     # Problem description and explanation
```



## 💡 **Edge Cases Considered:**  
1. **Single Node Tree:**  
   - The root itself is the LCA.  
2. **Tree with Multiple Deepest Leaves:**  
   - Correctly identifying the common ancestor.  
3. **Unbalanced Tree:**  
   - The deepest leaves may not be on the same side.  
4. **Empty Tree:**  
   - Return `None`.  



## 🚀 **Why This Works:**  
- **Efficiency:** Uses **DFS** to calculate depths and determine the LCA in a **single traversal**.  
- **Optimal LCA Calculation:** The method ensures that **only the deepest leaves** are considered.  
- **Recursion Handling:** Handles all edge cases gracefully using recursion.  



## ✅ **Test Cases:**  
- **Test with various tree structures:**  
  - Balanced, unbalanced, and single-node trees.  
- **Check for correct LCA:**  
  - Ensure that the deepest leaves' ancestor is correctly identified.  
- **Edge Cases:**  
  - Empty tree, tree with one node, tree with all nodes at the same depth.  