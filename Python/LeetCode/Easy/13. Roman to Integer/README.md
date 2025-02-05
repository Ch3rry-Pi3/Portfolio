# 🚀 **LeetCode 13: Roman to Integer**

## 📌 **Overview**
This project solves **LeetCode Problem 13: Roman to Integer**.  
The goal is to convert a **Roman numeral string** into an **integer**.

### **Problem Statement**
Given a string `s` representing a **Roman numeral**, return its **integer equivalent**.

🔹 **Constraints:**
- `1 <= s.length <= 15`
- `s` consists of characters **('I', 'V', 'X', 'L', 'C', 'D', 'M')** only.
- It is **guaranteed** that `s` is a valid Roman numeral.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: s = "III"
Output: 3
Explanation:
- `III` represents `1 + 1 + 1 = 3`.
```

### **Example 2**
```python
Input: s = "IV"
Output: 4
Explanation:
- `I` before `V` means **5 - 1 = 4**.
```

### **Example 3**
```python
Input: s = "MCMXCIV"
Output: 1994
Explanation:
- `M = 1000`
- `CM = 900`  (1000 - 100)
- `XC = 90`   (100 - 10)
- `IV = 4`    (5 - 1)
- **Total: `1000 + 900 + 90 + 4 = 1994`**.
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ **Roman numerals are mostly additive** (`XII = 10 + 1 + 1 = 12`).  
✔ **Certain numerals use subtraction** (`IX = 10 - 1 = 9`).  
✔ **Six specific cases involve subtraction:**
  - `I` before `V` (4) or `X` (9)
  - `X` before `L` (40) or `C` (90)
  - `C` before `D` (400) or `M` (900)

## 🧠 **Intuition Behind the Approach**
### **Step-by-Step Walkthrough**
Let's take `s = "MCMXCIV"` and walk through the logic:

| Step | Current Symbol | Next Symbol | Rule Applied | Running Total |
|------|--------------|------------|--------------|---------------|
| 1️⃣   | `M` (1000)  | `C` (100)  | **Add** `1000` | `1000` |
| 2️⃣   | `C` (100)   | `M` (1000) | **Subtract** `100` | `900` |
| 3️⃣   | `M` (1000)  | `X` (10)   | **Add** `1000` | `1900` |
| 4️⃣   | `X` (10)    | `C` (100)  | **Subtract** `10` | `1890` |
| 5️⃣   | `C` (100)   | `I` (1)    | **Add** `100` | `1990` |
| 6️⃣   | `I` (1)     | `V` (5)    | **Subtract** `1` | `1994` |

✔ **Final output is `1994`**.

## 📝 **Step-by-Step Approach**
### **1️⃣ Store Roman Numeral Values**
- Use a **dictionary** to map Roman numerals to integers.

### **2️⃣ Iterate Through `s`**
- If **current numeral is smaller than the next**, subtract it.
- Otherwise, add it.

### **3️⃣ Return Final Result**
- Sum all contributions.

## **💡 Implementation**
```python
class Solution:
    """
    This class provides an implementation of the 'Roman to Integer' problem.

    The function `romanToInt` converts a given Roman numeral string into an integer.
    """

    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral string to an integer.

        :param s: A string representing a Roman numeral.
        :return: Integer equivalent of the Roman numeral.
        """
        roman = {
            "I": 1, "V": 5, "X": 10, "L": 50, 
            "C": 100, "D": 500, "M": 1000
        }

        result = 0  # Stores the final integer result

        # Traverse the string, checking if subtraction is needed
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]  # Subtract when a smaller numeral appears before a larger one
            else:
                result += roman[s[i]]  # Otherwise, add the numeral value

        return result
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Single-pass iteration (`O(n)`)** | **O(n)** ✅ | **O(1)** ✅ |

- **Each character is processed once**, making it **O(n)**.
- **Only a dictionary is used**, making it **O(1)** space.

## 🏗 **Project Structure**
```
13. Roman to Integer/
├── roman_to_integer.py    # Python implementation of the solution
├── README.md              # Detailed explanation & walkthrough
```

✨ **Master Roman numeral conversion with an efficient `O(n)` approach!** 🚀  
