# ⚾ **LeetCode 682: Baseball Game**

## 📌 **Overview**
This project solves **LeetCode Problem 682: Baseball Game**. The goal is to compute the **sum of all scores recorded** in a baseball game given a list of operations.

### **Problem Statement**
You are given a list of strings **`operations`**, where each operation modifies the **game record** based on the following rules:

- **An integer `X`** → Record `X` as a new score.
- **`"+"`** → Record the sum of the **previous two scores**.
- **`"D"`** → Record **double** the previous score.
- **`"C"`** → **Invalidate** (remove) the previous score.

👉 **Return the sum of all scores** after applying the operations.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input**
```python
ops = ["5", "2", "C", "D", "+"]
```

#### **Operations Explained**
| Operation | Action | Record After Action |
|-----------|--------|---------------------|
| `"5"`  | Add 5 | `[5]` |
| `"2"`  | Add 2 | `[5, 2]` |
| `"C"`  | Remove last score (2) | `[5]` |
| `"D"`  | Double previous score (5 * 2 = 10) | `[5, 10]` |
| `"+"`  | Add last two scores (5 + 10 = 15) | `[5, 10, 15]` |

#### **Output**
```python
30
```

### **Example 2**
#### **Input**
```python
ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
```

#### **Output**
```python
27
```

## 🛠 **Approach**
### **1️⃣ Use a Stack**
- Maintain a stack to store valid scores.

### **2️⃣ Iterate Through Operations**
- If the operation is:
  - **Integer** → Convert to `int` and push onto the stack.
  - **`"+"`** → Sum the last **two** values and push.
  - **`"D"`** → Double the last value and push.
  - **`"C"`** → Pop the last value.

### **3️⃣ Compute Final Score**
- Return the sum of all valid scores in the stack.

## 🚀 **Implementation**
```python
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        Computes the total score based on a sequence of operations.

        Args:
        - operations (List[str]): A list of operations (e.g., ["5", "D", "C", "+"]).

        Returns:
        - int: The sum of all recorded scores.
        """
        stack = []
        
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))
        
        return sum(stack)
```

## ⏳ **Time Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Process Operations | Iterating through `operations` | **O(N)** |
| Stack Operations | `append()`, `pop()`, and `sum()` | **O(N)** |
| **Total Complexity** | **O(N)** | ✅ Efficient |

## 🏗 **Project Structure**
```
baseball_game/
├── baseball_game.py   # Python solution
├── README.md          # This documentation
```

## 🏆 **Why This Works**
✔ **Uses a stack** to efficiently manage operations.  
✔ **Handles all edge cases**, including empty lists and negative values.  
✔ **O(N) complexity** ensures fast performance.  

**🎯 Now you can efficiently compute scores using Python!** 🚀