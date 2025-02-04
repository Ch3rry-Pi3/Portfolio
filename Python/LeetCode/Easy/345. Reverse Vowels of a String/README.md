# 🚀 **LeetCode 345: Reverse Vowels of a String**

## 📌 **Overview**
This project solves **LeetCode Problem 345: Reverse Vowels of a String**.  
The goal is to **reverse only the vowels** in a given string while keeping all other characters **unchanged**.

### **Problem Statement**
Given a string `s`, return:
- A **new string** where **only the vowels are reversed**.
- All other characters **remain in their original positions**.

🔹 **Constraints:**
- `1 <= s.length <= 3 * 10⁵`
- `s` consists of **printable ASCII characters**.

📝 **The vowels are:** `a, e, i, o, u` (both **uppercase** and **lowercase**).  

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: s = "IceCreAm"
Output: "AceCrEIm"
Explanation:
- The vowels in `s` are: `['I', 'e', 'e', 'A']`.
- Reversing them results in `['A', 'e', 'e', 'I']`.
- The final string is `"AceCrEIm"`.
```

### **Example 2**
```python
Input: s = "leetcode"
Output: "leotcede"
Explanation:
- The vowels in `s` are: `['e', 'e', 'o', 'e']`.
- Reversing them results in `['o', 'e', 'e', 'e']`.
- The final string is `"leotcede"`.
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ **Only vowels should be reversed**, consonants **stay in place**.  
✔ **Both uppercase and lowercase vowels must be considered**.  
✔ **A two-pointer approach efficiently swaps vowels in `O(n)` time**.  
✔ **A single pass is sufficient** if vowels are swapped **in-place**.  

## 🧠 **Intuition Behind the Approach**
### **1️⃣ Use Two Pointers (`left` and `right`)**
- `left` starts at index `0`, and `right` starts at `len(s) - 1`.
- Move `left` **until it finds a vowel**.
- Move `right` **until it finds a vowel**.
- Swap the vowels and move both pointers inward.

### **2️⃣ Stop When Pointers Cross**
- The process stops when `left >= right`.

## 📝 **Step-by-Step Approach**
### **1️⃣ Convert `s` into a List**
- Since Python strings are **immutable**, convert `s` into a **mutable list**.

### **2️⃣ Use Two Pointers**
- `left = 0`, `right = len(s) - 1`
- **Move left and right pointers until they reach vowels.**
- Swap the vowels.

### **3️⃣ Convert List Back to String**
- Use `"".join(s)` to return the final modified string.

### **4️⃣ Example Walkthrough (`s = "IceCreAm"`)**
| Step | Left Pointer | Right Pointer | Swap? | Modified String |
|------|-------------|--------------|-------|----------------|
| 1    | `I` (index 0) | `A` (index 7) | ✅ Yes | `"AceCreIm"` |
| 2    | `e` (index 2) | `e` (index 5) | ✅ Yes | `"AceCrEIm"` |
| 3    | Pointers cross | Done | - | `"AceCrEIm"` |

✔ **Final output is `"AceCrEIm"`**.

## **💡 Implementation**
```python
class Solution:
    """
    This class provides an implementation of the 'Reverse Vowels of a String' problem.

    The function `reverseVowels` reverses only the vowels in a given string while keeping 
    the other characters in their original positions.
    """

    def reverseVowels(self, s: str) -> str:
        """
        Reverses only the vowels in the input string.

        :param s: Input string containing both vowels and consonants.
        :return: A string where the vowels are reversed, while other characters remain unchanged.
        """
        s = list(s)  # Convert string to a list for in-place modifications
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}  # Set of vowels
        left, right = 0, len(s) - 1                         # Two-pointer approach

        # Swap vowels using two pointers
        while left < right:
            if s[left] not in vowels:
                left += 1                                   # Move left pointer forward if it's not a vowel
            elif s[right] not in vowels:
                right -= 1                                  # Move right pointer backward if it's not a vowel
            else:
                s[left], s[right] = s[right], s[left]       # Swap vowels
                left, right = left + 1, right - 1           # Move both pointers

        return "".join(s)                                   # Convert list back to string
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Two-pointer swap (`O(n)`)** | **O(n)** ✅ | **O(n)** ✅ |

- **Each character is visited at most once**, making it **O(n)**.
- **Space complexity is `O(n)`** due to storing `s` as a list.

## 🏗 **Project Structure**
```
345. Reverse Vowels of a String/
├── reverse_vowels.py    # Python implementation of the solution
├── README.md            # Detailed explanation & walkthrough
```

✨ **Master vowel reversal with an efficient two-pointer approach!** 🚀  