# 🚀 **LeetCode 392: Is Subsequence**

## 📌 **Overview**
This project solves **LeetCode Problem 392: Is Subsequence**.  
The goal is to determine whether string **`s`** is a **subsequence** of string **`t`** while preserving the relative order of characters.

### **Problem Statement**
A **subsequence** of a string is a new string **formed by deleting some (or none) of the characters** from the original string **without disturbing the order** of the remaining characters.

Given two strings `s` and `t`, return:
- `True` if `s` is a **subsequence** of `t`.
- `False` otherwise.

🔹 **Constraints:**
- `0 <= s.length <= 100`
- `0 <= t.length <= 10⁴`
- `s` and `t` consist only of **lowercase English letters**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: s = "abc", t = "ahbgdc"
Output: True
Explanation:
- The characters `"abc"` appear **in order** within `"ahbgdc"` (`a → b → c`).
```

### **Example 2**
```python
Input: s = "axc", t = "ahbgdc"
Output: False
Explanation:
- The character `"x"` does not appear in `"ahbgdc"` in order.
```

### **Example 3**
```python
Input: s = "", t = "ahbgdc"
Output: True
Explanation:
- An **empty string** is always a subsequence of any string.
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ **The characters in `s` must appear in `t` in order.**  
✔ **Characters do not need to be adjacent but must maintain relative order.**  
✔ **An empty string is always a subsequence of any string.**  
✔ **A two-pointer approach efficiently checks for subsequences.**

## 🧠 **Intuition Behind the Approach**
### **1️⃣ Use Two Pointers (`pointer_s` and `pointer_t`)**
- `pointer_s` moves through `s`.
- `pointer_t` moves through `t`.
- If `s[pointer_s] == t[pointer_t]`, move both pointers.
- Otherwise, move only `pointer_t` in `t`.

### **2️⃣ Stop When Either Pointer Reaches the End**
- If `pointer_s` reaches the end of `s`, all characters were found **in order**, so return `True`.
- Otherwise, return `False`.

## 📝 **Step-by-Step Approach**
### **1️⃣ Initialise Two Pointers**
- `pointer_s = 0` (tracks position in `s`).
- `pointer_t = 0` (tracks position in `t`).

### **2️⃣ Traverse `t` Using `pointer_t`**
- If `s[pointer_s] == t[pointer_t]`, move `pointer_s` forward.
- Always move `pointer_t` forward.

### **3️⃣ Check If `s` Was Fully Matched**
- If `pointer_s == len(s)`, return `True`.
- Otherwise, return `False`.

### **4️⃣ Example Walkthrough (`s = "abc", t = "ahbgdc"`)**
| Step | `s[pointer_s]` | `t[pointer_t]` | Match? | Move Pointers |
|------|--------------|--------------|--------|---------------|
| 1    | `"a"`       | `"a"`        | ✅ Yes | `pointer_s → 1`, `pointer_t → 1` |
| 2    | `"b"`       | `"h"`        | ❌ No  | `pointer_t → 2` |
| 3    | `"b"`       | `"b"`        | ✅ Yes | `pointer_s → 2`, `pointer_t → 3` |
| 4    | `"c"`       | `"g"`        | ❌ No  | `pointer_t → 4` |
| 5    | `"c"`       | `"d"`        | ❌ No  | `pointer_t → 5` |
| 6    | `"c"`       | `"c"`        | ✅ Yes | `pointer_s → 3` (Reached end of `s`) |

✔ **Since all characters of `s` were matched in `t` in order, return `True`.**

## **💡 Implementation**
```python
class Solution:
    """
    This class provides an implementation of the 'Is Subsequence' problem.

    The function `isSubsequence` checks whether string `s` is a subsequence of string `t`.
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Determines if `s` is a subsequence of `t`.

        :param s: The string to check as a subsequence.
        :param t: The target string.
        :return: `True` if `s` is a subsequence of `t`, otherwise `False`.
        """
        pointer_s = pointer_t = 0                   # Initialise two pointers

        # Traverse `t` while checking for characters in `s`
        while pointer_s < len(s) and pointer_t < len(t):
            if s[pointer_s] == t[pointer_t]:        # If characters match, move `s` pointer
                pointer_s += 1
            pointer_t += 1                          # Always move `t` pointer

        return pointer_s == len(s)                  # `s` must be fully matched to be a subsequence


def main():
    """
    Demonstrates testing the isSubsequence function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        ("abc", "ahbgdc"),          # Expected: True
        ("axc", "ahbgdc"),          # Expected: False
        ("", "ahbgdc"),             # Expected: True (empty string is a subsequence of any string)
        ("b", "abc"),               # Expected: True
        ("abcdef", "abcdef"),       # Expected: True (identical strings)
        ("abc", "acb"),             # Expected: False (order matters)
    ]

    for s, t in test_cases:
        print(f"Input: s = \"{s}\", t = \"{t}\"")
        result = solver.isSubsequence(s, t)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Two-pointer approach (`O(n)`)** | **O(n)** ✅ | **O(1)** ✅ |

- **Each character is checked at most once**, making it **O(n)**.
- **No extra space is used**, making it **O(1)**.

## 🏗 **Project Structure**
```
392. Is Subsequence/
├── is_subsequence.py    # Python implementation of the solution
├── README.md            # Detailed explanation & walkthrough
```

✨ **Master the two-pointer approach for efficient subsequence checking!** 🚀  