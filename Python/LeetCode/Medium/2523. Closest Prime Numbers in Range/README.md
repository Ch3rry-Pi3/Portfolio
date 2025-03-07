# 🔢 **LeetCode 2523: Closest Prime Numbers in Range**  

## 📌 **Problem Overview**  

Given two positive integers, **left** and **right**, find the two integers **num1** and **num2** such that:  

- **left ≤ num1 < num2 ≤ right**  
- Both **num1** and **num2** are **prime numbers**.  
- **num2 - num1** is the **smallest possible difference** among all valid pairs.  
- If multiple pairs exist, return the one with the **smallest num1** value.  
- If no such numbers exist, return `[-1, -1]`.  

## 💡 **Examples**  

### **Example 1**  
```python
Input: left = 10, right = 19  
Output: [11, 13]  
```
✅ **Explanation:**  
- The **prime numbers** between **10 and 19** are **[11, 13, 17, 19]**.  
- The closest gap is **2**, achieved by **[11, 13]** and **[17, 19]**.  
- Since **11 < 17**, we return **[11, 13]**.

### **Example 2**  
```python
Input: left = 4, right = 6  
Output: [-1, -1]  
```
✅ **Explanation:**  
- The only **prime number** in this range is **5**.  
- Since we need **two** prime numbers, the conditions **cannot** be met.  
- We return `[-1, -1]`.

### **Example 3**  
```python
Input: left = 1, right = 100  
Output: [2, 3]  
```
✅ **Explanation:**  
- The **first two prime numbers** in this range are **2 and 3**.  
- Their difference is **1**, which is the smallest possible.  

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Sieve of Eratosthenes + Prime Filtering**  
1. **Use the Sieve of Eratosthenes** to efficiently find all prime numbers up to `right`.  
2. **Extract prime numbers in the range** `[left, right]`.  
3. **Find the closest prime pair** by iterating over the extracted list.  

📌 **Why does this work?**  
- The **Sieve of Eratosthenes** runs in **O(N log log N)**, making it highly efficient.  
- **Filtering primes** in the range is **O(N)**.  
- **Finding the closest pair** takes **O(N)**.

## 📝 **Implementation**  

```python
from typing import List, Tuple

class Solution:
    """
    Solution to find the closest pair of prime numbers in a given range.
    """

    def _sieve(self, upper_limit: int) -> List[bool]:
        """
        Implements the Sieve of Eratosthenes to find prime numbers up to a given limit.

        :param upper_limit: int - The upper bound for prime number checking.
        :return: List[bool] - Boolean list where True represents a prime number.
        """
        sieve = [True] * (upper_limit + 1)
        sieve[0] = sieve[1] = False         # 0 and 1 are not prime

        for number in range(2, int(upper_limit**0.5) + 1):
            if sieve[number]:
                for multiple in range(number * number, upper_limit + 1, number):
                    sieve[multiple] = False
        return sieve

    def closestPrimes(self, left: int, right: int) -> Tuple[int, int]:
        """
        Finds the closest pair of prime numbers within the given range.

        :param left: int - Lower bound of the range.
        :param right: int - Upper bound of the range.
        :return: Tuple[int, int] - The closest prime pair, or (-1, -1) if no valid pair exists.
        """
        # Step 1: Compute all prime numbers up to 'right'
        sieve_array = self._sieve(right)

        # Step 2: Filter primes within the given range
        prime_numbers = [num for num in range(left, right + 1) if sieve_array[num]]

        # Step 3: Find the closest prime pair
        if len(prime_numbers) < 2:
            return -1, -1       # If there are fewer than two primes, return [-1, -1]

        min_difference = float("inf")
        closest_pair = (-1, -1)

        for index in range(1, len(prime_numbers)):
            difference = prime_numbers[index] - prime_numbers[index - 1]
            if difference < min_difference:
                min_difference = difference
                closest_pair = (prime_numbers[index - 1], prime_numbers[index])

        return closest_pair
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Sieve of Eratosthenes** | **O(N log log N)** |
| **Filtering primes in range** | **O(N)** |
| **Finding the closest pair** | **O(N)** |
| **Overall Complexity** | **O(N log log N)** ✅ |

🔹 **Why is this optimal?**  
- The **Sieve of Eratosthenes** ensures we compute primes efficiently.  
- We only **iterate over primes** instead of checking primality per number.  

## 📂 **Project Structure**  

```
closest_prime_numbers/
├── closest_prime_numbers.py  # Python solution
├── README.md                 # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses Sieve of Eratosthenes** for efficient prime number filtering.  
✔ **Finds the closest prime pair** in **O(N)** time.  
✔ **Handles edge cases** (no valid pairs, large input ranges).  

🚀 **Master this approach for optimised prime number problems!** 🔢🔥  
