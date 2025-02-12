# 🎯 **LeetCode 2342: Max Sum of a Pair With Equal Sum of Digits**  

## 📌 **Problem Overview**  
You are given a **0-indexed** array `nums` consisting of **positive integers**.  

Your goal is to find **two indices** `i` and `j` (where `i ≠ j`) such that:  
1. The **sum of digits** of `nums[i]` is **equal** to the sum of digits of `nums[j]`.  
2. The **maximum value** of `nums[i] + nums[j]` is obtained over all valid pairs `(i, j)`.  

If no such pair exists, return `-1`.  

## 🔍 **Intuition**  

### **Understanding the Key Constraint: "Equal Sum of Digits"**  
Rather than comparing raw values in the array, we must **group numbers based on their digit sum**.  
- Example:  
  - `18 → sum(1 + 8) = 9`
  - `36 → sum(3 + 6) = 9`
  - `43 → sum(4 + 3) = 7`
  - `13 → sum(1 + 3) = 4`
  - `7 → sum(7) = 7`

Grouping these by **digit sum**:
```
9 → [18, 36]
7 → [43, 7]
4 → [13]
```
- Since `18` and `36` both have a digit sum of `9`, the pair `(18, 36)` satisfies the condition.
- Their sum is `18 + 36 = 54`, which is the **maximum possible sum**.

### 🛠 **Approach**  

1. **Compute the Digit Sum for Each Number**  
   - Store numbers along with their **digit sum** in a list.  
   
2. **Sort Based on Digit Sum (Primary) and Number Value (Secondary)**  
   - Sorting ensures **adjacent elements** in the list will belong to the same digit sum group.  
   
3. **Iterate Through Sorted List and Track Maximum Sum**  
   - Whenever two consecutive elements have the same digit sum, compute their sum.  
   - Update the maximum sum found so far.  

This **sorting approach** is efficient since it ensures we only need a **single pass** to compute the maximum sum among valid pairs.

## 🚀 **Python Solution**  

```python
from typing import List

class Solution:
    def calculate_digit_sum(self, num: int) -> int:
        """
        Computes the sum of digits of a given number.

        Args:
            num (int): The input number.

        Returns:
            int: The sum of the digits of the number.
        """
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def maximumSum(self, nums: List[int]) -> int:
        """
        Finds the maximum sum of a pair of numbers in the list where both numbers have the same digit sum.

        Args:
            nums (List[int]): A list of positive integers.

        Returns:
            int: The maximum sum of a pair with the same digit sum, or -1 if no such pair exists.
        """
        digit_sum_pairs = []

        # Store numbers with their digit sums as pairs
        for number in nums:
            digit_sum = self.calculate_digit_sum(number)
            digit_sum_pairs.append((digit_sum, number))

        # Sort based on digit sums, and if equal, by number value
        digit_sum_pairs.sort()

        max_pair_sum = -1

        # Iterate through the sorted array to find the maximum sum of pairs
        for index in range(1, len(digit_sum_pairs)):
            current_digit_sum = digit_sum_pairs[index][0]
            previous_digit_sum = digit_sum_pairs[index - 1][0]

            # If two consecutive numbers have the same digit sum
            if current_digit_sum == previous_digit_sum:
                current_sum = digit_sum_pairs[index][1] + digit_sum_pairs[index - 1][1]
                max_pair_sum = max(max_pair_sum, current_sum)

        return max_pair_sum
```

## 📌 **Example Walkthrough**  

### **Example 1**  
#### **Input:**  
```python
nums = [18, 43, 36, 13, 7]
```
#### **Step 1: Compute Digit Sums**  
| Number | Digit Sum |
|---------|----------|
| 18      | 9        |
| 43      | 7        |
| 36      | 9        |
| 13      | 4        |
| 7       | 7        |

#### **Step 2: Group Numbers by Digit Sum**
```
9 → [18, 36]
7 → [43, 7]
4 → [13]
```
#### **Step 3: Find the Maximum Pair Sum**
- The only valid pair is `(18, 36)` since both have a sum of digits **9**.
- Their sum is `18 + 36 = 54`.

#### **Output:**  
```python
54
```

### **Example 2**  
#### **Input:**  
```python
nums = [10, 12, 19, 14]
```
#### **Step 1: Compute Digit Sums**  
| Number | Digit Sum |
|---------|----------|
| 10      | 1        |
| 12      | 3        |
| 19      | 10       |
| 14      | 5        |

#### **Step 2: Group Numbers by Digit Sum**
```
1 → [10]
3 → [12]
10 → [19]
5 → [14]
```
#### **Step 3: No Valid Pairs Exist**
- There are no pairs with the same digit sum.

#### **Output:**  
```python
-1
```

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Compute Digit Sums | `O(N)` | **O(N)** |
| Sort Numbers | `O(N log N)` | **O(N log N)** |
| Find Maximum Pair Sum | `O(N)` | **O(N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Sorting ensures consecutive elements in the list have the same digit sum**  
✔ **We only traverse the array once after sorting**  
✔ **Efficient and optimal for large input sizes**  

🚀 **With this approach, you can quickly determine the maximum sum of pairs with the same digit sum!** 🎯

## 🔥 **Key Takeaways**  
- **Digit sum comparison** is the key constraint.  
- **Sorting simplifies finding valid pairs**.  
- **Time Complexity: O(N log N) due to sorting, otherwise O(N) for computation.**  
