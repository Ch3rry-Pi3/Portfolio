# 🚗 **LeetCode 853: Car Fleet**

## 📌 **Problem Overview**
You are given **`n` cars** at different starting positions on a **one-lane** road, all trying to reach the **same destination** (`target`). Each car has a certain **speed**, and **a car cannot pass another car**. However, a **slower car** can be caught up by a **faster car**, and they will then move together as a **fleet** at the speed of the slower car.

**Goal:**  
Return the **number of car fleets** that will arrive at the destination.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
```
#### **Output:**
```python
3
```
#### **Explanation:**
- **Car at 10** (speed 2) and **car at 8** (speed 4) meet at **12** and form **one fleet**.
- **Car at 0** (speed 1) does not catch up with any other car, so it forms **a separate fleet**.
- **Car at 5** (speed 1) and **car at 3** (speed 3) meet at **6** and move together as **a fleet**.

### **Example 2**
#### **Input:**
```python
target = 10
position = [3]
speed = [3]
```
#### **Output:**
```python
1
```
#### **Explanation:**
- There is **only one car**, so it forms **one fleet** by itself.

### **Example 3**
#### **Input:**
```python
target = 100
position = [0, 2, 4]
speed = [4, 2, 1]
```
#### **Output:**
```python
1
```
#### **Explanation:**
- The **car at 0** (speed 4) and **car at 2** (speed 2) meet at **4**, forming a **fleet**.
- They continue to **meet car at 5** and eventually form a **single fleet** at the **target**.

## 🛠 **Approach**
We solve this problem using **Sorting & a Stack**:

1. **Sort Cars by Position:**  
   - Since cars closer to the destination **influence those behind them**, we sort the cars based on their starting position **in ascending order**.

2. **Calculate Time to Reach the Target:**  
   - We compute `time = (target - position[i]) / speed[i]` for each car.

3. **Use a Stack to Track Fleets:**  
   - Process each car in **reverse order** (farthest to closest).
   - If a car **takes longer to reach the target than the car ahead**, it **forms a new fleet**.
   - Otherwise, it **joins the fleet ahead**.

**Time Complexity:** **O(N log N)** (due to sorting)  
**Space Complexity:** **O(N)** (for storing times)

## 🚀 **Python Solution**
```python
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Determines the number of car fleets that will arrive at the destination.

        Args:
            target (int): The destination mile.
            position (List[int]): A list of car starting positions.
            speed (List[int]): A list of car speeds.

        Returns:
            int: The number of car fleets that will arrive at the destination.
        """
        # Sort cars by position (ascending order)
        cars = sorted(zip(position, speed))

        # Compute the time each car takes to reach the target
        times = [float(target - p) / s for p, s in cars]

        fleets = 0
        while len(times) > 1:
            lead = times.pop()              # Take the lead car
            if lead < times[-1]:  
                fleets += 1                 # If the lead car arrives earlier, it forms its own fleet
            else:
                times[-1] = lead            # Merge with the slower car behind

        return fleets + bool(times)         # Count the last fleet if there is one
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Sorting cars | `sorted(zip(position, speed))` | **O(N log N)** |
| Compute arrival times | `O(N)` | **O(N)** |
| Process stack for fleets | `O(N)` | **O(N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 📁 **Project Structure**
```
car_fleet/
├── car_fleet.py   # Python solution
├── README.md      # Documentation
```

## 🏆 **Why This Works**
✔ **Sorting ensures we process the rightmost car first** 🏁  
✔ **Using a stack efficiently groups cars into fleets** 🏎️💨  
✔ **Runs in O(N log N), making it optimal for large inputs** 📈  

🚀 **With this solution, you can efficiently determine the number of car fleets reaching the target!** 🎯