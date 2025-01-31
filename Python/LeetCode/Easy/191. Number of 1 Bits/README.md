# 🚀 **LeetCode 191: Number of 1 Bits**

## 📌 **Overview**
This project solves **LeetCode Problem 191: Number of 1 Bits**, which is also known as **Hamming Weight**. The task is to determine how many **set bits** (1s) are present in the binary representation of an integer.

### **Problem Statement**
Given an integer `n`, return the number of `1` bits in its **binary representation**.

🔹 **Constraints:**
- `0 <= n <= 2³¹ - 1`
- The input is a **positive integer**
- The function should run in **O(log n)** time complexity

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: n = 11
Output: 3
Explanation:
- The binary representation of 11 is `1011`.
- It contains three `1` bits.
```

### **Example 2**
```python
Input: n = 128
Output: 1
Explanation:
- The binary representation of 128 is `10000000`.
- It contains only one `1` bit.
```

### **Example 3**
```python
Input: n = 2147483645
Output: 30
Explanation:
- The binary representation of 2147483645 is `1111111111111111111111111111101`.
- It contains **thirty** `1` bits.
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ Every integer has a **unique binary representation**.
✔ We need to **count the number of 1s** in the binary form of `n`.
✔ A **brute-force approach** would convert `n` to binary using `bin(n)`, but this is inefficient.
✔ A **bitwise approach** (`O(log n)`) is much more efficient and avoids unnecessary string operations.

## 📝 **Step-by-Step Approach**
### **1️⃣ Use Bitwise Right Shift (`>>`)**
- **Extract the least significant bit (LSB)** using `n % 2` (checks if the last bit is `1`).
- If the LSB is `1`, add `1` to the count.
- **Right shift** `n` by 1 (`n >> 1`) to check the next bit.
- Repeat until `n` becomes `0`.

### **2️⃣ Example Walkthrough (n = 11)**
```python
n = 11  # Binary: 1011
Iteration 1: LSB = 1 → count = 1 → n becomes 101 (5 in decimal)
Iteration 2: LSB = 1 → count = 2 → n becomes 10  (2 in decimal)
Iteration 3: LSB = 0 → count = 2 → n becomes 1   (1 in decimal)
Iteration 4: LSB = 1 → count = 3 → n becomes 0   (0 in decimal)
Final Count: 3
```

## **Implementation**
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Counts the number of `1` bits in the binary representation of `n`.

        :param n: Unsigned integer
        :return: Number of 1 bits (Hamming Weight)
        """
        result = 0
        while n:
            result += n % 2  # Add 1 if the least significant bit is 1
            n = n >> 1  # Right shift `n` to process the next bit
        return result
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|-----------------|
| **String Conversion (`bin(n)`)** | **O(log n)** ❌ | **O(1)** ✅ |
| **Bitwise Shift (`>>`)** | **O(log n)** ✅ | **O(1)** ✅ |

- **The bitwise approach runs in `O(log n)`, since the number of bits is at most 32 (for a 32-bit integer).**
- **Constant extra space is used (`O(1)`).**

## 🏗 **Project Structure**
```
191. Number of 1 Bits/
├── number_of_1_bits.py    # Efficient O(log n) bitwise solution
├── README.md              # Detailed explanation & walkthrough
```

**🚀 Master Bitwise Operations for Efficient Binary Processing!**

