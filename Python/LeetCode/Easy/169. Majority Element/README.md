# 🚀 **LeetCode 169: Majority Element**

## 📌 **Overview**
This project solves **LeetCode Problem 169: Majority Element**.  
The goal is to find the **majority element** in an array, which is the element that appears **more than `⌊n/2⌋` times**.

### **Problem Statement**
Given an **array of integers** `nums` of size `n`, return the **majority element**.  
The majority element **always exists**, so we are guaranteed to find an answer.

🔹 **Constraints:**
- `1 <= nums.length <= 5 × 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`
- **There is always a majority element.**

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [3, 2, 3]
Output: 3
```
#### **Explanation:**
- The number `3` appears **more than `⌊3/2⌋ = 1.5` times**.
- **Final Output:** `3`

### **Example 2**
```python
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```
#### **Explanation:**
- `2` appears **4 times**, which is more than `⌊7/2⌋ = 3.5`.
- **Final Output:** `2`

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ **The majority element always exists**, so we don’t need to handle cases where there isn’t one.  
✔ **A brute-force solution (`O(n²)`)** would involve counting each element’s occurrences.  
✔ **An optimal solution uses the Boyer-Moore Voting Algorithm (`O(n)`).**  

## 🧠 **Intuition Behind the Boyer-Moore Voting Algorithm**
### **Step-by-Step Walkthrough**
Let's take `nums = [2,2,1,1,1,2,2]` and see how the **Boyer-Moore Voting Algorithm** works.

#### **Step 1️⃣: Initialise `candidate = None` and `count = 0`**
- This keeps track of the **current candidate for majority** and **its frequency**.

#### **Step 2️⃣: Iterate Through the List**
| Index | Element | Candidate | Count | Action |
|--------|---------|-----------|-------|---------|
| 0  | `2` | `2` | `1` | Candidate starts as `2` |
| 1  | `2` | `2` | `2` | Count increases |
| 2  | `1` | `2` | `1` | Count decreases |
| 3  | `1` | `2` | `0` | Count resets |
| 4  | `1` | `1` | `1` | New candidate `1` |
| 5  | `2` | `1` | `0` | Count resets |
| 6  | `2` | `2` | `1` | New candidate `2` |

- **Final Candidate:** `2`
- **Final Output:** `2`

## 📝 **Step-by-Step Approach**
### **1️⃣ Initialise Variables**
- Set `candidate = None` and `count = 0`.

### **2️⃣ Iterate Through `nums`**
- If `count == 0`, assign `candidate = num`.
- If `num == candidate`, **increase `count`**.
- Otherwise, **decrease `count`**.

### **3️⃣ Return `candidate`**
- The majority element **always exists**, so `candidate` is guaranteed to be correct.

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of the 'Majority Element' problem.

    The function `majorityElement` finds the element that appears more than ⌊ n/2 ⌋ times
    using the Boyer-Moore Voting Algorithm.
    """

    def majorityElement(self, nums: List[int]) -> int:
        """
        Determines the majority element in the given list.

        :param nums: List of integers.
        :return: The majority element (appears more than ⌊ n/2 ⌋ times).
        """
        candidate = None  # Stores the potential majority element
        count = 0  # Counter for tracking candidate frequency

        # Boyer-Moore Voting Algorithm
        for num in nums:
            if count == 0:
                candidate = num  # Set new candidate
            
            count += 1 if num == candidate else -1  # Adjust count

        return candidate  # Majority element guaranteed to exist

```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Boyer-Moore Voting (`O(n)`)** | **O(n)** ✅ | **O(1)** ✅ |

- **Each element is processed once**, making it **O(n)**.
- **Only two variables (`candidate` and `count`) are used**, making it **O(1) space**.

## 🏗 **Project Structure**
```
169. Majority Element/
├── majority_element.py    # Python implementation of the solution
├── README.md              # Detailed explanation & walkthrough
```

✨ **Master majority-element detection with an efficient `O(n)` approach!** 🚀  