# 🔤 **LeetCode 1456: Maximum Number of Vowels in a Substring of Given Length**

## 📌 **Problem Overview**
Given a string `s` and an integer `k`, return the **maximum number of vowel letters** in any substring of `s` with length `k`.

### **Vowel Letters:**
Vowels in English are **'a', 'e', 'i', 'o', 'u'**.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
s = "abciiidef"
k = 3
```
#### **Output:**
```python
3
```
#### **Explanation:**
- The substring `"iii"` contains **3** vowels, which is the maximum possible.

### **Example 2**
#### **Input:**
```python
s = "aeiou"
k = 2
```
#### **Output:**
```python
2
```
#### **Explanation:**
- Any substring of length `2` will always contain **2** vowels.

### **Example 3**
#### **Input:**
```python
s = "leetcode"
k = 3
```
#### **Output:**
```python
2
```
#### **Explanation:**
- The substrings `"lee"`, `"eet"`, and `"ode"` each contain **2** vowels, which is the maximum.

## 🛠 **Approach**
We solve this problem using the **Sliding Window Technique** for efficiency.

### **1️⃣ Initialize a Vowel Count**
- Count the number of vowels in the **first `k` characters** of `s`.

### **2️⃣ Slide the Window**
- Move the window **one character at a time** to the right:
  - **Add** the new character’s vowel count.
  - **Remove** the leftmost character’s vowel count.
  - **Update** the maximum vowel count.

### **3️⃣ Return the Maximum Count Found**

This approach ensures an **O(N) time complexity**, making it optimal for large inputs.

## 🚀 **Python Solution**
```python
from typing import List

def max_vowels(s: str, k: int) -> int:
    """
    Finds the maximum number of vowel letters in any substring of length k.

    Args:
        s (str): The input string.
        k (int): The length of the substring.

    Returns:
        int: The maximum number of vowels found in any k-length substring.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Initialize the count of vowels in the first window of size k
    count = sum(1 for i in range(k) if s[i] in vowels)
    max_count = count

    # Slide the window to the right
    for i in range(k, len(s)):
        count += int(s[i] in vowels)            # Add new character if it is a vowel
        count -= int(s[i - k] in vowels)        # Remove leftmost character if it was a vowel
        max_count = max(max_count, count)       # Update max vowel count
    
    return max_count

```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Initialize First Window | Count vowels in the first `k` characters | **O(K)** |
| Slide the Window | Move window one step at a time | **O(N - K)** |
| **Total Complexity** | **O(N) Time, O(1) Space** | ✅ Efficient |

## 📁 **Project Structure**
```
max_vowels_in_substring/
├── max_vowels_in_substring.py   # Python solution
├── README.md                    # Documentation
```

## 🏆 **Why This Works**
✔ **Sliding Window Approach** ensures we process the string in **linear time**.  
✔ **Maintains a running count of vowels** to avoid unnecessary recomputation.  
✔ **Handles edge cases**, such as strings without vowels or very small values of `k`.  

🚀 **Now you can efficiently find the maximum vowels in any substring of length `k`!** 🎯