# √ **LeetCode 69: Sqrt(x)**

## 📌 **Overview**
This project solves **LeetCode Problem 69: Sqrt(x)** using **binary search** to efficiently compute the integer square root of `x`.

### **Problem Statement**
Given a **non-negative integer** `x`, return **the square root of `x` rounded down** to the nearest integer.

**Constraints:**
- **Do not use** built-in exponentiation functions like `pow(x, 0.5)` or `x ** 0.5`.
- `0 <= x <= 2³¹ - 1`

### **Example Walkthrough**
#### **Example 1**
```python
Input: x = 4
Output: 2
Explanation: sqrt(4) = 2, so we return 2.
```

#### **Example 2**
```python
Input: x = 8
Output: 2
Explanation: sqrt(8) = 2.82842..., and since we round down, we return 2.
```

## 🚀 **How It Works: Step-by-Step Explanation**
### **Approach: Using Binary Search**
Instead of iterating up to `x`, we can use **binary search** to efficiently find the square root.

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        result = 0

        while left <= right:
            middle = left + ((right - left) // 2)
            if middle * middle > x:
                right = middle - 1
            elif middle * middle < x:
                left = middle + 1
                result = middle
            else:
                return middle
        return result
```

## 🌌 **Step-by-Step Breakdown**
### **1️⃣ Initialise Binary Search Range**
```python
left, right = 0, x
result = 0
```
- `left` starts at `0` because `sqrt(x) >= 0`.
- `right` starts at `x` since `sqrt(x) <= x`.
- `result` stores the **largest integer square root found** so far.

### **2️⃣ Run Binary Search**
```python
while left <= right:
    middle = left + ((right - left) // 2)
```
- While `left` is less than or equal to `right`, continue searching.
- Compute `middle` to avoid integer overflow.

### **3️⃣ Compare `middle²` with `x`**
```python
if middle * middle > x:
    right = middle - 1
```
- If `middle² > x`, the square root must be **smaller**, so move `right` to `middle - 1`.

```python
elif middle * middle < x:
    left = middle + 1
    result = middle
```
- If `middle² < x`, the square root must be **larger**, so move `left` to `middle + 1`.
- Update `result` because this `middle` is the **largest valid square root found so far**.

```python
else:
    return middle
```
- If `middle² == x`, return `middle` immediately as the **exact square root**.

### **4️⃣ Return the Largest Integer Square Root**
```python
return result
```
- If the loop exits, return the **largest valid `result`** found.

## 🌐 **Example Walkthrough**: `mySqrt(8)`

| `left` | `right` | `middle` | `middle²` | Action |
|--------|--------|----------|------------|---------|
| 0 | 8 | 4 | 16 | `middle² > x`, move `right` to `middle - 1` |
| 0 | 3 | 1 | 1 | `middle² < x`, move `left` to `middle + 1`, store `result = 1` |
| 2 | 3 | 2 | 4 | `middle² < x`, move `left` to `middle + 1`, store `result = 2` |
| 3 | 3 | 3 | 9 | `middle² > x`, move `right` to `middle - 1` |

🔹 **Loop ends** (`left > right`), so we return **`result = 2`** ✅.

## 🔢 **Time Complexity Analysis**
### **Why is Binary Search Efficient?**
Instead of checking **every number up to `x`**, we use **binary search** to cut the search space in half each time.

| Approach | Time Complexity |
|----------|----------------|
| Brute-force | O(√x) |
| **Binary Search** | **O(log x)** ✅ |

Binary search reduces the problem size **exponentially**, making it **much faster** than a simple loop.

## 📝 **Project Structure**

```
69. Sqrt(x)/
├── sqrt_binary_search.py  # Efficient O(log x) solution
├── README.md              # Detailed explanation
```

### 📝 `sqrt_binary_search.py`
- **Implements the binary search approach for finding sqrt(x).**
- **Fast and efficient compared to naive methods.**

```python
if __name__ == "__main__":
    solver = Solution()
    x = int(input("Enter a number: "))
    print(f"Square root of {x} (rounded down) = {solver.mySqrt(x)}")
```

## 🚀 **Key Takeaways**
✅ **Binary search efficiently finds the integer square root**
✅ **Time complexity is reduced to O(log x) instead of O(√x)**
✅ **No floating-point calculations are needed**

## 🌟 **Future Improvements**
- 🛠️ **Newton's Method**: Implement an **O(log x)** solution using Newton's Iterative Method.
- ✨ **Bit Manipulation**: Explore **bitwise methods** to find sqrt(x) even faster.

**🚀 Try it out and see how fast binary search is!**

