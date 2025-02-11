# 📅 **LeetCode 1853: Convert Date Format**

## 📌 **Problem Overview**
We are given a table **Days**, where each row contains a **date** in the format **YYYY-MM-DD**.  
The goal is to **convert** each date into a **string** formatted as:

> **"Day_Name, Month_Name Day, Year"**  

The output should maintain **case sensitivity** (e.g., "Tuesday, April 12, 2022").  

### **Example Format Transformation**
| Input (YYYY-MM-DD) | Output (Formatted Date) |
|--------------------|------------------------|
| 2022-04-12        | Tuesday, April 12, 2022 |
| 2021-08-09        | Monday, August 9, 2021  |
| 2020-06-26        | Friday, June 26, 2020   |

## 🛠 **Approach**
To solve this problem, we will:
1. **Use pandas** to manipulate and format the date values.
2. **Apply the `.dt.strftime()` function** with the format:
   - `%A` → Full **weekday name** (e.g., `"Tuesday"`)
   - `%B` → Full **month name** (e.g., `"April"`)
   - `%-d` → **Day of the month** without leading zero (e.g., `12`, `9`, `26`)
   - `%Y` → Full **year** (e.g., `2022`)
3. **Ensure the formatting preserves case sensitivity.**

🔹 The final output should be **a DataFrame with the formatted date column**.

## 🚀 **Python Solution**
```python
import pandas as pd

def convert_date_format(days: pd.DataFrame) -> pd.DataFrame:
    """
    Converts the date format in the 'day' column to the specified format:
    'Day_Name, Month_Name Day, Year'.

    Args:
        days (pd.DataFrame): DataFrame containing a 'day' column with date values.

    Returns:
        pd.DataFrame: DataFrame with the formatted 'day' column.
    """
    # Convert 'day' column to the desired format
    days["day"] = days["day"].dt.strftime('%A, %B %-d, %Y')
    
    return days
```

## 📌 **Example Walkthrough**
### **Example 1**
#### **Input:**
```python
days = pd.DataFrame({
    "day": pd.to_datetime(["2022-04-12", "2021-08-09", "2020-06-26"])
})
```
#### **Output:**
```python
                      day
0  Tuesday, April 12, 2022
1   Monday, August 9, 2021
2   Friday, June 26, 2020
```
#### **Explanation:**
Each date is transformed into the correct **case-sensitive** format.

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Convert date format | `.dt.strftime()` | **O(n)** |
| **Total Complexity** | **O(n), Space: O(n)** | ✅ Efficient |

## 🎯 **Why This Approach?**
✔ **Uses pandas for efficient date formatting**  
✔ **Ensures correct case sensitivity**  
✔ **Handles multiple rows efficiently (O(n))**  

🚀 **With this approach, you can easily transform date formats in a structured dataset!** 🎯

Let me know if you'd like any modifications! 🚀😊