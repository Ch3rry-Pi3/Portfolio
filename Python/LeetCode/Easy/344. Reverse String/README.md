# 🚀 **LeetCode 344: Reverse String**

## 📌 **Overview**
This project solves **LeetCode Problem 344: Reverse String**.  
The goal is to reverse a given string **in-place**, ensuring **O(1) extra memory usage**.

### **Problem Statement**
Given an input string as an **array of characters** `s`, modify the array **in-place** so that it is reversed.

🔹 **Constraints:**
- `1 <= s.length <= 10⁵`
- `s[i]` is a **printable ASCII character**.
- **Must modify `s` in-place** using `O(1)` extra memory.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: s = ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]
```

### **Example 2**
```python
Input: s = ["H", "a", "n", "n", "a", "h"]
Output: ["h", "a", "n", "n", "a", "H"]
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ **We are given an array of characters**, not a string.  
✔ **The reversal must happen in-place**, meaning **no extra memory** can be used.  
✔ The simplest approach is to **swap elements from both ends using two pointers**.  

## 🧠 **Intuition Behind the Approach**
1. **Use two pointers (`left` and `right`)**:
   - `left` starts at index `0`, and `right` starts at `len(s) - 1`.
   - Swap characters at `left` and `right`, then move pointers inward.

2. **Repeat until `left` meets or crosses `right`**:
   - This ensures each element is swapped exactly **once**.

## 📝 **Step-by-Step Approach**
### **1️⃣ Initialize Two Pointers**
- `left = 0` (start of the list)
- `right = len(s) - 1` (end of the list)

### **2️⃣ Swap Elements Until Pointers Meet**
- Swap `s[left]` and `s[right]`.
- Move `left` rightward (`left += 1`).
- Move `right` leftward (`right -= 1`).

### **3️⃣ Example Walkthrough (`s = ["h", "e", "l", "l", "o"]`)**
| Step | Array State              | Left | Right |
|------|--------------------------|------|-------|
| 1    | `["o", "e", "l", "l", "h"]` | 1    | 3     |
| 2    | `["o", "l", "l", "e", "h"]` | 2    | 2     |
| 3    | **Done!**                 | ❌   | ❌    |

✔ **Final reversed array is `["o", "l", "l", "e", "h"]`.**

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of the 'Reverse String' problem.

    The function `reverseString` reverses a given array of characters in-place, ensuring O(1) extra memory usage.
    """

    def reverseString(self, s: List[str]) -> None:
        """
        Reverses the given list of characters in-place.

        :param s: List of characters representing a string.
        :return: None (modifies `s` in-place).
        """
        left, right = 0, len(s) - 1  # Initialize two pointers

        # Swap characters while the left index is less than the right index
        while left < right:
            s[left], s[right] = s[right], s[left]  # Swap characters
            left, right = left + 1, right - 1  # Move pointers inward


def main():
    """
    Demonstrates testing the reverseString function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        ["h", "e", "l", "l", "o"],  # Expected: ["o", "l", "l", "e", "h"]
        ["H", "a", "n", "n", "a", "h"],  # Expected: ["h", "a", "n", "n", "a", "H"]
        ["A", "B", "C", "D"],  # Expected: ["D", "C", "B", "A"]
        ["a"],  # Expected: ["a"] (single character remains the same)
        [],  # Expected: [] (empty list remains empty)
    ]

    for s in test_cases:
        print(f"Input: {s}")
        solver.reverseString(s)
        print(f"Output: {s}\n")  # Since it's modified in-place


if __name__ == "__main__":
    main()
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Two-pointer swap (`O(n)`)** | **O(n)** ✅ | **O(1)** ✅ |

- **Each character is swapped once**, making it **O(n)**.
- **No extra space is used**, making it **O(1)**.

## 🏗 **Project Structure**
```
344. Reverse String/
├── reverse_string.py    # Python implementation of the solution
├── README.md            # Detailed explanation & walkthrough
```

✨ **Master in-place string manipulation with efficient two-pointer logic!** 🚀  
