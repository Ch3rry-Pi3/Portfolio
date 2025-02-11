# 📝 **LeetCode 1910: Remove All Occurrences of a Substring**

## 📌 **Problem Overview**
You are given two strings **s** and **part**. Your task is to repeatedly **remove the leftmost occurrence** of **part** from **s** until **part** no longer appears in **s**.

🔹 **Steps to follow:**
1. **Find the leftmost occurrence** of `part` in `s`.
2. **Remove it** from `s`.
3. **Repeat** until `part` is no longer found in `s`.
4. **Return the final string.**

A **substring** is a contiguous sequence of characters in a string.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
s = "daabcbaabcbc"
part = "abc"
```
#### **Output:**
```python
"dab"
```
#### **Explanation:**
1. `"daabcbaabcbc"` → Remove `"abc"` at index **2** → `"dabaabcbc"`
2. `"dabaabcbc"` → Remove `"abc"` at index **4** → `"dababc"`
3. `"dababc"` → Remove `"abc"` at index **3** → `"dab"`
4. Now `"abc"` is **no longer** in `s`, so we return `"dab"`.

### **Example 2**
#### **Input:**
```python
s = "axxxxyyyyb"
part = "xy"
```
#### **Output:**
```python
"ab"
```
#### **Explanation:**
1. `"axxxxyyyyb"` → Remove `"xy"` at index **4** → `"axxxxyyyb"`
2. `"axxxxyyyb"` → Remove `"xy"` at index **3** → `"axxxyyb"`
3. `"axxxyyb"` → Remove `"xy"` at index **2** → `"axyb"`
4. `"axyb"` → Remove `"xy"` at index **1** → `"ab"`
5. `"xy"` is no longer in `s`, so we return `"ab"`.

## 🛠 **Approach**
We use **a loop to continuously remove occurrences of `part` from `s`**:

1. **While `part` exists in `s`:**
   - Find the **leftmost** occurrence of `part` using `.find(part)`.
   - Remove `part` by slicing `s` before and after `part`.
   - Continue until `part` is no longer found in `s`.

✅ **Time Complexity:**  
- Each removal operation takes **O(N)** (where `N` is the length of `s`).
- If we remove `part` **M** times, the worst-case complexity is **O(N * M)**.
- In practice, this is efficient for typical constraints.

✅ **Space Complexity:**  
- We **modify `s` in place**, so the space complexity is **O(1)**.

## 🚀 **Python Solution**
```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        Removes all occurrences of 'part' from 's' iteratively.

        Args:
            s (str): The input string.
            part (str): The substring to be removed.

        Returns:
            str: The final string after all occurrences of 'part' are removed.
        """
        while part in s:
            part_start_index = s.find(part)
            s = s[:part_start_index] + s[part_start_index + len(part):]
        return s
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Find `part` in `s` | `.find(part)` | **O(N)** |
| Remove `part` | String slicing | **O(N)** |
| Repeat `M` times | Worst-case removal | **O(N * M)** |
| **Total Complexity** | **O(N * M) worst case** | ✅ |

## 📁 **Project Structure**
```
LeetCode 1910. Remove All Occurrences of a Substring/
├── remove_substring.py   # Python solution
├── README.md             # Documentation
```

## 🏆 **Why This Works**
✔ **Simple and intuitive** approach using a `while` loop.  
✔ **In-place string modification** ensures no unnecessary space usage.  
✔ **Handles all edge cases**, including empty `s`, `part` not found, and full removal.

🚀 **With this solution, you can efficiently remove all occurrences of a substring!** 🎯