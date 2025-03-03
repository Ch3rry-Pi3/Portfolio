# 🔀 **LeetCode 2161: Partition Array According to Given Pivot**  

## 📌 **Problem Overview**  

Given a **0-indexed** integer array `nums` and an integer `pivot`, rearrange `nums` such that:  

1. Every element **less than** `pivot` appears **before** every element **greater than** `pivot`.  
2. Every element **equal to** `pivot` appears **between** elements **less than** and **greater than** `pivot`.  
3. **Relative order** of elements **less than** and **greater than** `pivot` is **maintained**.  

Return the rearranged `nums` **after the reordering**.  

## 📝 **Example 1**  
```python
Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]
```
✅ **Explanation:**  
- Elements **less than 10**: `[9,5,3]`  
- Elements **equal to 10**: `[10,10]`  
- Elements **greater than 10**: `[12,14]`  
- **Relative order** is preserved within each category.

## 📝 **Example 2**  
```python
Input: nums = [-3,4,3,2], pivot = 2
Output: [-3,2,4,3]
```
✅ **Explanation:**  
- Elements **less than 2**: `[-3]`  
- Elements **equal to 2**: `[2]`  
- Elements **greater than 2**: `[4,3]`  
- **Relative order** is maintained.

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Three-List Partitioning**  
- We use **three separate lists** to store elements **less than**, **equal to**, and **greater than** `pivot`.  
- After partitioning, we concatenate the three lists to get the final output.  

📌 **Why this works?**  
- **Preserves relative order** within partitions.  
- **O(n) time complexity**, as each element is processed once.

## 📝 **Implementation**  

```python
from typing import List

class Solution:
    """
    Solution for partitioning an array according to a given pivot value.
    """

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """
        Rearranges nums such that:
        - All elements less than pivot appear first (in original order).
        - All elements equal to pivot appear next.
        - All elements greater than pivot appear last (in original order).

        :param nums: List[int] - The input array.
        :param pivot: int - The pivot value that elements are compared against.
        :return: List[int] - The rearranged array.
        """
        # Lists to store partitioned elements
        less_than_pivot = []
        equal_to_pivot = []
        greater_than_pivot = []

        # Partition elements into three categories
        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)
            elif num == pivot:
                equal_to_pivot.append(num)
            else:
                greater_than_pivot.append(num)

        # Concatenate the partitions to get the final result
        return less_than_pivot + equal_to_pivot + greater_than_pivot
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Partitioning elements** | **O(n)** |
| **Concatenating lists** | **O(n)** |
| **Overall Complexity** | **O(n)** ✅ |

🔹 **Why is this optimal?**  
- **Single-pass partitioning** ensures **O(n) time complexity**.  
- Uses **O(n) space complexity** due to three separate lists.  

## 📂 **Project Structure**  

```
2161. Partition Array According to Given Pivot/
├── partition_array.py  # Python solution
├── README.md       # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Three-list partitioning** preserves relative order.  
✔ **O(n) complexity** ensures fast execution.  
✔ **Concise and readable approach** improves maintainability.  

🚀 **Master this technique for in-place sorting problems!** 🔥  