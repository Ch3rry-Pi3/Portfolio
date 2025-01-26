# 📈 **LeetCode 121: Best Time to Buy and Sell Stock**

## 📌 **Overview**
This project solves **LeetCode Problem 121: Best Time to Buy and Sell Stock** using an **efficient two-pointer technique** to maximise profit when buying and selling a stock on different days.

### **Problem Statement**
Given an array `prices`, where `prices[i]` represents the price of a given stock on the `i`-th day, find the **maximum profit** you can achieve by choosing **one** day to buy a stock and **a later day** to sell it.

🔹 **Constraints:**
- You **must buy before selling** (i.e., `buy day < sell day`).
- If **no profit** can be made, return `0`.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
```

### **Example 2**
```python
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No transactions are done because the stock price keeps decreasing.
```

## 🚀 **How It Works: Sliding Window Approach**
Instead of checking **every possible buy-sell pair** (which is inefficient, `O(n²)`), we use a **two-pointer technique**:

### **Algorithm Steps**
1. **Initialise two pointers**:
   - `left` (buy day) → starts at day `0`.
   - `right` (sell day) → starts at day `1`.
2. **Move `right` through the list**:
   - If `prices[right] > prices[left]` → **calculate profit** and update `maxProfit`.
   - If `prices[right] < prices[left]` → **move `left` to right** (reset buy day).
3. **Continue until `right` reaches the end of the list**.

### **Implementation**
```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Finds the maximum profit that can be achieved from buying and selling stock.

        :param prices: List of stock prices
        :return: Maximum possible profit
        """
        left, right = 0, 1  # left = buy, right = sell
        maxProfit = 0

        while right < len(prices):
            # Check if it's profitable
            if prices[left] < prices[right]:
                # Calculate profit
                profit = prices[right] - prices[left]
                # Update maxProfit
                maxProfit = max(maxProfit, profit)
            else:
                # Move left pointer to right pointer's position
                left = right

            # Move right pointer forward
            right += 1

        return maxProfit
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|-----------------|
| **Brute Force (nested loops)** | **O(n²)** ❌ | **O(1)** |
| **Optimised Two-Pointer Approach** | **O(n)** ✅ | **O(1)** ✅ |

- **Brute force** iterates through **all buy-sell pairs** (too slow).
- **Sliding window approach** only makes **one pass**, making it **fast and memory-efficient**.

## 🏗 **Project Structure**

```
121. Best Time to Buy and Sell Stock/
├── buy_and_sell.py  # Efficient O(n) solution using two pointers
├── README.md        # Detailed explanation
```

### 📝 **`buy_and_sell.py`**
- **Implements the two-pointer approach for maximising stock trading profit.**
- **Optimised for O(n) time complexity.**

```python
def main():
    """
    Demonstrates finding the maximum profit from stock prices.
    """
    solver = Solution()
    
    test_cases = [
        [7, 1, 5, 3, 6, 4],     # Expected output: 5
        [7, 6, 4, 3, 1],        # Expected output: 0 (no profit)
        [2, 4, 1],              # Expected output: 2
        [3, 2, 6, 5, 0, 3]      # Expected output: 4
    ]

    for prices in test_cases:
        print(f"Stock prices: {prices}")
        result = solver.maxProfit(prices)
        print(f"Maximum Profit: {result}\n")

if __name__ == "__main__":
    main()
```

## 🔥 **Key Takeaways**
✅ **Uses two-pointer technique to maximise profit**
✅ **Efficient O(n) time complexity**
✅ **Handles cases where no profit is possible**

## 🚀 **Try It Yourself!**
- Clone the repository.
- Run `buy_and_sell.py` to test the function.

```bash
python buy_and_sell.py
```

## 🌟 **Future Improvements**
- 🏎 **Explore multi-transaction variations** where multiple buys/sells are allowed.
- 📈 **Optimise further using dynamic programming techniques**.

**🚀 Master stock trading problems with this efficient approach!**