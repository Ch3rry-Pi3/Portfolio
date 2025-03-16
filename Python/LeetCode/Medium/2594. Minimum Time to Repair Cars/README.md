# ⏳ **LeetCode 2594: Minimum Time to Repair Cars**  

## 📌 **Problem Overview**  

You are given an **integer array** `ranks`, where:  
- `ranks[i]` represents the **rank** of the `i-th` mechanic.  
- A mechanic with rank `r` can repair **n** cars in **r × n² minutes**.  

You are also given an **integer** `cars`, which represents the **total number of cars** waiting to be repaired.  

📢 **Objective**: Find the **minimum time required** to repair all `cars`, assuming that all mechanics **work simultaneously**.

## ✅ **Example 1**  

```python
Input: ranks = [4,2,3,1], cars = 10
Output: 16
```

### **Explanation:**  
- Mechanic **1** (rank = `4`) repairs **2 cars** → `4 × 2² = 16` minutes  
- Mechanic **2** (rank = `2`) repairs **2 cars** → `2 × 2² = 8` minutes  
- Mechanic **3** (rank = `3`) repairs **2 cars** → `3 × 2² = 12` minutes  
- Mechanic **4** (rank = `1`) repairs **4 cars** → `1 × 4² = 16` minutes  

🚗 **Total repair time** = **16 minutes (minimum possible)** ✅  

## ✅ **Example 2**  

```python
Input: ranks = [5,1,8], cars = 6
Output: 16
```

### **Explanation:**  
- Mechanic **1** (rank = `5`) repairs **1 car** → `5 × 1² = 5` minutes  
- Mechanic **2** (rank = `1`) repairs **4 cars** → `1 × 4² = 16` minutes  
- Mechanic **3** (rank = `8`) repairs **1 car** → `8 × 1² = 8` minutes  

🚗 **Total repair time** = **16 minutes** ✅  

## 🛠 **Approach & Intuition**  

### 🔹 **Binary Search on Time**  
Since the **minimum** time needs to be found, **binary search** is an efficient approach.  

#### **Key Observations:**  
1. The **minimum possible time** is `1`.  
2. The **maximum possible time** occurs when the **slowest mechanic (highest rank) repairs all cars**.  
3. **Binary search** helps optimize the search space efficiently.

#### **Steps:**  
1. **Set the search range**:  
   - `low = 1` (minimum time).  
   - `high = cars² × min(ranks)` (worst case).  
2. **Perform binary search on time (`mid`)**:  
   - Check if `mid` minutes allow repairing all `cars`.  
   - Use **sum of floor(√(mid / rank))** to count the number of cars repaired in `mid` time.  
   - If fewer cars are repaired, **increase time**.  
   - Otherwise, **try a smaller time**.

📌 **Why Binary Search?**  
- **Reduces search space exponentially** (`O(log max_time)`).  
- **Ensures optimal solution** in **O(n log max_time)** complexity.  

## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        Finds the minimum time needed to repair all cars.

        :param ranks: List of integers representing mechanic ranks.
        :param cars: Total number of cars to be repaired.
        :return: Minimum time required to repair all cars.
        """
        # Define the search space for binary search
        low, high = 1, cars * cars * min(ranks)

        # Perform binary search to find the optimal minimum time
        while low < high:
            mid = (low + high) // 2
            cars_repaired = sum(int((mid / rank) ** 0.5) for rank in ranks)

            # If we can repair at least 'cars' cars, try a smaller time
            if cars_repaired >= cars:
                high = mid
            else:
                low = mid + 1       # If not enough cars are repaired, increase time

        return low

```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Binary Search Range (`log max_time`)** | **O(log max_time)** ✅ |
| **Mechanic Calculation (`O(n)`)** | **O(n)** ✅ |
| **Overall Complexity** | **O(n log max_time)** ✅ |

🔹 **Why is this efficient?**  
- **Binary search reduces the search space** exponentially.  
- **Summation of square roots is performed in O(n)** for each binary search iteration.  

## 📂 **Project Structure**  

```
2594. Minimum Time to Repair Cars/
├── minimum_time.py   # Python solution
├── README.md         # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Binary search effectively finds the optimal repair time.**  
✔ **Greedy checking ensures all mechanics work simultaneously.**  
✔ **O(n log max_time) complexity is highly efficient.**  

🚀 **Master this technique for similar "minimum time" problems!** 🔥  