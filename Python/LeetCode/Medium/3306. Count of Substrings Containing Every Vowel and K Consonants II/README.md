# 📌 **LeetCode 3306: Count of Substrings Containing Every Vowel and K Consonants II**  

## 🔍 **Problem Overview**  
Given a string **word** consisting only of lowercase English letters and a non-negative integer **k**, determine the number of substrings that:  

✅ Contain **every vowel** (`a, e, i, o, u`) **at least once**  
✅ Contain **exactly `k` consonants**  

The function should return the **total number** of such substrings.  

## 🔢 **Example 1**  
```python
Input: word = "aeioqq", k = 1
Output: 0
```
✅ **Explanation:**  
- There is no substring that contains all vowels at least once.  
- The answer is **0**.  

## 🔢 **Example 2**  
```python
Input: word = "aeiou", k = 0
Output: 1
```
✅ **Explanation:**  
- The only valid substring is `"aeiou"`, which contains all vowels and zero consonants.  

## 🔢 **Example 3**  
```python
Input: word = "ieaouqqieaouqq", k = 1
Output: 3
```
✅ **Explanation:**  
Valid substrings that contain every vowel and **exactly one consonant**:  
1️⃣ `"ieaouq"`  
2️⃣ `"qieaou"`  
3️⃣ `"ieaouq"`  

Total valid substrings: **3**.  

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Sliding Window + Frequency Tracking**  
- Use a **sliding window** technique to efficiently track vowels and consonants in the substring.  
- Maintain a **dictionary (`vowel_count`)** to track vowel occurrences.  
- Keep a **counter (`consonant_count`)** to track consonants.  

### 🔹 **Algorithm:**
1. Expand the window (`right` pointer) while adding new characters.  
2. If all **5 vowels** (`a, e, i, o, u`) are present and consonants `>= k`, count valid substrings.  
3. Shrink the window (`left` pointer) to check other valid substrings.  
4. Use two calls to `_atLeastK()` to compute **exactly `k`** consonants.  

## 📝 **Implementation**  

```python
from typing import Dict

class Solution:
    def _isVowel(self, c: str) -> bool:
        return c in {"a", "e", "i", "o", "u"}

    def _atLeastK(self, word: str, k: int) -> int:
        num_valid_substrings = 0
        start = 0
        end = 0
        vowel_count: Dict[str, int] = {}
        consonant_count = 0

        while end < len(word):
            new_letter = word[end]

            if self._isVowel(new_letter):
                vowel_count[new_letter] = vowel_count.get(new_letter, 0) + 1
            else:
                consonant_count += 1

            while len(vowel_count) == 5 and consonant_count >= k:
                num_valid_substrings += len(word) - end
                start_letter = word[start]
                
                if self._isVowel(start_letter):
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1

                start += 1

            end += 1

        return num_valid_substrings

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self._atLeastK(word, k) - self._atLeastK(word, k + 1)
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Sliding Window Traversal** | **O(n)** |
| **Updating Frequency Counts** | **O(1)** |
| **Overall Complexity** | **O(n)** ✅ |

✅ **Why is this efficient?**  
- We iterate over `word` **at most twice** with the sliding window technique.  
- Dictionary lookups and updates for vowels are **O(1)**.  

## 📂 **Project Structure**  

```
substr_vowel_consonant/
├── substrings_vowels_consonants.py  # Python solution
├── README.md                        # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Sliding Window** minimizes redundant computations.  
✔ **Dictionary + Counter** efficiently track vowel/consonant counts.  
✔ **Optimized O(n) approach** makes it scalable for large inputs.  

🚀 **Master this technique for advanced substring problems!** 🔥  
