# 🏔️ **LeetCode 1732: Find the Highest Altitude**

## 📌 **Problem Overview**
A biker is going on a road trip. The trip consists of **n + 1** points at different altitudes. The biker starts at **altitude 0** and follows a series of **altitude gains** at each step.

### **Goal:**  
Given an integer array **gain**, where **gain[i]** represents the **net altitude change** between points **i** and **i + 1**, return the **highest altitude** reached.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
gain = [-5, 1, 5, 0, -7]
```
#### **Output:**
```python
1
```
#### **Explanation:**
- Starting altitude = **0**.
- The altitudes after each step: **[0, -5, -4, 1, 1, -6]**.
- The highest altitude reached = **1**.

### **Example 2**
#### **Input:**
```python
gain = [-4, -3, -2, -1, 4, 3, 2]
```
#### **Output:**
```python
0
```
#### **Explanation:**
- The altitudes after each step: **[0, -4, -7, -9, -10, -6, -3, -1]**.
- The highest altitude reached = **0**.

## 🛠 **Approach**
This problem can be solved efficiently with a **single pass** through the `gain` array.

### **1️⃣ Initialise Variables**
- `current_altitude = 0`: The starting altitude.
- `highest_point = 0`: The highest altitude reached so far.

### **2️⃣ Iterate Through Gains**
- Update `current_altitude` at each step by adding the altitude change.
- Update `highest_point` if `current_altitude` exceeds it.

### **3️⃣ Return the Maximum Altitude**
- The final `highest_point` is the answer.

✅ **Time Complexity:** **O(N)** – We iterate through `gain` once.  
✅ **Space Complexity:** **O(1)** – We use only a few integer variables.

## 🚀 **Python Solution**
```python
from typing import List

def largest_altitude(gain: List[int]) -> int:
    """
    Computes the highest altitude reached during a road trip based on 
    altitude gains at each step.

    Args:
        gain (List[int]): A list representing the net altitude gain 
                          at each step of the journey.

    Returns:
        int: The highest altitude reached during the trip.
    """
    current_altitude = 0                                            # Starting altitude at point 0
    highest_point = 0                                               # Initially, the highest altitude is 0

    # Iterate through the altitude gains
    for altitude_gain in gain:
        current_altitude += altitude_gain                           # Update the altitude
        highest_point = max(highest_point, current_altitude)        # Track the highest point

    return highest_point
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Iterate through `gain` | `for altitude_gain in gain` | **O(N)** |
| Update `current_altitude` | Constant time per step | **O(1)** |
| Track `highest_point` | Constant time per step | **O(1)** |
| **Total Complexity** | **O(N) Time, O(1) Space** | ✅ Efficient |

## 📁 **Project Structure**
```
highest_altitude/
├── highest_altitude.py   # Python solution
├── README.md             # Documentation
```

## 🏆 **Why This Works**
✔ **Uses a single pass approach** for efficiency.  
✔ **Constant space complexity (O(1))** makes it scalable.  
✔ **Handles all edge cases**, including negative and zero altitude gains.  

🚀 **With this approach, we efficiently compute the highest altitude reached during the trip!** 🎯