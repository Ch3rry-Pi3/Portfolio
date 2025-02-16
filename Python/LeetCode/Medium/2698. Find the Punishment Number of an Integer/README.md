# 🔢 **LeetCode 2698: Find the Punishment Number of an Integer**  

## 📌 **Problem Overview**  
Given a **positive integer** `n`, we define its **punishment number** as the sum of the squares of all integers `i` such that:  

- The **square of `i`** can be partitioned into contiguous substrings.  
- The sum of those substrings equals `i`.  

### **Example Condition**  
For a number `i`, check if `i²` can be split into substrings whose sum equals `i`.  

### **Goal**  
Compute the **punishment number** for `n`, which is the sum of squares of all valid `i`.  

## 🧩 **Understanding the Partitioning Condition**  
A number `i` satisfies the condition if:  
1. **Compute `i²`**.  
2. **Check if it can be partitioned** into contiguous substrings such that their sum equals `i`.  
3. **Sum up all valid `i²`** to get the final answer.

## 📝 **Example Walkthrough**  
### **Example 1**  
#### **Input:**  
```python
n = 10
```
#### **Step-by-Step Validation:**  
| `i`  | `i²`  | Valid Partitioning? | Partition Sum |
|------|------|-------------------|---------------|
| 1    | 1    | ✅ Yes | `1` = 1 |
| 9    | 81   | ✅ Yes | `8 + 1` = 9 |
| 10   | 100  | ✅ Yes | `10 + 0` = 10 |

#### **Output Calculation:**  
```python
1² + 9² + 10² = 1 + 81 + 100 = 182
```
#### **Output:**  
```python
182
```

### **Example 2**  
#### **Input:**  
```python
n = 37
```
#### **Valid Numbers and Partitioning:**  
| `i`  | `i²`  | Valid Partitioning? | Partition Sum |
|------|------|-------------------|---------------|
| 1    | 1    | ✅ Yes | `1` = 1 |
| 9    | 81   | ✅ Yes | `8 + 1` = 9 |
| 10   | 100  | ✅ Yes | `10 + 0` = 10 |
| 36   | 1296 | ✅ Yes | `1 + 29 + 6` = 36 |

#### **Output Calculation:**  
```python
1² + 9² + 10² + 36² = 1 + 81 + 100 + 1296 = 1478
```
#### **Output:**  
```python
1478
```

## 🛠 **Approach**  
1. **Iterate through `i` from `1` to `n`**.  
2. **Compute `i²`**.  
3. **Check if `i²` can be partitioned** to sum to `i`.  
4. **Use recursion** to check different partition possibilities.  
5. **If valid, add `i²` to the total punishment number**.  

## 🚀 **Python Solution**  
```python
class Solution:
    def can_partition(self, num: int, target: int) -> bool:
        """
        Recursively checks if the given number's square can be partitioned
        into contiguous substrings that sum up to the target value.

        Args:
            num (int): The square of a number.
            target (int): The original number to match by partitioning.

        Returns:
            bool: True if a valid partition exists, False otherwise.
        """
        # Invalid partition found
        if target < 0 or num < target:
            return False

        # Valid partition found
        if num == target:
            return True

        # Recursively check all partitions for a valid partition
        return (
            self.can_partition(num // 10, target - num % 10)
            or self.can_partition(num // 100, target - num % 100)
            or self.can_partition(num // 1000, target - num % 1000)
        )

    def punishmentNumber(self, n: int) -> int:
        """
        Calculates the punishment number for a given integer n.

        The punishment number is the sum of the squares of numbers in the range
        [1, n] whose squared values can be partitioned into contiguous substrings
        summing to the original number.

        Args:
            n (int): The upper limit of the range.

        Returns:
            int: The punishment number.
        """
        punishment_num = 0

        # Iterate through numbers in range [1, n]
        for current_num in range(1, n + 1):
            square_num = current_num * current_num

            # Check if valid partition can be found and add squared number if so
            if self.can_partition(square_num, current_num):
                punishment_num += square_num

        return punishment_num
```

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Iterating through numbers | `for i in range(1, n + 1)` | **O(n)** |
| Checking partitions | Recursion depth for partitioning | **O(log(i²))** |
| Storing & summing punishment numbers | **O(1)** |
| **Total Complexity** | **O(n log n)** | ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Recursive Partition Checking** ensures all valid splits are checked.  
✔ **Efficient Iteration** through numbers instead of brute force approaches.  
✔ **Guaranteed Correctness** by checking multiple partitions at different levels.  

🚀 **This approach effectively determines the punishment number in an optimised way!** 🎯