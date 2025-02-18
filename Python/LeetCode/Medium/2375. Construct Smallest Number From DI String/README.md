# 🔢 **LeetCode 2375: Construct Smallest Number From DI String**  

## 📌 **Problem Overview**  
Given a **DI string pattern**, construct the **lexicographically smallest** number that satisfies the pattern rules.

- A **DI string** consists of characters `'I'` and `'D'`:
  - `'I'` means **increasing** → `num[i] < num[i+1]`
  - `'D'` means **decreasing** → `num[i] > num[i+1]`
- The **result must be a permutation** of digits `1-9`, where **each digit is used exactly once**.

### **Example 1**  
```python
Input: pattern = "IIIIDDD"
Output: "123549876"
```
✅ **Explanation:**  
- The first 4 positions must be **increasing** → `1 < 2 < 3 < 5`
- The last 3 positions must be **decreasing** → `9 > 8 > 7 > 6`
- `123549876` is the **smallest valid number**.

### **Example 2**  
```python
Input: pattern = "DDD"
Output: "4321"
```
✅ **Explanation:**  
- Since all characters are **'D'**, the smallest lexicographical number is **4321**.

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Stack-Based Approach**  
1. **Use a Stack to process numbers in reverse order**:
   - If we encounter `'D'`, we push the next number onto the stack.
   - If we encounter `'I'` (or reach the end), we pop the stack and append to the result.
2. **Why does this work?**
   - Using a stack ensures that when encountering `'I'`, the numbers pop out **in increasing order**, and when encountering `'D'`, we delay popping to form a **decreasing sequence**.

📌 **Illustration for `"IDID"`:**  
| Step | Stack | Output |
|------|-------|--------|
| Push `1` | `[1]` | `[]` |
| 'I' → Pop | `[]` | `[1]` |
| Push `2` | `[2]` | `[1]` |
| Push `3` | `[2,3]` | `[1]` |
| 'D' → Pop | `[2]` | `[1,3]` |
| Push `4` | `[2,4]` | `[1,3]` |
| 'I' → Pop | `[2]` | `[1,3,4]` |
| 'D' → Pop | `[]` | `[1,3,4,2]` |

✅ **Final Output** → `"13254"`  

## 📝 **Implementation**  

```python
class Solution:
    """
    This class generates the lexicographically smallest number 
    that follows the given DI pattern.
    """

    def smallestNumber(self, pattern: str) -> str:
        """
        Constructs the smallest number that satisfies the DI pattern.

        :param pattern: A string consisting of 'I' (increasing) and 'D' (decreasing).
        :return: The smallest lexicographical valid number as a string.
        """

        result = []         # Stores the final output sequence
        stack = []          # Stack to help generate the smallest sequence

        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))        # Push the next number onto the stack

            # When we reach 'I' or the end of the pattern, pop the stack to form the result
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())

        return "".join(result)

```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| Iterating over `pattern` | **O(n)** |
| Stack operations (`push` and `pop`) | **O(n)** |
| String concatenation | **O(n)** |
| **Overall Complexity** | **O(n)** ✅ |

🔹 **Why is this optimal?**  
- Instead of brute-force searching all permutations (**O(n!)**), **this method constructs the solution efficiently in O(n)**.

## 📂 **Project Structure**  

```
2375. Construct Smallest Number From DI String/
├── smallest_number_from_di_string.py  # Python solution
├── README.md                          # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Stack-based approach** ensures correctness while maintaining **O(n) complexity**.  
✔ **Greedy strategy** constructs the smallest valid permutation **incrementally**.  
✔ **Intuitive and memory-efficient solution** compared to brute force.

🚀 **Master this pattern for future DI-based problems!** 🔥  