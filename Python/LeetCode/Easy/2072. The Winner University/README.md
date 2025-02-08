# 🏆 **LeetCode 2072: The Winner University**  

## 📌 **Overview**  
This project solves **LeetCode Problem 2072: The Winner University**,  
where we **determine which university (New York or California) has more excellent students**.  

### **Problem Statement**  
You are given **two datasets** containing student scores:  
1. **`NewYork` Table** - Scores of students from **New York University**  
2. **`California` Table** - Scores of students from **California University**  

A student is considered **excellent** if their score is **90 or above**.  
The university with the **most excellent students wins**.  

### **Rules:**  
✔ If **New York has more excellent students** → return **"New York University"**  
✔ If **California has more excellent students** → return **"California University"**  
✔ If both have **the same number of excellent students** → return **"No Winner"**  

## 🎯 **Example Walkthrough**  
### **Example Input**  
#### **New York University Scores**
| student_id | score |
|------------|-------|
| 1          | 91    |
| 2          | 80    |
| 3          | 87    |

#### **California University Scores**
| student_id | score |
|------------|-------|
| 1          | 89    |
| 2          | 90    |
| 3          | 88    |

### **Step-by-Step Breakdown**  
1️⃣ **Identify "excellent students" (`score >= 90`)**  
   - **New York:** 1 student (91) ✅  
   - **California:** 1 student (90) ✅  

2️⃣ **Compare the count of excellent students**  
   - Both universities have **1 excellent student each** → **It's a draw** ❌  

3️⃣ **Return "No Winner"**  

### **Expected Output**  
```python
Output:
         winner
0  No Winner
```
🔥 **Now we have determined the winning university (or if it's a draw)!** 🚀  

## 📝 **Step-by-Step Approach**
### **1️⃣ Count Students with Score ≥ 90**
```python
ny_excel = len(new_york[new_york['score'] >= 90])
cal_excel = len(california[california['score'] >= 90])
```
- **Filters students with scores 90+ for each university.**  

### **2️⃣ Determine the Winner**
```python
if ny_excel > cal_excel:
    result = 'New York University'
elif cal_excel > ny_excel:
    result = 'California University'
else:
    result = 'No Winner'
```
- **Compares counts and assigns the appropriate winner.**

### **3️⃣ Return a DataFrame**
```python
return pd.DataFrame({'winner': [result]})
```
- **Returns the result in a proper `DataFrame` format.**

## 💡 **Implementation**
```python
import pandas as pd

def find_winner(new_york: pd.DataFrame, california: pd.DataFrame) -> pd.DataFrame:
    """
    Determines the winning university based on the number of excellent students.

    An excellent student is one who scores 90 or above.
    The university with the most excellent students wins.
    If both universities have the same number of excellent students, it's a draw.

    :param new_york: DataFrame containing New York University student scores.
    :param california: DataFrame containing California University student scores.
    :return: DataFrame with a single column 'winner' indicating the winning university.
    """

    # Count excellent students (score >= 90) in each university
    ny_excel = len(new_york[new_york['score'] >= 90])
    cal_excel = len(california[california['score'] >= 90])

    # Determine the winner based on the count
    if ny_excel > cal_excel:
        result = 'New York University'
    elif cal_excel > ny_excel:
        result = 'California University'
    else:
        result = 'No Winner'  # It's a draw

    # Return the result in a DataFrame format
    return pd.DataFrame({'winner': [result]})

```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Using `.len()` & Filtering (`O(n)`)** | **O(n)** ✅ | **O(1)** ✅ |

- **Each university is processed in linear time (`O(n)`).**  
- **Uses only a few extra variables (`O(1) space complexity`).**  

## 🏗 **Project Structure**
```
2072. The Winner University/
├── the_winner_university.py  # Python implementation of the solution
├── README.md                 # Detailed explanation & walkthrough
```

✨ **Master DataFrame filtering with this efficient `O(n)` approach!** 🚀  