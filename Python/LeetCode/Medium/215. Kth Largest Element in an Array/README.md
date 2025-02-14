# 🏆 **LeetCode 215: Kth Largest Element in an Array**

## 📌 **Problem Overview**
Given an integer array `nums` and an integer `k`, return the **k-th largest element** in the array.

⚠ **Note**: The k-th largest element is **based on sorted order**, **not the k-th distinct element**.

🔹 **Constraints:**
- You must solve it **without sorting**.

## 📝 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
```
#### **Output:**
```python
5
```
#### **Explanation:**
- The sorted array is `[1, 2, 3, 4, 5, 6]`.
- The **2nd largest** element is **5**.

### **Example 2**
#### **Input:**
```python
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
```
#### **Output:**
```python
4
```
#### **Explanation:**
- The sorted array is `[1, 2, 2, 3, 3, 4, 5, 5, 6]`.
- The **4th largest** element is **4**.

## 🔍 **Intuition**
Since sorting has **O(N log N)** complexity, we need a more efficient approach.  
We can use a **Min-Heap** (`heapq` in Python) to maintain only the **k largest elements** at all times.

- The **smallest element** in the heap will be the k-th largest element.
- Each push/pop operation on a heap is **O(log k)**.
- The total time complexity is **O(N log k)**, which is much faster than sorting.

## 🛠 **Approach**
1. **Use a Min-Heap (`heapq`)**:
   - Insert elements into the heap while maintaining its size at **k**.
   - If the heap size exceeds **k**, remove the **smallest** element.
   - This ensures that the heap always contains the **k largest elements**.
   - The root of the heap will be the **k-th largest element**.

2. **Final result**:
   - The **smallest element in the heap** (heap's root) is our answer.

## 🚀 **Optimised Python Solution**
```python
import heapq
from typing import List

class Solution:
    """
    A class to find the K-th largest element in an array using a min-heap.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the K-th largest element in an array.

        Args:
            nums (List[int]): A list of integers.
            k (int): The position (1-based) of the largest element to find.

        Returns:
            int: The K-th largest element in the array.
        """
        # Min-heap to store the k largest elements
        heap = []

        # Iterate through each number in the array
        for num in nums:
            heapq.heappush(heap, num)       # Push the number into the heap
            if len(heap) > k:               # If heap size exceeds k, pop the smallest element
                heapq.heappop(heap)

        # The root of the heap is the K-th largest element
        return heap[0]
```

## ⏳ **Complexity Analysis**
| Operation          | Time Complexity  |
|-------------------|----------------|
| Heap Insertion (N elements) | **O(N log k)** |
| Heap Removal (N elements)   | **O(N log k)** |
| **Total Complexity**       | **O(N log k)** |

✅ **Why is this efficient?**  
- Sorting takes **O(N log N)**, but using a heap keeps operations **O(N log k)**.
- When `k << N`, this approach is much faster.

## 🎯 **Why This Approach?**
✔ **More efficient than sorting**  
✔ **Maintains only k elements** at all times  
✔ **Uses a simple min-heap**  

This is an **optimal solution** for finding the k-th largest element in an array efficiently! 🚀
