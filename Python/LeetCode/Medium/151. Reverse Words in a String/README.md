# 🚀 **LeetCode 151: Reverse Words in a String**

## 📌 **Overview**
This project solves **LeetCode Problem 151: Reverse Words in a String**.  
The goal is to **reverse the order of words** in a given string while ensuring:  
- **No extra spaces** are included in the output.  
- Words are **separated by a single space**.  

### **Problem Statement**
Given a string `s`, return:
- A string where **words appear in reverse order**.
- There is **only a single space** between words.
- **Leading and trailing spaces are removed**.

🔹 **Constraints:**
- `1 <= s.length <= 10⁴`
- `s` contains English letters, digits, spaces, and punctuation.
- **At least one word exists** in `s`.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: s = "the sky is blue"
Output: "blue is sky the"
```

### **Example 2**
```python
Input: s = "  hello world  "
Output: "world hello"
Explanation:
- The reversed string should **not contain** leading or trailing spaces.
```

### **Example 3**
```python
Input: s = "a good   example"
Output: "example good a"
Explanation:
- Multiple spaces should be **reduced** to a **single space**.
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ Words in `s` **may be separated by multiple spaces**.  
✔ **Extra spaces before and after words** should be removed.  
✔ The words **must be reversed**, but their **internal order must remain the same**.  
✔ **Efficient built-in string methods** can simplify the solution.

## 🧠 **Intuition Behind the Approach**
### **1️⃣ Remove Extra Spaces**
- Use **`strip()`** to remove **leading and trailing spaces**.
- Use **`split()`** to **extract words**, automatically handling multiple spaces.

### **2️⃣ Reverse the Word Order**
- Use **slicing (`[::-1]`)** to reverse the word list.

### **3️⃣ Join the Words with a Single Space**
- Use **`" ".join()`** to ensure only **one space** separates words.

## 📝 **Step-by-Step Approach**
### **1️⃣ Clean the Input**
- **Trim spaces** (`s.strip()`) to remove unwanted spaces at the start and end.
- **Split into words** (`s.split()`) to break words while automatically handling extra spaces.

### **2️⃣ Reverse the Words**
- Use **slicing (`[::-1]`)** to reorder words.

### **3️⃣ Reconstruct the String**
- Use **`" ".join(words)`** to join them with a single space.

### **4️⃣ Example Walkthrough (`s = "  hello  world  "`)**
| Step | Action | Result |
|------|--------|--------|
| 1️⃣   | Trim spaces | `"hello  world"` |
| 2️⃣   | Split into words | `["hello", "world"]` |
| 3️⃣   | Reverse words | `["world", "hello"]` |
| 4️⃣   | Join with a single space | `"world hello"` |

✔ **Final output is `"world hello"`**.

## **💡 Implementation**
```python
class Solution:
    """
    This class provides an implementation of the 'Reverse Words in a String' problem.

    The function `reverseWords` takes an input string, removes extra spaces, and returns 
    the words in reverse order, ensuring only a single space separates them.
    """

    def reverseWords(self, s: str) -> str:
        """
        Reverses the order of words in a given string.

        :param s: Input string containing words separated by spaces.
        :return: A string with words reversed and properly spaced.
        """
        s = s.strip()  # Remove leading and trailing spaces
        words = s.split()  # Split string into words, automatically handling multiple spaces
        reversed_words = words[::-1]  # Reverse the list of words
        return " ".join(reversed_words)  # Join words with a single space


def main():
    """
    Demonstrates testing the reverseWords function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        "the sky is blue",          # Expected: "blue is sky the"
        "  hello world  ",          # Expected: "world hello"
        "a good   example",         # Expected: "example good a"
        "  multiple   spaces   ",   # Expected: "spaces multiple"
        "one-word",                 # Expected: "one-word"
        "  ",                       # Expected: "" (empty string after trimming)
    ]

    for s in test_cases:
        print(f"Input: \"{s}\"")
        result = solver.reverseWords(s)
        print(f"Output: \"{result}\"\n")


if __name__ == "__main__":
    main()
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Using Built-in String Methods** | **O(n)** ✅ | **O(n)** ✅ |

- **`strip()` and `split()` take `O(n)`**.
- **Reversing the list takes `O(n)`**.
- **Joining words takes `O(n)`**, so the total is **O(n)**.
- **Space complexity is `O(n)`** since we store the word list.

## 🏗 **Project Structure**
```
151. Reverse Words in a String/
├── reverse_words.py    # Python implementation of the solution
├── README.md           # Detailed explanation & walkthrough
```

✨ **Master string manipulation with efficient built-in methods!** 🚀  