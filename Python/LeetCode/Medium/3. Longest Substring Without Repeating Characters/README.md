# 📌 LeetCode 3: Longest Substring Without Repeating Characters

## 📖 Problem Statement

Given a string `s`, find the **length** of the **longest substring** without repeating characters.

### 🔹 **Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### 🔹 **Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### 🔹 **Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a **subsequence** and not a substring.
```

## 🏆 **Approach: Sliding Window + Hash Map**
We use a **Sliding Window** technique with a **Hash Map** to efficiently track seen characters and their latest index positions.

### 🔹 **Algorithm:**
1. Use **two pointers** `i` (left) and `j` (right) to define the window.
2. Maintain a **hash map** `char_to_next_index` that stores the **next index** of each character.
3. **Expand the window** by moving `j` to the right.
4. **If a duplicate character is encountered**, move `i` to the right of the last occurrence of that character.
5. **Update the maximum length** found so far.
6. **Return the longest valid substring length**.

## ⏳ **Complexity Analysis**
| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Sliding Window + Hash Map | **O(N)** | **O(min(N, 26))** |

- **Time Complexity**: Each character is processed **once**, making it **O(N)**.
- **Space Complexity**: Stores a max of **26 letters** (`O(1)`) or **O(N)** in the worst case (if all unique).

## 💡 **Intuition with an Example**
Consider `s = "abcabcbb"`:

| Step | `i` (Left) | `j` (Right) | Window | Length |
|------|-----------|-------------|--------|--------|
| 1    | 0         | 0           | "a"    | 1      |
| 2    | 0         | 1           | "ab"   | 2      |
| 3    | 0         | 2           | "abc"  | 3 ✅    |
| 4    | 1         | 3           | "bca"  | 3      |
| 5    | 2         | 4           | "cab"  | 3      |
| 6    | 3         | 5           | "abc"  | 3      |
| 7    | 4         | 6           | "bc"   | 2      |
| 8    | 5         | 7           | "b"    | 1      |

🔹 **Max Length = 3** (Substring `"abc"`).

## 📝 **Code Implementation**
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.
        """

        n = len(s)
        ans = 0  # Stores the maximum length of substring without repeating characters
        char_to_next_index = {}         # Dictionary to store the next index of each character

        i = 0  # Left pointer of the sliding window

        # Iterate through the string using the right pointer (j)
        for j in range(n):
            # If the character is already in the dictionary, update left pointer
            if s[j] in char_to_next_index:
                i = max(char_to_next_index[s[j]], i)

            # Update the maximum length found so far
            ans = max(ans, j - i + 1)

            # Store the next index of the character
            char_to_next_index[s[j]] = j + 1

        return ans
```

## 🎯 **Edge Cases Considered**
- **Empty String**: `s = ""` → Output: `0`
- **All Unique Characters**: `s = "abcdef"` → Output: `6`
- **All Identical Characters**: `s = "aaaa"` → Output: `1`
- **Mixed Characters**: `s = "dvdf"` → Output: `3`

## 🔥 **Why This Approach?**
✔ **Efficient**: Uses a **Sliding Window** technique with **O(N)** time complexity.  
✔ **Optimised Memory**: Stores **only unique** characters.  
✔ **Straightforward**: Uses dictionary lookups for **fast updates**.

---

## 📌 **Conclusion**
- This approach efficiently finds the **longest substring without repeating characters** using **Sliding Window + Hash Map**.
- The **optimised O(N) solution** ensures scalability for large inputs.
- This problem is frequently asked in **interviews** as it demonstrates **efficient string traversal techniques**.

🚀 **Mastering this approach helps in solving many substring-related problems!** 🚀

This README is **well-structured**, contains **clear explanations**, and is **formatted professionally** for easy understanding! 🚀 Let me know if you'd like any modifications! 😊