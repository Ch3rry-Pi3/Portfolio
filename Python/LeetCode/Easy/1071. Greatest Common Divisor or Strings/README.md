# 📌 Greatest Common Divisor of Strings

## 📝 Overview
This project solves **LeetCode Problem 1071: Greatest Common Divisor of Strings**.
The goal is to determine the largest possible string that divides both input strings, meaning it can be repeated multiple times to form both.

### **Problem Statement**
Given two strings `str1` and `str2`, return the **longest string** that is a divisor of both. A string `X` is a **divisor** of `Y` if `Y` can be constructed by repeating `X` multiple times.

🔹 **Constraints:**
- `1 <= str1.length, str2.length <= 1000`
- `str1` and `str2` consist of uppercase English letters only.

## 🎯 Example Walkthrough

### **Example 1**
```python
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
```
**Explanation:**
- `ABC` is repeated twice to form `str1 = "ABCABC"`.
- `ABC` is repeated once to form `str2 = "ABC"`.
- Since `ABC` is the largest possible string that can generate both, return `"ABC"`.

### **Example 2**
```python
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
```
**Explanation:**
- The substring `AB` is repeated 3 times to form `"ABABAB"`.
- The substring `AB` is repeated 2 times to form `"ABAB"`.
- Since `AB` is the largest divisor that can create both strings, return `"AB"`.

### **Example 3**
```python
Input: str1 = "LEET", str2 = "CODE"
Output: ""
```
**Explanation:**
- There is no common substring that can be repeated to form both strings.
- Return an empty string.

## 🚀 Understanding the Approach
### **1️⃣ Key Observations**
✔ A valid divisor must be **a prefix** of both strings.
✔ The length of the divisor must be a **common factor** of both string lengths.
✔ If repeating the divisor multiple times reconstructs both strings, it is a valid divisor.

## 📝 Step-by-Step Algorithm
1️⃣ Compute the lengths of both strings (`length1` and `length2`).
2️⃣ Check all possible divisors, starting from the longest possible one (`min(length1, length2)`) down to `1`.
3️⃣ For each possible divisor length:
   - If `length1 % length or length2 % length` evaluates to `True`, return `False` immediately.
   - Determine how many times the substring must repeat to form each string.
   - Extract the substring and check if repeating it reconstructs both `str1` and `str2`.
   - If valid, return the substring.
4️⃣ If no valid divisor is found, return an **empty string**.

## 🔍 Example Walkthrough with Code Execution

### **Input: str1 = "ABCABC", str2 = "ABC"**
#### **Step 1: Compute Lengths**
```python
length1 = len("ABCABC") = 6
length2 = len("ABC") = 3
```

#### **Step 2: Iterate Over Possible Divisors**
- Start with `length = min(6, 3) = 3`.
- Check if `length` is a **common factor** of `length1` and `length2`:
  ```python
  if length1 % length or length2 % length:
      return False
  ```
  - `6 % 3 == 0` ✅
  - `3 % 3 == 0` ✅ → Proceed.

#### **Step 3: Verify Repeating Pattern**
- Extract `substring = "ABC"`.
- Check if repeating it reconstructs both strings:
  ```python
  if "ABC" * (6 // 3) == "ABCABC" and "ABC" * (3 // 3) == "ABC":
  ```
  - `"ABC" * 2 == "ABCABC"` ✅
  - `"ABC" * 1 == "ABC"` ✅ → Valid divisor found!

#### **Step 4: Return Result**
```python
return "ABC"
```
✅ Output: `"ABC"`

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Iterate through divisors and check reconstruction** | **O(N)** ✅ | **O(1)** ✅ |

- **We iterate through possible divisors**, making the approach **O(N)**.
- **No extra space is used**, making it **O(1)**.

## **🏗 Project Structure**
```
1071. Greatest Common Divisor of Strings/
├── gcd_strings.py    # Python implementation of the solution
├── README.md         # Detailed explanation & walkthrough
```

✨ **Master string manipulation with mathematical intuition!** 🚀

