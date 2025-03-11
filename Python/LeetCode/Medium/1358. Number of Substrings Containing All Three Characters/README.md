# 🔢 LeetCode 1358: Number of Substrings Containing All Three Characters  

## 📌 Problem Overview  

Given a string **s** consisting only of the characters **a**, **b**, and **c**, return the **number of substrings** that contain **at least one occurrence** of all three characters.  

## 📝 Example  

### **Example 1**  
```python
Input: s = "abcabc"
Output: 10
```
✅ **Explanation:**  
The substrings containing **at least one occurrence** of **a, b, and c** are:  
- `"abc"`, `"abca"`, `"abcab"`, `"abcabc"`
- `"bcabc"`, `"cab"`, `"cabc"`, and `"abc"` **(again)**  

Total valid substrings: **10**  

### **Example 2**  
```python
Input: s = "aaacb"
Output: 3
```
✅ **Explanation:**  
The substrings containing **at least one occurrence** of **a, b, and c** are:  
- `"aaacb"`, `"aacb"`, and `"acb"`  

Total valid substrings: **3**  

### **Example 3**  
```python
Input: s = "abc"
Output: 1
```
✅ **Explanation:**  
- The only valid substring is `"abc"`, which already contains **a, b, and c**.  

Total valid substrings: **1**  

## 🚀 Approach & Intuition  

### 🔹 **Sliding Window & Last Seen Positions**
- **Use an array** to track the **last position** of 'a', 'b', and 'c'.
- At each character in the string:
  1. **Update** the last seen position of the character.
  2. **Find the leftmost** of the last seen positions.
  3. The **number of valid substrings** ending at the current index is **1 + min(last_seen_positions)**.

📌 **Why does this work?**  
- The **earliest occurrence** of any required character determines the smallest valid substring.  
- This approach ensures an **efficient O(n) solution** instead of brute force **O(n²)**.

## 📝 Implementation  

```python
class Solution:
    """
    LeetCode 1358: Number of Substrings Containing All Three Characters
    """

    def numberOfSubstrings(self, s: str) -> int:
        """
        Counts the number of substrings containing at least one occurrence of 'a', 'b', and 'c'.

        :param s: str - The input string consisting only of 'a', 'b', and 'c'.
        :return: int - The number of valid substrings.
        """
        # Track last seen positions of 'a', 'b', and 'c'
        last_pos = [-1] * 3
        total = 0

        for pos in range(len(s)):
            # Update last seen position for current character
            last_pos[ord(s[pos]) - ord("a")] = pos

            # Calculate valid substrings ending at this position
            total += 1 + min(last_pos)

        return total
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Updating last seen positions** | **O(1)** |
| **Iterating through the string** | **O(n)** |
| **Overall Complexity** | **O(n) ✅** |

🔹 **Why is this optimal?**  
- **Each character is processed once**, making it **linear time**.  
- **No nested loops**, avoiding **O(n²) inefficiency**.

## 📂 **Project Structure**  

```
substrings_all_three/
├── substrings_all_three.py   # Python solution
├── README.md                 # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Sliding window approach optimally tracks character positions.**  
✔ **Efficient O(n) complexity ensures scalability.**  
✔ **Works for all edge cases including long and repetitive strings.**  

🚀 **Master this technique for substring problems!** 🌟🔥  