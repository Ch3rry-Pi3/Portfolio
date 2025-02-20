# 🎯 **LeetCode 1980: Find Unique Binary String**  

## 📌 **Problem Overview**  
Given an array `nums` containing `n` **unique** binary strings of **length n**, the task is to find a **binary string of length n** that **does not appear** in `nums`.  

- If multiple valid strings exist, return **any** of them.  
- Each string consists only of the characters **'0'** and **'1'**.  

## 🎯 **Example Walkthrough**  

### **Example 1**  
```python
Input: nums = ["01", "10"]  
Output: "11"  
```
✅ The possible binary strings of length `2` are:  
```python
["00", "01", "10", "11"]
```
Among them, `"11"` **does not exist** in `nums`. `"00"` would also be correct.

### **Example 2**  
```python
Input: nums = ["00", "01"]  
Output: "11"  
```
✅ The possible binary strings of length `2` are:  
```python
["00", "01", "10", "11"]
```
Since `"11"` is missing from `nums`, we return `"11"`.  
Alternatively, `"10"` would also be a correct answer.

### **Example 3**  
```python
Input: nums = ["111", "011", "001"]  
Output: "101"  
```
✅ The possible binary strings of length `3` are:  
```python
["000", "001", "010", "011", "100", "101", "110", "111"]
```
Since `"101"` is not present in `nums`, we return `"101"`.  
Other correct answers could be `"000"`, `"010"`, or `"110"`.

## 🧠 **Key Idea: Cantor's Diagonal Argument**  

This problem is closely related to **Cantor’s Diagonal Argument**, a proof technique used in set theory to demonstrate that **some infinities are larger than others**.  

🔹 **The Idea Applied Here:**  
- If we construct a new binary string by flipping the **diagonal elements** of `nums` (i.e., `nums[i][i]`), we **guarantee** that the generated string is not in `nums`.  
- Why? Because it **differs from every string in `nums` by at least one bit**.  

This ensures that the generated string is **always unique** and **not present** in `nums`, making it an elegant and foolproof solution.  

## 🚀 **Approach Explanation**  

### **1️⃣ Construct a Unique Binary String Using Diagonal Elements**  
- Iterate through `nums`, accessing the **i-th bit of the i-th string** (`nums[i][i]`).  
- If the bit is `"0"`, flip it to `"1"`, and vice versa.  
- This guarantees that the resulting string **differs** from every existing string.

### **2️⃣ Return the Constructed String**  
- Since `nums` contains **n unique** binary strings, our diagonal modification **always** produces a valid missing binary string.

## 📝 **Python Solution**  
```python
from typing import List

def findDifferentBinaryString(nums: List[str]) -> str:
    """
    Finds a binary string of length n that does not appear in nums.

    This solution constructs a unique binary string using Cantor’s Diagonal Argument:
    - Flipping the i-th bit of the i-th string guarantees uniqueness.

    Args:
        nums (List[str]): A list of unique binary strings of length n.

    Returns:
        str: A binary string of length n that is not in nums.
    """
    n = len(nums)
    return "".join("1" if nums[i][i] == "0" else "0" for i in range(n))
```

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| **String Construction** | Iterate through `nums`, flipping diagonal elements | **O(n)** |
| **Overall Complexity** | **O(n)** ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Guarantees uniqueness** using **Cantor's Diagonal Argument**.  
✔ **Avoids brute force search** by directly **constructing** a missing binary string.  
✔ **Linear runtime O(n)** – Highly efficient.  

## 📂 **Project Structure**  
```
unique_binary_string/
├── unique_binary_string.py  # Python solution
├── README.md                # Explanation & approach
```

✨ **A clever mathematical trick, turned into a powerful algorithm! 🚀**