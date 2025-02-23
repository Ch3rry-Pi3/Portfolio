# 🔢 **LeetCode 889: Construct Binary Tree from Preorder and Postorder Traversal**  

## 📌 **Problem Overview**  

Given two integer arrays, **preorder** and **postorder**, representing the **preorder traversal** and **postorder traversal** of a binary tree, reconstruct the tree and return its **root**.  

- **Preorder Traversal:** Visit **root → left subtree → right subtree**  
- **Postorder Traversal:** Visit **left subtree → right subtree → root**  

If there exist multiple possible answers, **return any of them**.

### **Example 1**  
```python
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
```

✅ **Explanation:**  
- The **preorder** traversal suggests **1** is the root.  
- The **postorder** traversal confirms **4 and 5 are children of 2**, and **6 and 7 are children of 3**.  
- We reconstruct the binary tree and return its root.


### **Example 2**  
```python
Input: preorder = [1], postorder = [1]
Output: [1]
```

✅ **Explanation:**  
- A **single-node tree** with **1** as the root.  
- Both traversals are the same, so the tree consists of only one node.

### **Example 3**  
```python
Input: preorder = [1,401,349,90,88], postorder = [90,349,88,401,1]
Output: [1,401,null,349,88,90]
```

✅ **Explanation:**  
- The **preorder** traversal tells us the node order.  
- The **postorder** traversal confirms the child relationships.  
- The tree is reconstructed accordingly.


## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Recursive Construction**  
1. **Use a helper function `_construct_tree(preorder, postorder)`**  
2. **Recursive Steps:**  
   - The first element of **preorder** is always the **root**.  
   - If the **root value is not the last element in postorder**, recursively construct the **left subtree**.  
   - If still unmatched, recursively construct the **right subtree**.  
3. **Base Case:** Stop recursion when all nodes are placed.

📌 **Why does this work?**  
- **Preorder provides root-first ordering**  
- **Postorder ensures subtrees are processed before their root**, helping us know when to complete subtrees.

## 📝 **Implementation**  

```python
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Constructs a binary tree from its preorder and postorder traversals.
    """

    def __init__(self):
        """
        Initialises the index trackers for preorder and postorder lists.
        """
        self.pre_index = 0
        self.post_index = 0

    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        """
        Builds a binary tree from preorder and postorder traversal lists.

        :param preorder: List[int] - Preorder traversal of the tree.
        :param postorder: List[int] - Postorder traversal of the tree.
        :return: Optional[TreeNode] - The root of the reconstructed binary tree.
        """
        return self._construct_tree(preorder, postorder)

    def _construct_tree(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        """
        Recursively constructs the binary tree.

        :param preorder: List[int] - Preorder traversal of the tree.
        :param postorder: List[int] - Postorder traversal of the tree.
        :return: Optional[TreeNode] - The root node of the constructed subtree.
        """
        if self.pre_index >= len(preorder):
            return None

        root = TreeNode(preorder[self.pre_index])
        self.pre_index += 1

        if root.val != postorder[self.post_index]:
            root.left = self._construct_tree(preorder, postorder)

        if root.val != postorder[self.post_index]:
            root.right = self._construct_tree(preorder, postorder)

        self.post_index += 1
        return root
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Constructing the Tree** | **O(n)** |
| **Preorder Traversal** | **O(n)** |
| **Postorder Traversal** | **O(n)** |
| **Overall Complexity** | **O(n)** ✅ |

🔹 **Why is this optimal?**  
- The algorithm **visits each node exactly once** using index tracking.  
- **Recursive approach** ensures minimal overhead.  

## 📂 **Project Structure**  

```
binary_tree_preorder_postorder/
├── binary_tree_preorder_postorder.py  # Python solution
├── README.md                          # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Recursive construction** aligns with preorder/postorder properties.  
✔ **Efficient O(n) complexity** ensures scalability.  
✔ **Handles multiple valid outputs** due to unique constraints.  

🚀 **Master this technique for future tree reconstruction problems!** 🌳🔥  
