# 🔢 **LeetCode 3174: Clear Digits**

## 📌 **Problem Overview**
You are given a string `s` that consists of **letters and digits**. Your task is to **remove all digits** by repeatedly performing the following operation:

- **Delete the first digit** in the string.
- **Delete the closest non-digit character to its left** (if any).

After performing this operation on all digits, **return the final modified string**.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
s = "abc"
```
#### **Output:**
```python
"abc"
```
#### **Explanation:**
There are no digits in the string, so we return `"abc"` as is.

### **Example 2**
#### **Input:**
```python
s = "cb34"
```
#### **Output:**
```python
""
```
#### **Explanation:**
1. The first digit is `'3'`, so we remove it along with its closest left character (`'b'`). String becomes `"c4"`.
2. The next digit is `'4'`, so we remove it along with its closest left character (`'c'`). String becomes `""` (empty).

### **Example 3**
#### **Input:**
```python
s = "a1b2c3"
```
#### **Output:**
```python
""
```
#### **Explanation:**
1. Remove `'1'` and `'a'`, string becomes `"b2c3"`.
2. Remove `'2'` and `'b'`, string becomes `"c3"`.
3. Remove `'3'` and `'c'`, string becomes `""` (empty).

## 🛠 **Approach**
### **1️⃣ Convert String to a List**
- Since Python strings are **immutable**, we convert `s` into a **list** for easy modification.

### **2️⃣ Iterate Through the List**
- **Use a `while` loop** with an index `char_index`.
- If a character is a **digit**, remove it along with the **closest left non-digit**.
- Adjust the index accordingly after removals.

### **3️⃣ Return the Modified String**
- Convert the list back into a string after processing.

## 🚀 **Python Solution**
```python
def clear_digits(s: str) -> str:
    """
    Removes all digits from the string by deleting each digit and 
    the closest non-digit character to its left repeatedly.

    Args:
        s (str): Input string containing alphanumeric characters.

    Returns:
        str: The modified string after all digits and their closest 
             left non-digit characters have been removed.
    """
    s = list(s)
    char_index = 0

    # Iterate through the string
    while char_index < len(s):
        if s[char_index].isdigit():
            # Remove the digit
            del s[char_index]

            # If there's a non-digit character to the left, remove it
            if char_index > 0:
                del s[char_index - 1]
                char_index -= 1             # Adjust index after removal
        else:
            char_index += 1                 # Move to the next character

    return "".join(s)
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Convert string to list | `list(s)` | **O(N)** |
| Iterate through characters | `while` loop | **O(N)** |
| Remove characters | `del s[index]` | **O(N)** (in worst case) |
| Convert list back to string | `"".join(s)` | **O(N)** |
| **Total Complexity** | **O(N²) worst-case** | ⚠️ Can be improved |

## 📁 **Project Structure**
```
clear_digits/
├── clear_digits.py   # Python solution
├── README.md         # Documentation
```

## 🏆 **Why This Works**
✔ **Efficient string modification using a list**.  
✔ **Handles edge cases** (e.g., empty strings, all digits).  
✔ **Iterative approach ensures correctness**.  

🚀 **Now you have a structured solution to efficiently remove digits!** 🎯