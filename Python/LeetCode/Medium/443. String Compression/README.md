# 🚀 **LeetCode 443: String Compression**

## 📌 **Overview**
This project solves **LeetCode Problem 443: String Compression**.  
The goal is to **compress a given list of characters in-place** by replacing consecutive repeating characters with the character itself followed by the count of its occurrences.

### **Problem Statement**
Given a list of characters `chars`, modify it **in-place** using the following rules:
1. **For each group of consecutive repeating characters**:
   - If the group's length is `1`, keep the character as is.
   - Otherwise, append the character **followed by the count** of its occurrences.
2. The **modified list** should remain in the same order.
3. The function should return **the new length of the modified list**.

🔹 **Constraints:**
- `1 <= chars.length <= 10⁴`
- `chars[i]` is a **lowercase English letter**.
- **Must run in `O(n)` time** and use **constant extra space (`O(1)`)**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Modified List: ["a", "2", "b", "2", "c", "3"]
```
#### **Explanation:**
- The groups are **"aa"**, **"bb"**, **"ccc"**.
- We **replace them** as:
  - `"aa"` → `"a2"`
  - `"bb"` → `"b2"`
  - `"ccc"` → `"c3"`
- The final compressed list is `["a", "2", "b", "2", "c", "3"]` with a **length of 6**.

### **Example 2**
```python
Input: chars = ["a"]
Output: 1
Modified List: ["a"]
```
#### **Explanation:**
- The list contains a **single character**, so **no compression is needed**.

### **Example 3**
```python
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b"]
Output: 4
Modified List: ["a", "b", "1", "0"]
```
#### **Explanation:**
- The group **"bbbbbbbbbb"** (10 times) is replaced with `"b10"`.
- The final compressed list is `["a", "b", "1", "0"]` with a **length of 4**.

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ **If a character appears only once, it remains unchanged.**  
✔ **If a character repeats, append its count directly after it.**  
✔ **Compression should happen **in-place**, modifying the given list.**  
✔ **The function returns the new length of the modified list.**  
✔ **Groups with length `≥ 10` should be split into multiple digits (`10 → "1", "0"`).**  

## 🧠 **Intuition Behind the Approach**
### **Step-by-Step Walkthrough**
Let's take `chars = ["a","a","b","b","c","c","c"]` and see how we modify it **in-place**.

#### **Step 1️⃣: Identify Groups of Consecutive Characters**
| Step | Character | Count |
|------|----------|-------|
| 1    | `"a"`    | `2` |
| 2    | `"b"`    | `2` |
| 3    | `"c"`    | `3` |

#### **Step 2️⃣: Replace the Groups**
| Original | Compressed |
|----------|------------|
| `"aa"`   | `"a2"` |
| `"bb"`   | `"b2"` |
| `"ccc"`  | `"c3"` |

- The final compressed list is `["a", "2", "b", "2", "c", "3"]` with a **length of 6**.

## 📝 **Step-by-Step Approach**
### **1️⃣ Track the Position to Insert Compressed Characters**
- Use a variable `insert` to track where to place compressed values.

### **2️⃣ Traverse the List and Count Consecutive Characters**
- Use a nested loop to count **how many times** each character appears consecutively.

### **3️⃣ Modify the List In-Place**
- Place the character at `insert`.
- If the character repeats, convert the count to a string and **insert its digits separately**.

### **4️⃣ Return the New Length**
- The function **returns the new length of the modified list**.

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of the 'String Compression' problem.

    The function `compress` modifies the input character array in-place to compress
    consecutive repeating characters while maintaining only constant extra space.
    """

    def compress(self, chars: List[str]) -> int:
        """
        Compresses the given character array in-place.

        :param chars: List of characters to be compressed.
        :return: The new length of the compressed array.
        """
        insert = 0                                                      # Position to insert compressed characters
        i = 0                                                           # Pointer to traverse the array

        while i < len(chars):
            group = 1                                                   # Initialise character group count

            # Count consecutive repeating characters
            while (group + i) < len(chars) and chars[group + i] == chars[i]:
                group += 1

            # Store the character at the current insert position
            chars[insert] = chars[i]
            insert += 1

            # If the character group is greater than 1, store the count as well
            if group > 1:
                string = str(group)                                     # Convert count to string
                chars[insert:insert + len(string)] = list(string)       # Insert count
                insert += len(string)                                   # Move insert pointer forward

            # Move the traversal pointer past this group
            i += group

        return insert                                                   # Return the new length of the compressed array


def main():
    """
    Demonstrates testing the compress function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        ["a", "a", "b", "b", "c", "c", "c"],                            # Expected: ["a", "2", "b", "2", "c", "3"], return 6
        ["a"],                                                          # Expected: ["a"], return 1
        ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],        # Expected: ["a", "b", "1", "0"], return 4
        ["a", "a", "a", "a", "a"],                                      # Expected: ["a", "5"], return 2
        ["a", "b", "c"],                                                # Expected: ["a", "b", "c"], return 3 (no compression)
    ]

    for chars in test_cases:
        print(f"Input: {chars}")
        result = solver.compress(chars)
        print(f"Compressed Output: {chars[:result]}, Length: {result}\n")


if __name__ == "__main__":
    main()
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Single-pass iteration (`O(n)`)** | **O(n)** ✅ | **O(1)** ✅ |

- **Each character is processed once**, making it **O(n)**.
- **No extra space is used**, making it **O(1)** (modifying the input in-place).

## 🏗 **Project Structure**
```
443. String Compression/
├── string_compression.py    # Python implementation of the solution
├── README.md                # Detailed explanation & walkthrough
```

✨ **Master in-place compression with an efficient `O(n)` approach!** 🚀  