# 🔄 **LeetCode 190: Reverse Bits**

## 📌 **Overview**
This project solves **LeetCode Problem 190: Reverse Bits**.  
The task is to **reverse the bits of a given 32-bit unsigned integer** and return the decimal representation of the reversed binary number.

### **Problem Statement**
Given a **32-bit unsigned integer** `n`, reverse its bits and return the corresponding integer.

🔹 **Constraints:**
- The input **must be** a binary string of **length 32**.
- The integer is treated as **unsigned**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: n = 00000010100101000001111010011100
Output: 964176192
```
**Explanation:**
- The **binary representation** of `n` is `00000010100101000001111010011100`.
- Reversing these bits gives `00111001011110000010100101000000`.
- The **decimal equivalent** of `00111001011110000010100101000000` is `964176192`.

### **Example 2**
```python
Input: n = 11111111111111111111111111111101
Output: 3221225471
```
**Explanation:**
- The binary representation of `n` is `11111111111111111111111111111101`.
- Reversing these bits gives `10111111111111111111111111111111`.
- The decimal equivalent is `3221225471`.

## 🛠 **Solution Approach**  
### 🔍 **Understanding the Algorithm**  
We use **bitwise operations** to reverse the bits efficiently:

1. **Iterate through all 32 bits** (since `n` is a 32-bit integer).
2. **Left shift `result` by 1** to make space for the new bit.
3. **Extract the least significant bit** of `n` (`n % 2` or `n & 1`) and add it to `result`.
4. **Right shift `n` by 1**, so that the next bit moves to the least significant position.
5. **Repeat 32 times**, ensuring all bits are reversed.

### 🔄 **Step-by-Step Example**
Let's reverse the bits for `n = 1010` (binary):

| Step | `result << 1` | `result += (n % 2)` | `n >> 1` |
|------|--------------|------------------|----------|
| 1    | `0000`         | `0000`             | `101`   |
| 2    | `0000`         | `0001`             | `010`   |
| 3    | `0010`         | `0010`             | `001`   |
| 4    | `00100`        | `00101`            | `_`     |

Final result: `1010` → **`0101`**  

## 📝 **Code Implementation**
```python
from typing import List

class Solution:
    """
    A class to reverse the bits of a given 32-bit unsigned integer.
    """

    def reverseBits(self, n: int) -> int:
        """
        Reverses the bits of a given 32-bit unsigned integer.

        :param n: An integer representing a 32-bit unsigned value.
        :return: The integer obtained after reversing its bits.
        """
        result = 0  # Store the reversed bits

        for i in range(32):             # Loop through all 32 bits
            result = result << 1        # Shift result left to make space
            bit = n & 1                 # Extract the last bit
            result += bit               # Append the extracted bit to result
            n = n >> 1                  # Right shift n to process the next bit

        return result

def main():
    """
    Demonstrates the reverseBits function with a sample input.
    """
    solution = Solution()
    
    # Example input: Binary representation of 43261596
    n = 43261596
    reversed_bits = solution.reverseBits(n)
    
    print(f"Original: {bin(n)} ({n})")
    print(f"Reversed: {bin(reversed_bits)} ({reversed_bits})")

if __name__ == "__main__":
    main()
```

## ⏳ **Time and Space Complexity**  
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Iterating through 32 bits** | **O(1)** ✅ | **O(1)** ✅ |

- **The loop runs exactly 32 times**, making the approach **O(1)**.
- **No extra space is used**, only integer variables (**O(1)**).

## 🏗 **Project Structure**  
```
190. Reverse Bits/
├── reverse_bits.py    # Python implementation of the solution
├── README.md          # Detailed explanation & walkthrough
```

🚀 **Mastering bitwise operations makes you a more efficient programmer!**
