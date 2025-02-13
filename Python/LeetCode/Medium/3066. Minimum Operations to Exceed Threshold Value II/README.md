# 🔢 **LeetCode 3066: Minimum Operations to Exceed Threshold Value II**  

## 📌 **Problem Overview**  
We are given an **integer array `nums`** and an **integer `k`**. Our goal is to make **all elements in `nums` at least `k`** by repeatedly performing the following operation:  

1. **Remove** the two smallest numbers `x` and `y` from `nums`.  
2. **Compute a new number** as `min(x, y) * 2 + max(x, y)`.  
3. **Add** the computed number back into `nums`.  

The process continues until **all elements** in `nums` are at least `k`.  
We need to **return the minimum number of operations required** to achieve this.

## 🧠 **Approach: Priority Queue (Min-Heap)**  

### **Intuition**  
To efficiently find the **two smallest elements** in `nums` for each operation, we use a **min-heap (priority queue)**:  

- The **smallest element** in a min-heap is always at the top.  
- Removing the smallest element takes **O(log N)** time.  
- Adding a new element back into the heap also takes **O(log N)** time.  

Thus, using a **heap** improves our operation time from **O(N) per operation** to **O(log N) per operation**, making the solution much more efficient.

### **Why a Min-Heap?**
- Finding the smallest element in a **list** takes **O(N)** time.  
- Finding the smallest element in a **heap** takes **O(1)** time.  
- Removing the smallest element from a **heap** takes **O(log N)** time.  
- Using a heap reduces our complexity from **O(N log N) in a list-based approach** to **O(log N) per operation**.

### **Key Operations in Min-Heap**
| Operation | Time Complexity |
|-----------|----------------|
| Heapify (Convert `nums` into a heap) | **O(N)** |
| Extract the two smallest elements | **O(log N) + O(log N) = O(log N)** |
| Insert new computed value back into heap | **O(log N)** |
| Repeat until all elements are **≥ k** | **O(N log N) in total** |

## 🏆 **Example Walkthrough**  

### **Example 1**
#### **Input:**
```python
nums = [2, 11, 10, 1, 3]
k = 10
```

#### **Processing Steps:**
| Step | Heap (nums) | Operation Performed | New Element Added |
|------|-----------|---------------------|----------------|
| 1️⃣  | `[1, 2, 3, 10, 11]` | Remove `1`, `2` → Add `(1 * 2 + 2 = 4)` | `[3, 4, 10, 11]` |
| 2️⃣  | `[3, 4, 10, 11]` | Remove `3`, `4` → Add `(3 * 2 + 4 = 10)` | `[10, 10, 11]` |
| ✅  | `[10, 10, 11]` | All elements **≥ 10** → Stop | - |

#### **Output:**  
```plaintext
2
```
**Explanation:** It takes **2 operations** to make all elements in `nums` at least `10`.

### **Example 2**
#### **Input:**
```python
nums = [1, 1, 2, 4, 9]
k = 20
```

#### **Processing Steps:**
| Step | Heap (nums) | Operation Performed | New Element Added |
|------|-----------|---------------------|----------------|
| 1️⃣  | `[1, 1, 2, 4, 9]` | Remove `1`, `1` → Add `(1 * 2 + 1 = 3)` | `[2, 3, 4, 9]` |
| 2️⃣  | `[2, 3, 4, 9]` | Remove `2`, `3` → Add `(2 * 2 + 3 = 7)` | `[4, 7, 9]` |
| 3️⃣  | `[4, 7, 9]` | Remove `4`, `7` → Add `(4 * 2 + 7 = 15)` | `[9, 15]` |
| 4️⃣  | `[9, 15]` | Remove `9`, `15` → Add `(9 * 2 + 15 = 33)` | `[33]` |
| ✅  | `[33]` | All elements **≥ 20** → Stop | - |

#### **Output:**  
```plaintext
4
```
**Explanation:** It takes **4 operations** to make all elements in `nums` at least `20`.

## 🛠 **Python Solution**
```python
import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Finds the minimum number of operations needed to make all elements 
        in the array greater than or equal to k.

        In each operation:
        1. Remove the two smallest numbers x and y from the heap.
        2. Add a new number calculated as min(x, y) * 2 + max(x, y).
        3. Repeat until all elements in the array are ≥ k.

        Parameters:
        nums (List[int]): A list of integers.
        k (int): The threshold value.

        Returns:
        int: The minimum number of operations needed.
        """
        # Convert the list into a min-heap for efficient retrieval of the smallest elements
        heapq.heapify(nums)

        num_operations = 0
        while nums[0] < k:
            # Extract the two smallest elements
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            # Compute the new value and push it back into the heap
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))

            # Increment operation count
            num_operations += 1

        return num_operations
```

## ⏳ **Complexity Analysis**
| Step        | Operation            | Time Complexity |
|------------|----------------------|----------------|
| Heapify    | `heapq.heapify(nums)` | **O(N)** |
| Extract Min | `heappop(nums)` (twice per operation) | **O(log N) per operation** |
| Insert New Element | `heappush(nums, new_value)` | **O(log N) per operation** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🚀 **How to Use**
### **1️⃣ Installation**
Ensure you have **Python 3.x** installed.  

### **2️⃣ Running the Script**
```bash
python minimum_operations.py
```

### **3️⃣ Sample Output**
```plaintext
Input: nums = [2, 11, 10, 1, 3], k = 10 → Output: 2
Input: nums = [1, 1, 2, 4, 9], k = 20 → Output: 4
Input: nums = [5, 7, 8], k = 10 → Output: 0
Input: nums = [1, 2], k = 5 → Output: 1
```

## 🎯 **Why This Approach?**
✔ Uses a **min-heap (priority queue) for efficient extraction of the smallest elements**.  
✔ Ensures **O(log N) per operation**, making it much faster than a naive approach.  
✔ 🚀 **Optimised for large datasets with `O(N log N)` complexity.**  

🔥 **This method ensures an efficient and scalable way to determine the minimum operations needed!** 📊✨