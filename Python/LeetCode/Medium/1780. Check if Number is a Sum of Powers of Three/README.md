# 🔢 **LeetCode 1780: Check if Number is a Sum of Powers of Three**  

## 📌 **Problem Overview**  

Given an integer `n`, return `true` **if it is possible to represent** `n` **as the sum of distinct powers of three**. Otherwise, return `false`.  

### **Definition**  
An integer `y` is a **power of three** if there exists an integer `x` such that:  

\[
y = 3^x
\]

## 📝 **Example 1**  
```python
Input: n = 12
Output: true
```
✅ **Explanation:** 

\[
12 = 3^1 + 3^2 = 3 + 9
\]

Thus, `12` can be represented as the sum of distinct powers of three.

## 📝 **Example 2**  
```python
Input: n = 91
Output: true
```
✅ **Explanation:**  

\[
91 = 3^0 + 3^2 + 3^4 = 1 + 9 + 81
\]

Thus, `91` satisfies the condition.

## 📝 **Example 3**  
```python
Input: n = 21
Output: false
```
❌ **Explanation:**  
- `21` **cannot** be expressed as the sum of **distinct** powers of `3`.  

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Ternary Representation**  
- Every **positive integer** can be represented in **base-3** (ternary).  
- If `n` can be written using only **0s and 1s** in base-3, it **is a sum of distinct powers of three**.  
- If any **digit equals 2**, then `n` **cannot** be formed as a sum of distinct powers of three.  

📌 **How does this work?**  
- **Extract the last ternary digit** (`n % 3`).  
- If it is **2**, return `False` (since we would need duplicate powers).  
- **Divide `n` by 3** to check the next digit.  
- If we reach `n == 0`, return `True`.  

## 📝 **Implementation**  

```python
class Solution:
    """
    Solution to check if a number can be represented as a sum of distinct powers of three.
    """

    def checkPowersOfThree(self, n: int) -> bool:
        """
        Determines if n can be expressed as a sum of distinct powers of three.

        :param n: int - The number to check.
        :return: bool - True if possible, False otherwise.
        """
        while n > 0:
            # If n % 3 == 2, it requires duplicate powers of three (invalid case)
            if n % 3 == 2:
                return False
            # Move to the next higher power of three
            n //= 3
        return True
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Iterating over digits in base-3** | **O(log₃(n))** |
| **Overall Complexity** | **O(log₃(n))** ✅ |

🔹 **Why is this optimal?**  
- Each step **reduces `n` by a factor of 3**, leading to **log₃(n) iterations**.  
- This ensures a very fast execution time even for large `n` up to **10⁷**.  

## 📂 **Project Structure**  

```
1780. Check if Number is a Sum of Powers of Three/
├── power_of_three.py  # Python solution
├── README.md          # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses base-3 representation** to check for valid sums.  
✔ **O(log₃(n)) complexity** ensures optimal performance.  
✔ **Simple and efficient solution with no extra space usage**.  

🚀 **Master this technique for problems involving sum of distinct powers!** 🔥  
