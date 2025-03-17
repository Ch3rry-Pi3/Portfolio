# 🔢 **LeetCode 2206: Divide Array Into Equal Pairs**  

## 📌 **Problem Overview**  

You are given an integer array **nums** consisting of **2 × n** integers.  

You need to **divide `nums` into `n` pairs** such that:  

- **Each element belongs to exactly one pair.**  
- **The elements in each pair are equal.**  

Return **`True`** if `nums` can be divided into pairs, otherwise return **`False`**.  

## ✅ **Example 1**  

```python
Input: nums = [3,2,3,2,2,2]
Output: True
```

### **Explanation:**  
There are **6 elements** in `nums`, so they should be divided into **6 / 2 = 3 pairs**.  
If we divide `nums` into pairs:  

- **(2,2)**
- **(3,3)**
- **(2,2)**  

✅ **All conditions are satisfied, so we return `True`.**  

## ✅ **Example 2**  

```python
Input: nums = [1,2,3,4]
Output: False
```

### **Explanation:**  
There is **no way** to divide `nums` into **4 / 2 = 2 pairs** such that all pairs satisfy the given conditions.  
❌ **So, we return `False`.**  

## 🛠 **Approach & Intuition**  

### 🔹 **Using a Frequency Count (HashMap / Counter)**  

1. **Use `Counter` to count occurrences** of each element in `nums`.  
2. **Check if each number appears an even number of times** because:  
   - If a number appears an odd number of times, it **cannot be evenly paired**.  
3. **Return `True` if all counts are even**, otherwise return `False`.  

📌 **Why is this efficient?**  
- We only **traverse the list once** (`O(n)`) to count frequencies.  
- We then **check each frequency** (`O(n)`) to ensure they are even.  
- ✅ **Overall Complexity: `O(n)` (Linear time).**  

## 📝 **Python Implementation**  

```python
from collections import Counter
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        """
        Determines whether the given list of numbers can be divided into equal pairs.
        
        :param nums: List of integers with length 2 * n.
        :return: True if nums can be divided into pairs where elements in each pair are equal, otherwise False.
        """
        # Count frequency of each number in nums
        frequency = Counter(nums)

        # Check if all numbers appear an even number of times
        return all(count % 2 == 0 for count in frequency.values())
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Counting Frequencies (Using `Counter`)** | **O(n)** ✅ |
| **Checking If All Counts Are Even** | **O(n)** ✅ |
| **Overall Complexity** | **O(n)** ✅ |

🔹 **Why is this optimal?**  
- **Single pass** to count occurrences ensures linear time complexity.  
- **Efficient dictionary lookup** makes it **faster than sorting-based approaches**.  

## 📂 **Project Structure**  

```
2206. Divide Array Into Equal Pairs/
├── array_equal_pairs.py  # Python solution
├── README.md             # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses `Counter` for fast frequency counting**.  
✔ **Simple `O(n)` solution with a single traversal**.  
✔ **Direct and easy-to-understand logic**.  

🚀 **Master this technique for solving similar frequency-based problems!** 🔥  
