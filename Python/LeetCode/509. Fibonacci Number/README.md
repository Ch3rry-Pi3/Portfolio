# 📉 **LeetCode 509: Fibonacci Number**

## 📌 **Overview**
The **Fibonacci sequence** is one of the most well-known sequences in mathematics. This project solves **LeetCode Problem 509: Fibonacci Number** using two different approaches:

1. 💡 **Recursive Approach** – A simple but inefficient method using recursion.
2. ⚡ **Optimised Approach** – A faster version using **memoisation** (caching).

This project helps you:
- ✨ **Understand recursion and its working principles**.
- ⌛ **Analyse time complexity and why naive recursion is slow**.
- ♻️ **Optimise recursive solutions using memoisation**.

## 🎯 **Problem Statement**
Given an integer `n`, return the `n`th Fibonacci number.

### ✨ **Fibonacci Sequence Definition**

```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2), for n >= 2
```

👉 Each number is the **sum of the two previous numbers** in the sequence.

**Example:**
```python
Input: n = 5
Output: 5
Explanation:
F(5) = F(4) + F(3)
     = (3 + 2)
     = 5
```

## 🚀 **How It Works**

### 🏃️ **Step-by-Step Execution (Recursive Approach)**
Let's compute `fib(5)` **manually** using recursion.

```
fib(5) = fib(4) + fib(3)
       = (fib(3) + fib(2)) + (fib(2) + fib(1))
       = ((fib(2) + fib(1)) + fib(0)) + (fib(1) + fib(0)) + fib(1)
       = ((1 + 0) + 1) + (1 + 0) + 1
       = 2 + 1 + 1
       = 5
```

### 🌌 **Why Recursion Works**
Each Fibonacci number is built from **previous results**. The function **keeps breaking the problem down** until it reaches the **base cases** (`F(0)` or `F(1)`).

- 🔄 **Recursive calls keep breaking the problem into smaller parts.**
- ⏳ **Each call waits for previous calls to finish before returning a result.**
- ⚠️ **This results in duplicate calculations, making recursion inefficient!**

## 🔢 **Time Complexity Breakdown**

### 🔮 **Recursive Complexity: Why is it O(2ⁿ)?**

The recursive Fibonacci function follows this recurrence:
\[
T(n) = T(n-1) + T(n-2) + O(1)
\]
This creates an **exponential number of calls**:
\[
T(n) \approx O(1.618^n) \approx O(2^n)
\]

### 📈 **Growth of Recursive Calls**
| `n` | Estimated Calls (`O(2^n)`) |
|----|------------------|
| 5  | 10  |
| 10  | 1000  |
| 20  | 1,000,000  |
| 30  | 1,000,000,000  |
| 50  | 🔥 Too slow! 🔥  |

## 📝 **Project Structure**

```
leetcode_509_fibonacci/
├── recursive_fib.py      # Naïve recursive Fibonacci (O(2^n))
├── optimised_fib.py      # Memoised Fibonacci (O(n))
├── README.md             # Explanation and walkthrough
```

### 📝 `recursive_fib.py`  
- **Implements the naive recursive Fibonacci function.**  
- **Inefficient** due to repeated calculations.

```python
class FibonacciRecursive:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
```

### 📝 `optimised_fib.py`  
- **Uses memoisation** to store results in a dictionary.  
- **Reduces time complexity from O(2ⁿ) to O(n)**.

```python
class FibonacciOptimised:
    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        if n <= 1:
            return n
        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]
```

## 💡 **How to Run the Code**

### 🛠️ **Run Recursive Fibonacci**
```bash
python recursive_fib.py
```
➡️ Enter a number when prompted.

### 🛠️ **Run Optimised Fibonacci**
```bash
python optimised_fib.py
```
➡️ Enter a number when prompted.

## 🚀 **Key Takeaways**
✅ **The recursive method is simple but inefficient**
✅ **The optimised method is much faster due to caching**
✅ **Memoisation reduces the time complexity from O(2ⁿ) to O(n)**

## 🛠️ **Future Improvements**
- 🔄 **Iterative Approach:** Use loops instead of recursion.
- 📊 **Dynamic Programming:** Store results in an array instead of a dictionary.

**🚀 Try it out and see the performance difference!**

