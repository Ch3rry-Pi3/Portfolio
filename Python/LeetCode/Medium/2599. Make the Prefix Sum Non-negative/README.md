# 📊 **LeetCode 2599: Make the Prefix Sum Non-negative**  

## 📌 **Problem Overview**  
You are given a **0-indexed** integer array `nums`. You can apply the following operation any number of times:  

- Pick any element from `nums` and **move it to the end** of the array.  

The **prefix sum array** of `nums` is an array `prefix` such that:  

\[
\text{prefix}[i] = \sum_{j=0}^{i} \text{nums}[j]
\]

The goal is to find the **minimum number of operations** required to ensure that **all prefix sums are non-negative**.  

## 🎯 **Example Walkthrough**  

### **Example 1**  
#### **Input:**  
```python
nums = [2, 3, -5, 4]
```
#### **Output:**  
```python
0
```
#### **Explanation:**  
- The array is already **valid**, meaning no operations are needed.  
- The prefix sum array is **[2, 5, 0, 4]**, which contains no negative values.  

### **Example 2**  
#### **Input:**  
```python
nums = [3, -5, -2, 6]
```
#### **Output:**  
```python
1
```
#### **Explanation:**  
- **One operation** is required: move `-5` to the end.  
- The array becomes **[3, -2, 6, -5]**.  
- The prefix sum is **[3, 1, 7, 2]**, which contains no negative values.  

## 🛠 **Approach**  

We solve this problem using a **priority queue (min-heap)**:  

### **Algorithm**
1. **Initialise Variables:**  
   - `operations = 0`: A counter for the number of operations performed.  
   - `prefix_sum = 0`: A variable to track the running sum of elements in `nums`.  
   - `pq = []`: A priority queue (min-heap) to store negative numbers encountered in the array.  

2. **Iterate through the array `nums`**:
   - For each element `num` in `nums`:  
     - If `num` is **negative**, add it to the priority queue `pq`.  
     - Add `num` to `prefix_sum` to update the running sum.  
     - If `prefix_sum` becomes **negative**:  
       - Remove the smallest element (most negative) from `pq`.  
       - Subtract the popped value from `prefix_sum`.  
       - **Increment** `operations`.  

3. **Return `operations`** after iterating through all elements.  

This approach ensures that we **minimise the number of moves** required to maintain a non-negative prefix sum.

## 🚀 **Python Solution**  

```python
import heapq
from typing import List

class Solution:
    """
    A class to find the minimum number of operations needed to make the prefix sum non-negative.
    """

    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        """
        Computes the minimum number of operations required to ensure all prefix sums are non-negative.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The minimum number of operations required.
        """

        operations = 0                  # Track the number of operations performed
        prefix_sum = 0                  # Running prefix sum
        min_heap = []                   # Min heap to store negative numbers

        for num in nums:
            # Push negative elements to the min heap
            if num < 0:
                heapq.heappush(min_heap, num)

            prefix_sum += num           # Update prefix sum

            # If the prefix sum becomes negative, remove the smallest negative number
            if prefix_sum < 0:
                prefix_sum -= heapq.heappop(min_heap)
                operations += 1         # Increment the operations count

        return operations
```

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| Iterate through `nums` | `for num in nums` | **O(N)** |
| Maintain heap (`heappush` and `heappop`) | **O(log N)** per operation | **O(N log N)** (worst case) |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 📁 **Project Structure**  

```
prefix_sum_nonnegative/
├── prefix_sum_nonnegative.py  # Python solution
├── README.md                  # Documentation
```

## 🏆 **Why This Works**  

✔ **Efficient heap-based approach** ensures optimal performance.  
✔ **Handles all edge cases**, including arrays with all negative numbers.  
✔ **Minimises the number of operations** needed to maintain a non-negative prefix sum.  

🚀 **This solution guarantees that we find the minimum number of moves required!** 🎯