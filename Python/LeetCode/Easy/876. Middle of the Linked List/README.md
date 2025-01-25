# 🔗 **LeetCode 876: Middle of the Linked List**

## 📌 **Overview**
This project solves **LeetCode Problem 876: Middle of the Linked List** using the **two-pointer technique** to efficiently find the middle node of a singly linked list.

### **Problem Statement**
Given the `head` of a singly linked list, return **the middle node**.
- If there are **two middle nodes**, return the **second middle node**.

## 🖼 **Illustrations**
### **Example 1: Odd Length Linked List**
![Odd Length Linked List](images/odd.jpg)

```python
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
```

### **Example 2: Even Length Linked List**
![Even Length Linked List](images/even.jpg)

```python
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes (3 and 4), we return the second one.
```

## 🚀 **How It Works: Two-Pointer Technique**

### **Approach**
We use **two pointers (`slow` and `fast`)**:
1. `slow` moves **one step** at a time.
2. `fast` moves **two steps** at a time.
3. When `fast` reaches the end, `slow` is at the middle node.

### **Implementation**
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle of a singly linked list using the two-pointer technique.

        :param head: The head node of the linked list
        :return: The middle node of the linked list
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

## 📌 **Step-by-Step Execution**

### **Example 1: `head = [1,2,3,4,5]`**
| Iteration | `slow` Position | `fast` Position |
|-----------|----------------|-----------------|
| Start     | 1              | 1               |
| Step 1    | 2              | 3               |
| Step 2    | 3              | 5               |
| End       | 3              | None            |

**🔹 Output: `[3,4,5]`** ✅

### **Example 2: `head = [1,2,3,4,5,6]`**
| Iteration | `slow` Position | `fast` Position |
|-----------|----------------|-----------------|
| Start     | 1              | 1               |
| Step 1    | 2              | 3               |
| Step 2    | 3              | 5               |
| Step 3    | 4              | None            |

**🔹 Output: `[4,5,6]`** ✅

## ⏳ **Time Complexity Analysis**
- **Each node is visited once**, so the time complexity is **O(n)**.
- **No extra space is used**, so the space complexity is **O(1)**.

| Approach | Time Complexity | Space Complexity |
|----------|----------------|-----------------|
| **Two-Pointer** | **O(n)** | **O(1)** ✅ |

## 🏗 **Project Structure**

```
876. Middle of the Linked List/
├── middle_linked_list.py  # Efficient O(n) solution
├── README.md              # Detailed explanation
├── images/
│   ├── odd.jpg            # Example 1 (odd-length list)
│   ├── even.jpg           # Example 2 (even-length list)
```

### 📝 **`middle_linked_list.py`**
- **Implements the two-pointer approach to find the middle node.**
- **Efficient and runs in O(n) time.**

```python
if __name__ == "__main__":
    # Example usage (assuming a linked list is created beforehand)
    solver = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(f"Middle Node: {solver.middleNode(head).val}")
```

## 🔥 **Key Takeaways**
✅ **Uses two-pointer technique to find the middle in one pass.**
✅ **Handles both odd and even length lists correctly.**
✅ **Optimized for O(n) time and O(1) space.**

## 🚀 **Try It Yourself!**
- Clone the repository.
- Run `middle_linked_list.py` to test the function.

```bash
python middle_linked_list.py
```

## 🌟 **Future Improvements**
- 🏗 **Convert to an iterative stack-based solution.**
- 🏎 **Optimize further with cycle detection techniques.**

**🚀 Master linked list traversal with this optimized approach!**

