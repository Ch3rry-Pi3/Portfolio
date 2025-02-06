# 🚀 **LeetCode 1726: Tuple with Same Product**

## 📌 **Overview**
This project solves **LeetCode Problem 1726: Tuple with Same Product**.  
The goal is to count the number of **valid tuples** `(a, b, c, d)` where:

\[
a \times b = c \times d
\]

and all elements are distinct, meaning `a ≠ b ≠ c ≠ d`.

### **Problem Statement**
Given an array `nums` of **distinct positive integers**, return the **total number of valid tuples**.

🔹 **Constraints:**
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10⁴`
- **All numbers in `nums` are distinct**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [2, 3, 4, 6]
Output: 8
```
#### **Valid Tuples:**
- `(2,6,3,4)`, `(2,6,4,3)`, `(6,2,3,4)`, `(6,2,4,3)`
- `(3,4,2,6)`, `(3,4,6,2)`, `(4,3,2,6)`, `(4,3,6,2)`

Each **unique product pair** generates **8 permutations**.

### **Example 2**
```python
Input: nums = [1, 2, 4, 5, 10]
Output: 16
```
#### **Valid Tuples:**
- `(1,10,2,5)`, `(1,10,5,2)`, `(10,1,2,5)`, `(10,1,5,2)`
- `(2,5,1,10)`, `(2,5,10,1)`, `(5,2,1,10)`, `(5,2,10,1)`
- `(2,10,4,5)`, `(2,10,5,4)`, `(10,2,4,5)`, `(10,2,5,4)`
- `(4,5,2,10)`, `(4,5,10,2)`, `(5,4,2,10)`, `(5,4,10,2)`

Each **valid pair** generates **8 permutations**, leading to **16 total tuples**.

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ **Each pair `(a, b)` creates a unique product.**  
✔ **Every product can be formed by multiple unique pairs.**  
✔ **For each product appearing `k` times, the number of valid tuples is `8 * (k * (k - 1) / 2)`.**  

## 🧠 **Intuition Behind the Approach**
### **Step-by-Step Walkthrough**
Let's take `nums = [2, 3, 4, 6]` and see how we track product pairs.

#### **Step 1️⃣: Calculate All Pair Products**
| Pair  | Product |
|-------|--------|
| (2,3) | `6` |
| (2,4) | `8` |
| (2,6) | `12` |
| (3,4) | `12` |
| (3,6) | `18` |
| (4,6) | `24` |

#### **Step 2️⃣: Count Product Occurrences**
| Product | Occurrences |
|---------|------------|
| `6`  | 1 |
| `8`  | 1 |
| `12` | 2 |
| `18` | 1 |
| `24` | 1 |

#### **Step 3️⃣: Compute Valid Tuples**
- Only **products appearing twice or more** can form valid tuples.
- **Formula**: `8 * (count * (count - 1) / 2)`
- **For `12` appearing twice:**  
  - `8 * (2 * 1 / 2) = 8`
- **Final Output:** `8`

## 📝 **Step-by-Step Approach**
### **1️⃣ Track Product Frequencies**
- Use a dictionary `product_cnt` to count **how many times each product appears**.

### **2️⃣ Count Valid Pair Combinations**
- Use another dictionary `pair_cnt` to track **how many valid tuples** each product forms.

### **3️⃣ Compute Final Result**
- Iterate over the product counts and **apply the formula**:

\[
\text{valid tuples} = 8 \times \frac{k (k - 1)}{2}
\]

## **💡 Implementation**
```python
from typing import List
from collections import defaultdict

class Solution:
    """
    This class provides an implementation of the 'Tuple with Same Product' problem.

    The function `tupleSameProduct` counts the number of valid tuples (a, b, c, d)
    such that a * b = c * d, where a, b, c, and d are distinct elements of nums.
    """

    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        Computes the number of valid tuples satisfying the condition a * b = c * d.

        :param nums: List of distinct positive integers.
        :return: The total number of valid tuples.
        """
        product_cnt = defaultdict(int)                          # Tracks occurrences of product pairs
        pair_cnt = defaultdict(int)                             # Tracks the count of valid pairs

        # Generate all possible product pairs
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                pair_cnt[product] += product_cnt[product]       # Store valid pair count
                product_cnt[product] += 1                       # Count occurrences of this product

        # Compute final result by multiplying valid pairs by 8 (per problem requirement)
        result = sum(8 * cnt for cnt in pair_cnt.values())

        return result
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Nested Loops (`O(n²)`)** | **O(n²)** ✅ | **O(n²)** ✅ |

- **Each pair of elements is checked once**, making it **O(n²)**.
- **Dictionaries store product frequencies**, making space **O(n²) in the worst case**.

## 🏗 **Project Structure**
```
1726. Tuple with Same Product/
├── tuple_same_product.py    # Python implementation of the solution
├── README.md                # Detailed explanation & walkthrough
```

✨ **Master combinatorial counting with an efficient `O(n²)` approach!** 🚀  