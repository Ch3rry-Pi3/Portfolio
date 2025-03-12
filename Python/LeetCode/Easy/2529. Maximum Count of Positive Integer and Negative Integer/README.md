# 🔢 **LeetCode 2529: Maximum Count of Positive Integer and Negative Integer**  

## 📌 **Problem Overview**  

Given a **non-decreasing sorted array** of integers, return the **maximum count** between the number of positive integers and the number of negative integers.  

📌 **Important Notes:**  
- `0` is neither positive nor negative.  
- The function should return the **larger count** between positives and negatives.  

## ✅ **Example 1**  

```python
Input: nums = [-2, -1, -1, 1, 2, 3]
Output: 3
```

### **Explanation:**  
- There are **3 positive numbers**: `[1, 2, 3]`
- There are **3 negative numbers**: `[-2, -1, -1]`
- The **maximum count among them is 3** ✅

## ✅ **Example 2**  

```python
Input: nums = [-3, -2, -1, 0, 1, 2]
Output: 3
```

### **Explanation:**  
- There are **3 positive numbers**: `[1, 2]`
- There are **3 negative numbers**: `[-3, -2, -1]`
- The **maximum count among them is 3** ✅

## ✅ **Example 3**  

```python
Input: nums = [5, 20, 66, 1314]
Output: 4
```

### **Explanation:**  
- There are **4 positive numbers**: `[5, 20, 66, 1314]`
- There are **0 negative numbers**
- The **maximum count among them is 4** ✅

## 🛠 **Approach & Intuition**  

### 🔹 **Iterate and Count**  
1. **Initialise two counters:**  
   - `positive_count = 0` → Counts positive numbers  
   - `negative_count = 0` → Counts negative numbers  
2. **Iterate through the array** and increment the respective counter.  
3. **Return the maximum** between `positive_count` and `negative_count`.  

📌 **Why is this efficient?**  
- The algorithm **only iterates once**, making it **O(n) time complexity** ✅  
- Uses **constant extra space**, making it **O(1) space complexity** ✅  

## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        """
        Returns the maximum count between the number of positive and negative integers in a sorted list.

        :param nums: A non-decreasing sorted list of integers.
        :return: Maximum count between positive and negative numbers.
        """
        positive_count = 0
        negative_count = 0

        for num in nums:
            if num > 0:
                positive_count += 1
            elif num < 0:
                negative_count += 1

        return max(positive_count, negative_count)
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Iterating through nums** | **O(n)** ✅ |
| **Counting positives and negatives** | **O(n)** ✅ |
| **Finding the max value** | **O(1)** ✅ |
| **Overall Complexity** | **O(n)** ✅ |

🔹 **Why is this optimal?**  
- The **single iteration** ensures **linear runtime**, keeping it **efficient even for large inputs**.  
- Uses **only two integer counters**, ensuring **constant space usage**.  

## 📂 **Project Structure**  

```
max_count_positive_negative/
├── max_count_positive_negative.py  # Python solution
├── README.md                       # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Simple iteration ensures optimal performance**.  
✔ **Handles edge cases like zeroes in the array**.  
✔ **Runs in O(n) time complexity**, making it **scalable**.  

🚀 **Master this technique for solving similar counting problems!** 🔥  
