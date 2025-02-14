# 📌 **LeetCode 1352: Product of the Last K Numbers**

## 📖 **Problem Statement**
Design an algorithm that accepts a stream of integers and retrieves the **product** of the **last k** integers of the stream efficiently.

You need to implement the `ProductOfNumbers` class with the following methods:
- `ProductOfNumbers()`: Initializes an object with an empty stream.
- `void add(int num)`: Appends the integer `num` to the stream.
- `int getProduct(int k)`: Returns the product of the last `k` numbers in the stream.

🔹 If there are fewer than `k` numbers in the stream, return `0`.  
🔹 The test cases ensure that all contiguous sequences will fit into a **32-bit integer**.

---

## 🚀 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
["ProductOfNumbers", "add", "add", "add", "add", "add", "getProduct", "getProduct", "getProduct", "add", "getProduct"]
[[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]
```
#### **Output:**
```python
[null, null, null, null, null, null, 20, 40, 0, null, 32]
```
#### **Explanation:**
```python
product_of_numbers = ProductOfNumbers()
product_of_numbers.add(3)               # Stream: [3]
product_of_numbers.add(0)               # Stream: [3, 0] (Reset due to 0)
product_of_numbers.add(2)               # Stream: [2]
product_of_numbers.add(5)               # Stream: [2, 5]
product_of_numbers.add(4)               # Stream: [2, 5, 4]
product_of_numbers.getProduct(2)        # Output: 5 * 4 = 20
product_of_numbers.getProduct(3)        # Output: 2 * 5 * 4 = 40
product_of_numbers.getProduct(4)        # Output: 0 (reset happened)
product_of_numbers.add(8)               # Stream: [2, 5, 4, 8]
product_of_numbers.getProduct(2)        # Output: 4 * 8 = 32
```

---

## 🔍 **Intuition and Approach**
This problem requires efficiently retrieving the product of the last `k` numbers in the stream. A **brute-force** approach of storing all numbers and recalculating the product each time would be inefficient.

### **Optimised Approach: Using Prefix Product**
We use a **prefix product list** to store the cumulative product of all numbers in the stream:
1. **Maintain a cumulative product array** where `prefix_product[i]` stores the product of all elements up to index `i`.
2. **When a new number is added**, multiply it by the last stored product and append to the list.
3. **If a 0 is added**, reset the entire list since multiplication by zero invalidates previous products.
4. **To get the product of last `k` numbers**, use **division**:
   - If `prefix_product = [1, a, a*b, a*b*c, a*b*c*d]`
   - The last `k` product is computed as `prefix_product[n] / prefix_product[n-k]`
   - This ensures an **O(1) lookup time**.

---

## 🛠 **Optimised Python Solution**
```python
class ProductOfNumbers:
    """
    A class that maintains a stream of integers and allows retrieving the product 
    of the last k elements in the stream efficiently.
    """

    def __init__(self):
        """
        Initialises an empty stream with a prefix product list.
        The list starts with 1 to handle multiplication logic seamlessly.
        """
        self.prefix_product = [1]
        self.size = 0

    def add(self, num: int):
        """
        Appends an integer to the stream.
        
        If the number is 0, the entire prefix product list is reset, 
        as multiplication with 0 invalidates previous values.

        Args:
            num (int): The number to be added to the stream.
        """
        if num == 0:
            # Reset on zero since it invalidates all previous products.
            self.prefix_product = [1]
            self.size = 0
        else:
            # Append the cumulative product of the current number with the last product.
            self.prefix_product.append(self.prefix_product[-1] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        """
        Retrieves the product of the last k numbers in the current list.

        Args:
            k (int): The number of last elements to consider for the product.

        Returns:
            int: The product of the last k elements or 0 if k exceeds the list size.
        """
        if k > self.size:
            return 0  # If k is greater than available numbers, return 0.

        # Compute product efficiently using division of prefix products.
        return self.prefix_product[-1] // self.prefix_product[-k - 1]
```

---

## ⏳ **Complexity Analysis**
| Operation       | Time Complexity | Space Complexity |
|----------------|----------------|------------------|
| `add(num)`     | **O(1)**        | **O(N)** (stores prefix product) |
| `getProduct(k)`| **O(1)**        | **O(1)** (uses division for quick lookup) |
| **Total Complexity** | **O(N) time, O(N) space** | ✅ Efficient |

---

## 🎯 **Why This Approach?**
✅ **Efficient Retrieval**: Using **prefix product** allows O(1) retrieval of last `k` product.  
✅ **Handles Zeros Gracefully**: A `0` resets the list since multiplication invalidates previous values.  
✅ **Scalable**: Works efficiently for large streams.  

🚀 **With this approach, you can quickly process a stream of numbers and retrieve last `k` products in O(1) time!** 🎯

---

## 🏆 **Key Takeaways**
- **Brute-force recalculations** for each query would be inefficient.
- **Prefix product arrays** enable **fast O(1) retrieval**.
- **Reset on encountering `0`** since multiplication nullifies previous results.

This method ensures an **optimal balance of time and space complexity**, making it ideal for handling real-time streams. 🚀