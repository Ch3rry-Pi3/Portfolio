# 🚀 **LeetCode 58: Length of Last Word**

## 📌 **Overview**
This project solves **LeetCode Problem 58: Length of Last Word**.  
The goal is to **return the length of the last word** in a given string.

### **Problem Statement**
Given a string `s` consisting of **words and spaces**, return the **length of the last word** in the string.

🔹 **Definition:**
- A **word** is defined as a **maximal substring** consisting of **non-space characters only**.
- The string **may contain leading or trailing spaces**.

🔹 **Constraints:**
- `1 <= s.length <= 10⁴`
- `s` consists of only **uppercase and lowercase English letters and spaces**.
- There will always be **at least one word** in `s`.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: s = "Hello World"
Output: 5
```
#### **Explanation:**
- The last word is `"World"`, which has a **length of 5**.

### **Example 2**
```python
Input: s = "   fly me   to   the moon  "
Output: 4
```
#### **Explanation:**
- The last word is `"moon"`, which has a **length of 4**.
- **Trailing spaces** are ignored.

### **Example 3**
```python
Input: s = "luffy is still joyboy"
Output: 6
```
#### **Explanation:**
- The last word is `"joyboy"`, which has a **length of 6**.

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ **The last word is the final sequence of non-space characters** in `s`.  
✔ **We must ignore any trailing spaces** before counting.  
✔ **A simple reverse traversal efficiently finds the last word's length.**  

## 🧠 **Intuition Behind the Approach**
### **Step-by-Step Walkthrough**
Let's take `s = "   fly me   to   the moon  "` and see how we extract the last word.

#### **Step 1️⃣: Ignore Trailing Spaces**
| Step | Character | Action |
|------|-----------|--------|
| 28   | `' '`    | Ignore |
| 27   | `' '`    | Ignore |
| 26   | `'n'`    | **Start Counting** |

#### **Step 2️⃣: Count Characters Until a Space**
| Step | Character | Action | Length |
|------|-----------|--------|---------|
| 26   | `'n'`    | ✅ Count | `1` |
| 25   | `'o'`    | ✅ Count | `2` |
| 24   | `'o'`    | ✅ Count | `3` |
| 23   | `'m'`    | ✅ Count | `4` |
| 22   | `' '`    | ❌ Stop | **Final: 4** |

**Final Output:** `4`

## 📝 **Step-by-Step Approach**
### **1️⃣ Trim Trailing Spaces**
- Start from the last index and **ignore all trailing spaces**.

### **2️⃣ Count Characters Until the Next Space**
- Count **all non-space characters** until the next space (or start of the string).

### **3️⃣ Return the Count**
- The count gives us the **length of the last word**.

## **💡 Implementation**
```python
class Solution:
    """
    This class provides an implementation of the 'Length of Last Word' problem.

    The function `lengthOfLastWord` returns the length of the last word in a given string.
    A word is defined as a maximal substring consisting of non-space characters only.
    """

    def lengthOfLastWord(self, s: str) -> int:
        """
        Determines the length of the last word in a string.

        :param s: A string containing words and spaces.
        :return: Length of the last word in the string.
        """
        i, length = len(s) - 1, 0

        # Ignore trailing spaces at the end of the string
        while i >= 0 and s[i] == " ":
            i -= 1
        
        # Count characters until a space or the start of the string is reached
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        
        return length
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Single-pass iteration (`O(n)`)** | **O(n)** ✅ | **O(1)** ✅ |

- **Each character is processed at most once**, making it **O(n)**.
- **Only two variables (`i` and `length`) are used**, making it **O(1) space**.

## 🏗 **Project Structure**
```
58. Length of Last Word/
├── length_of_last_word.py    # Python implementation of the solution
├── README.md                 # Detailed explanation & walkthrough
```

✨ **Master string manipulation with an efficient `O(n)` approach!** 🚀  