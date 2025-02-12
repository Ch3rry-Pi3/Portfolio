# 🔗 **LeetCode 21: Merge Two Sorted Lists**

## 📌 **Problem Overview**
You are given the heads of two **sorted linked lists**, `list1` and `list2`. The goal is to **merge them** into one **sorted** linked list while preserving the original order.

🔹 Each node contains:
- An **integer value**.
- A **pointer to the next node**.

🔹 The function should **return the head of the merged linked list**.

### 🔍 **Visual Representation**
Below is an example of merging two sorted linked lists:

<img src="images/merge.jpg" alt="Merging Two Sorted Lists" width="600"/>

## 🛠 **Approach**
To efficiently merge two sorted linked lists, we use a **dummy node** and a **pointer** to track the merged list.

### 🚀 **Steps to Solve:**
1. **Create a dummy node (`prehead`)** as a placeholder for the merged list.
2. **Use a pointer (`prev`)** to traverse and build the new list.
3. **Compare the values of `l1` and `l2`**:
   - Append the **smaller node** to the merged list.
   - Move the pointer forward.
4. **If one list is exhausted**, attach the remaining nodes of the other list.
5. **Return `prehead.next`** as the merged sorted list.

### ⏳ **Complexity Analysis**
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Merging two lists | **O(N + M)** | **O(1)** |

- **O(N + M)**: Each node from `list1` and `list2` is processed once.
- **O(1)**: No extra space is used apart from pointers.

## 🚀 **Python Solution**
```python
class ListNode:
    """
    Definition for a singly linked list node.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Merges two sorted linked lists into one sorted linked list.

        Args:
            l1 (ListNode): The head of the first sorted linked list.
            l2 (ListNode): The head of the second sorted linked list.

        Returns:
            ListNode: The head of the merged sorted linked list.
        """

        # Dummy node to serve as a placeholder for the new linked list
        prehead = ListNode(-1)

        # Pointer to construct the new linked list
        prev = prehead

        # Traverse both lists and merge nodes in sorted order
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next  # Move to the next node in l1
            else:
                prev.next = l2
                l2 = l2.next  # Move to the next node in l2
            prev = prev.next  # Move the pointer forward

        # Attach the remaining nodes from the non-empty list (if any)
        prev.next = l1 if l1 is not None else l2

        # The merged list starts from the next node of the dummy node
        return prehead.next
```

## 📌 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
list1 = [1, 2, 4]
list2 = [1, 3, 4]
```
#### **Output:**
```python
[1, 1, 2, 3, 4, 4]
```
#### **Explanation:**
- We merge both sorted linked lists node by node in order.

### **Example 2**
#### **Input:**
```python
list1 = []
list2 = []
```
#### **Output:**
```python
[]
```
#### **Explanation:**
- Both lists are empty, so the merged list is also empty.

### **Example 3**
#### **Input:**
```python
list1 = []
list2 = [0]
```
#### **Output:**
```python
[0]
```
#### **Explanation:**
- One list is empty, so we return the non-empty list.

## ✅ **Why This Approach?**
✔ Uses **constant space** (`O(1)`).  
✔ **Efficient merging** with a **dummy node**.  
✔ **O(N + M) time complexity**, making it **optimal** for merging two sorted lists.

🔗 **By following this approach, we can efficiently merge two sorted linked lists while maintaining the order!** 🚀