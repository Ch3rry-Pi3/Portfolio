# 🚀 **LeetCode 11: Container With Most Water**

## 📌 **Overview**
This project solves **LeetCode Problem 11: Container With Most Water** using the **two-pointer approach** to efficiently determine the maximum water area that can be stored between vertical lines.

### **Problem Statement**
Given an array `height` where `height[i]` represents the height of a vertical line at index `i`, find two lines that, together with the x-axis, form a container **that holds the most water**.

🔹 **Constraints:**
- `n == height.length`
- `2 <= n <= 10⁵`
- `0 <= height[i] <= 10⁴`

**You may not tilt the container.**

## 🎯 **Example Walkthrough**
### **Example 1**
![Container Example](images/container.jpg)
```python
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation:
- The best container is formed between height[1] = 8 and height[8] = 7.
- The width is `8 - 1 = 7`.
- The height is `min(8, 7) = 7`.
- The area is `7 * 7 = 49`.
```

### **Example 2**
```python
Input: height = [1,1]
Output: 1
Explanation:
- The only possible container is between height[0] = 1 and height[1] = 1.
- The width is `1 - 0 = 1`.
- The height is `min(1, 1) = 1`.
- The area is `1 * 1 = 1`.
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ The area is determined by the **shorter** of the two lines forming the container.
✔ The wider the gap between two lines, the larger the potential area.
✔ A **brute-force approach (O(n²))** would compare every pair, but this is inefficient for large inputs.
✔ A **two-pointer approach (O(n))** efficiently finds the optimal solution by **moving the smaller-height pointer** inward.

## 📝 **Step-by-Step Approach**
### **1️⃣ Use Two Pointers**
- Start with two pointers: one at the **leftmost** index (`left = 0`) and one at the **rightmost** index (`right = n - 1`).
- Compute the area using the formula:
  ```python
  area = (right - left) * min(height[left], height[right])
  ```

### **2️⃣ Move the Smaller Pointer**
- Always **move the pointer with the smaller height**:
  - If `height[left] < height[right]`, move `left` rightward (`left += 1`).
  - Otherwise, move `right` leftward (`right -= 1`).
- This is because moving the larger height **would not** increase the area, but moving the smaller one **could**.

### **3️⃣ Keep Track of Maximum Area**
- Continuously update the maximum area found so far:
  ```python
  result = max(result, area)
  ```
- Repeat until `left` meets `right`.

## **Implementation**
```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Finds the maximum water that can be contained between two lines.

        :param height: List of integers representing line heights
        :return: Maximum container water area
        """
        result = 0
        left, right = 0, len(height) - 1  # Two-pointer initialization

        while left < right:
            area = (right - left) * min(height[left], height[right])
            result = max(result, area)

            # Move the smaller height pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|-----------------|
| **Brute Force (Nested Loops)** | **O(n²)** ❌ | **O(1)** ✅ |
| **Two-Pointer Approach** | **O(n)** ✅ | **O(1)** ✅ |

- **Two-pointer approach runs in `O(n)`, only requiring a single pass through the array.**
- **Constant extra space is used (`O(1)`).**

## 🏗 **Project Structure**
```
11. Container With Most Water/
├── container_with_most_water.py   # Efficient O(n) two-pointer solution
├── README.md                      # Detailed explanation & walkthrough
├── images/
    ├── container.jpg               # Visualization of problem example
```

**🚀 Master the Two-Pointer Technique for Maximum Water Containers!**

