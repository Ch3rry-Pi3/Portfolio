# 🔢 **LeetCode 1100: Find K-Length Substrings With No Repeated Characters**  

## 📌 **Problem Overview**  

Given a string **s** and an integer **k**, return the **number of substrings** in **s** of length **k** that have **no repeated characters**.  

## ✅ **Example 1**  

```python
Input: s = "havefunonleetcode", k = 5
Output: 6
```

### **Explanation:**  
There are **6 valid substrings** of length **k=5** that contain **only unique characters**:  
- `"havef"`
- `"avefu"`
- `"vefun"`
- `"efuno"`
- `"etcode"`
- `"tcod"`

## ✅ **Example 2**  

```python
Input: s = "home", k = 5
Output: 0
```

### **Explanation:**  
Since **k > len(s)**, it's **not possible** to find any valid substring.

## 🛠 **Approach & Intuition**  

### 🔹 **Sliding Window + Frequency Array**  
1. **Use two pointers** (`left` and `right`) to track the **current window**.  
2. **Use a frequency array** (`freq[26]`) to track the occurrences of characters.  
3. **Expand the window (`right`)** until we get a substring of size `k`.  
4. **If there are repeated characters,** move the `left` pointer forward to **restore uniqueness**.  
5. **Count substrings** that meet the condition and continue until `right` reaches the end.  

📌 **Why is this efficient?**  
- The algorithm **only processes each character once**, making it **O(n) time complexity** ✅  
- Using an **array instead of a hash set** makes it **faster and memory-efficient** ✅  

## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        """
        Counts the number of substrings of length k in s with no repeated characters.

        :param s: The input string consisting of lowercase English letters.
        :param k: The desired length of the substrings.
        :return: The count of valid substrings.
        """

        if k > 26:
            return 0        # More than 26 unique characters is impossible

        answer = 0
        n = len(s)
        left = right = 0
        freq = [0] * 26         # Frequency array for 'a' to 'z'

        def get_val(ch: str) -> int:
            """Returns the index of a character in the alphabet (0-based)."""
            return ord(ch) - ord("a")

        while right < n:
            freq[get_val(s[right])] += 1

            while freq[get_val(s[right])] > 1:
                freq[get_val(s[left])] -= 1
                left += 1

            if right - left + 1 == k:
                answer += 1
                freq[get_val(s[left])] -= 1
                left += 1

            right += 1

        return answer

```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Sliding Window Traversal** | **O(n)** ✅ |
| **Character Frequency Tracking** | **O(1)** ✅ |
| **Overall Complexity** | **O(n)** ✅ |

🔹 **Why is this optimal?**  
- The **sliding window** ensures we **only traverse `s` once**, keeping the **runtime linear**.  
- Using a **frequency array instead of a dictionary** ensures **constant-time updates**.  

## 📂 **Project Structure**  

```
find_k_substrings_no_repeated/
├── substrings_no_repeated.py  # Python solution
├── README.md                  # Explanation and walkthrough
```


## 🎯 **Key Takeaways**  
✔ **Sliding window technique** ensures efficient substring counting.  
✔ **Uses a frequency array** for optimal character tracking.  
✔ **Runs in O(n) time complexity**, making it **scalable**.  

🚀 **Master this technique for solving similar substring problems!** 🔥  
