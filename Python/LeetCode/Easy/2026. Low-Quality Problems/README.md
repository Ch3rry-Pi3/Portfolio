# 🛑 **LeetCode 2073: Low Quality Problems**  

## 📌 **Overview**  
This project solves **LeetCode Problem 2073: Low Quality Problems**,  
where we **identify problems with a low like-to-dislike ratio** based on user feedback.  

### **Problem Statement**  
You are given a dataset containing problems with **likes** and **dislikes** from users.  
We need to **find and return the IDs of problems** where:  

🔹 **Like-to-total vote ratio is below `0.6`**  
🔹 **Sort the results by `problem_id` in ascending order**  

## 🎯 **Example Walkthrough**  
### **Example Input**  
#### **Problems Table**
| problem_id | likes | dislikes |
|------------|-------|----------|
| 1          | 100   | 50       |
| 2          | 50    | 80       |
| 3          | 10    | 100      |
| 4          | 200   | 50       |
| 5          | 80    | 60       |

### **Step-by-Step Breakdown**  
1️⃣ **Compute the like-to-total vote ratio**  
   - **Formula:**  
     \[
     \text{ratio} = \frac{\text{likes}}{\text{likes} + \text{dislikes}}
     \]
   
2️⃣ **Filter out problems where `ratio < 0.6`**  

| problem_id | likes | dislikes | ratio  |
|------------|-------|----------|--------|
| 1          | 100   | 50       | 0.67 ✅ |
| 2          | 50    | 80       | 0.38 ❌ |
| 3          | 10    | 100      | 0.09 ❌ |
| 4          | 200   | 50       | 0.80 ✅ |
| 5          | 80    | 60       | 0.57 ❌ |

3️⃣ **Return the IDs of problems that failed the ratio check (`< 0.6`)**  
   - **Problems 2, 3, and 5** are low quality.  

### **Expected Output**  
```python
Output:
   problem_id
0          2
1          3
2          5
```
🔥 **Now we have identified and filtered low-quality problems!** 🚀  

## 📝 **Step-by-Step Approach**
### **1️⃣ Compute the Like-to-Total Vote Ratio**
```python
problems["ratio"] = problems.apply(
    lambda x: x["likes"] / (x["likes"] + x["dislikes"]), axis=1
)
```
- **Applies the formula across all rows** efficiently.  

### **2️⃣ Filter Problems Where Ratio < 0.6**
```python
problems.query("ratio < 0.6")
```
- **Keeps only low-quality problems.**  

### **3️⃣ Return Sorted `problem_id` Column**
```python
.sort_values(by="problem_id")
```
- **Ensures the results are sorted in ascending order.**

## 💡 **Implementation**
```python
import pandas as pd

def low_quality_problems(problems: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies low-quality problems based on the like-to-dislike ratio.

    A problem is considered low quality if its like-to-total vote ratio is below 0.6.

    :param problems: DataFrame containing 'problem_id', 'likes', and 'dislikes'.
    :return: DataFrame containing only 'problem_id' of low-quality problems, sorted by 'problem_id'.
    """

    # Compute the like-to-total vote ratio
    problems["ratio"] = problems.apply(
        lambda x: x["likes"] / (x["likes"] + x["dislikes"]), axis=1
    )

    # Filter problems with a ratio lower than 0.6 and return sorted 'problem_id'
    return problems.query("ratio < 0.6")[["problem_id"]].sort_values(by="problem_id")
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Using `.apply()` & `.query()` (`O(n)`)** | **O(n)** ✅ | **O(n)** ✅ |

- **Each row is processed once (`O(n) time complexity`).**  
- **Stores results in a new DataFrame (`O(n) space complexity`).**  

## 🏗 **Project Structure**
```
2073. Low Quality Problems/
├── low_quality_problems.py   # Python implementation of the solution
├── README.md                 # Detailed explanation & walkthrough
```

✨ **Master DataFrame filtering with this efficient `O(n)` approach!** 🚀  