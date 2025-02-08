# 🤖 **LeetCode 657: Robot Return to Origin**

## 📌 **Overview**
This project solves **LeetCode Problem 657: Robot Return to Origin**.  
The goal is to determine whether a robot following a sequence of movement instructions **returns to its starting position (0,0).**  

### **Problem Statement**
You are given a **string** `moves`, where:
- `"U"` moves the robot **up** (+1 on y-axis)
- `"D"` moves the robot **down** (-1 on y-axis)
- `"L"` moves the robot **left** (-1 on x-axis)
- `"R"` moves the robot **right** (+1 on x-axis)

👉 **The task:** Return `True` if the robot **ends up back at the origin** after completing all moves, otherwise return `False`.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
moves = "UD"
```
#### **Output:**
```python
True
```
#### **Explanation:**
- `"U"` moves the robot **up** (+1 on y-axis).
- `"D"` moves the robot **down** (-1 on y-axis).
- The robot is back at `(0,0)`, so the function returns `True`.

### **Example 2**
#### **Input:**
```python
moves = "LL"
```
#### **Output:**
```python
False
```
#### **Explanation:**
- `"L"` moves **left** (-1 on x-axis).
- `"L"` moves **left** (-1 on x-axis).
- The robot is now at `(-2,0)`, **not at the origin**, so the function returns `False`.

### **Example 3**
#### **Input:**
```python
moves = "LDRRLRUULR"
```
#### **Output:**
```python
True
```
#### **Explanation:**
- The robot moves in different directions but eventually returns to `(0,0)`.

## 🛠 **Approach**
### **1️⃣ Track Movement on a Coordinate Plane**
- Initialise `(x, y) = (0,0)`, representing the origin.
- Iterate through each move:
  - `"U"` increases `y` by 1.
  - `"D"` decreases `y` by 1.
  - `"L"` decreases `x` by 1.
  - `"R"` increases `x` by 1.
- After processing all moves, check if `(x, y) == (0, 0)`. If so, return `True`; otherwise, return `False`.

## 🚀 **Implementation**
```python
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Determines whether a sequence of moves brings the robot back to the origin (0,0).
        """
        # Initialise coordinates
        x, y = 0, 0

        # Process each move
        for move in moves:
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "R":
                x += 1
            elif move == "L":
                x -= 1

        # The robot returns to origin if (x, y) == (0, 0)
        return x == 0 and y == 0
```

## ⏳ **Time Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Iterating over `moves` | `for move in moves` | **O(N)** |
| Condition checks | `"if move == X"` | **O(1) per move** |
| **Total Complexity** | **O(N)** | ✅ Efficient |

## 🏗 **Project Structure**
```
robot_return/
├── robot_return.py   # Python solution
├── README.md         # This documentation
```

## 🏆 **Why This Works**
✔ **Simple coordinate tracking** with an efficient `O(N)` loop  
✔ **No extra space usage**, only two integer variables (`x, y`)  
✔ **Handles any length of input** gracefully  

**🚀 Now you can track a robot's movements efficiently!** 🎯