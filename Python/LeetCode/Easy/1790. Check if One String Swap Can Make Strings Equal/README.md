# 🚀 **LeetCode 1790: Check if One String Swap Can Make Strings Equal**

## 📌 **Overview**
This project solves **LeetCode Problem 1790: Check if One String Swap Can Make Strings Equal**.  
The goal is to determine if two given strings **can be made equal by performing at most one character swap**.

### **Problem Statement**
You are given two strings `s1` and `s2` of **equal length**. A **string swap** allows you to choose **two indices** and swap the characters at those indices.

Return:
- `True` if **one swap (or no swap) is enough** to make `s1` equal to `s2`.
- `False` otherwise.

🔹 **Constraints:**
- `1 <= s1.length == s2.length <= 100`
- `s1` and `s2` consist of **lowercase English letters only**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: s1 = "bank", s2 = "kanb"
Output: True
Explanation:
- Swapping `'b'` (index `0`) with `'k'` (index `3`) in `s2` makes it `"bank"`, which is equal to `s1`.
```

### **Example 2**
```python
Input: s1 = "attack", s2 = "defend"
Output: False
Explanation:
- Too many differences exist between `s1` and `s2`, making a **single swap insufficient**.
```

### **Example 3**
```python
Input: s1 = "kelb", s2 = "kelb"
Output: True
Explanation:
- The strings are already equal, **no swap is needed**.
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ **If the strings are already equal, return `True` immediately.**  
✔ **If they differ at exactly two positions, check if swapping those characters makes them equal.**  
✔ **If they differ at more than two positions, return `False`.**  

## 🧠 **Intuition Behind the Approach**
### **Step-by-Step Walkthrough**
Let's take `s1 = "bank"` and `s2 = "kanb"` and see how we track mismatched indices.

#### **Step 1️⃣: Identify Differences**
We **compare each character** in `s1` and `s2`.

| Index | `s1` | `s2` | Mismatch? |
|-------|------|------|-----------|
| 0     | `b`  | `k`  | ✅ Yes  |
| 1     | `a`  | `a`  | ❌ No   |
| 2     | `n`  | `n`  | ❌ No   |
| 3     | `k`  | `b`  | ✅ Yes  |

- We **store mismatched indices**: `[0, 3]`.

#### **Step 2️⃣: Check If Swap Works**
- `s1[0] == s2[3]` ✅ (`b == b`)
- `s1[3] == s2[0]` ✅ (`k == k`)
- **A swap between these two indices makes the strings equal, so return `True`**.

## 📝 **Step-by-Step Approach**
### **1️⃣ Find Mismatched Indices**
- Iterate through `s1` and `s2` and **store the indices** where characters differ.

### **2️⃣ Return `False` if More Than Two Differences**
- If the number of mismatched indices **exceeds 2**, return `False`.

### **3️⃣ If Exactly Two Differences Exist, Check Swap Validity**
- If swapping the mismatched characters would make `s1 == s2`, return `True`.

### **4️⃣ If No Differences Exist, Return `True`**
- The strings are already equal, so **no swap is needed**.

## **💡 Implementation**
```python
class Solution:
    """
    This class provides an implementation of the 'Check if One String Swap Can Make Strings Equal' problem.

    The function `areAlmostEqual` checks whether two strings can be made equal
    by performing at most one swap on exactly one of the strings.
    """

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Determines if two strings can be made equal with at most one swap.

        :param s1: First input string.
        :param s2: Second input string.
        :return: `True` if one swap can make the strings equal, otherwise `False`.
        """
        indexes = []                    # Stores indices where s1 and s2 differ

        # Identify indices where characters differ
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indexes.append(i)
            if len(indexes) > 2:        # More than two mismatches mean swap can't fix it
                return False

        # If exactly two indices differ, check if swapping makes them equal
        if len(indexes) == 2:
            i, j = indexes
            return s1[i] == s2[j] and s1[j] == s2[i]

        # If no differences exist, the strings are already equal
        return len(indexes) == 0

```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Single-pass iteration (`O(n)`)** | **O(n)** ✅ | **O(1)** ✅ |

- **Each character is processed once**, making it **O(n)**.
- **Only a few indices are stored**, making it **O(1)** space.

## 🏗 **Project Structure**
```
1790. Check if One String Swap Can Make Strings Equal/
├── check_one_swap.py    # Python implementation of the solution
├── README.md            # Detailed explanation & walkthrough
```

✨ **Master string swaps with an efficient `O(n)` approach!** 🚀  