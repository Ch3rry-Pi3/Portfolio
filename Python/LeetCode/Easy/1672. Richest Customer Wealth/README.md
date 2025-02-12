# 💰 **LeetCode 1672: Richest Customer Wealth**

## 📌 **Problem Overview**
You are given an **m × n** integer grid **`accounts`**, where:  
- `accounts[i][j]` represents the **amount of money** the `i`-th customer has in the `j`-th bank.  
- The **wealth** of a customer is defined as the **sum of all the money** they have across all banks.  
- The **richest customer** is the one with the **maximum wealth**.  

💡 **Goal:** Return the **maximum** wealth that any customer has.

## 🔍 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
accounts = [[1, 2, 3], [3, 2, 1]]
```
#### **Output:**
```python
6
```
#### **Explanation:**
- **Customer 1** has wealth = **1 + 2 + 3 = 6**  
- **Customer 2** has wealth = **3 + 2 + 1 = 6**  
- Both have equal wealth of **6**, so return **6**.

### **Example 2**
#### **Input:**
```python
accounts = [[1, 5], [7, 3], [3, 5]]
```
#### **Output:**
```python
10
```
#### **Explanation:**
- **Customer 1** has wealth = **1 + 5 = 6**  
- **Customer 2** has wealth = **7 + 3 = 10**  
- **Customer 3** has wealth = **3 + 5 = 8**  
- The richest customer has **10**, so return **10**.

### **Example 3**
#### **Input:**
```python
accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
```
#### **Output:**
```python
17
```
#### **Explanation:**
- **Customer 1** has wealth = **2 + 8 + 7 = 17**  
- **Customer 2** has wealth = **7 + 1 + 3 = 11**  
- **Customer 3** has wealth = **1 + 9 + 5 = 15**  
- The richest customer has **17**, so return **17**.

## 🛠 **Approach**
This problem can be efficiently solved using a **simple iteration**:

1. **Initialise a variable** `max_wealth` to keep track of the richest customer’s wealth.
2. **Iterate through each customer's account** in `accounts`:
   - Compute their **total wealth** by summing the bank balances.
   - Update `max_wealth` if the current wealth is **greater**.
3. **Return `max_wealth`** as the answer.

This approach ensures a **fast and efficient solution** with a linear time complexity.

## 🚀 **Optimised Python Solution**
```python
from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Computes the maximum wealth among all customers.

        Args:
            accounts (List[List[int]]): A 2D list where accounts[i][j] represents 
                                        the amount of money the i-th customer has in the j-th bank.

        Returns:
            int: The maximum wealth that any customer has.
        """

        # Initialise the maximum wealth seen so far to 0 (the minimum wealth possible)
        max_wealth_so_far = 0
        
        # Iterate over accounts
        for account in accounts:
            # Compute the total wealth of the current customer
            curr_customer_wealth = sum(account)
            
            # Update the maximum wealth if the current customer's wealth is greater
            max_wealth_so_far = max(max_wealth_so_far, curr_customer_wealth)
            
        # Return the maximum wealth
        return max_wealth_so_far
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Iterate through accounts | `for account in accounts` | **O(m)** |
| Compute wealth | `sum(account)` | **O(n)** |
| Track max wealth | `max()` operation | **O(1)** |
| **Total Complexity** | **O(m × n)** (m = customers, n = banks) | ✅ Linear |

## 🎯 **Why This Approach?**
✔ **Simple iteration**, no extra space required ✅  
✔ **O(m × n) complexity**, optimal for this problem ✅  
✔ **Straightforward implementation**, easy to understand ✅  

With this approach, we can quickly determine the **richest customer's wealth** 💰🚀
