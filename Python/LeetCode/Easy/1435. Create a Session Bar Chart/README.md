# 📊 **LeetCode 1435: Create a Session Bar Chart**

## 📌 **Problem Overview**
You want to analyse how long users stay on your application by categorising session durations into predefined time bins.

Given a table **`Sessions`**, where each row contains a unique session ID and a **duration** (in seconds), your task is to **group the session durations** into the following categories:

- **`[0-5>`** → Duration is **less than 5 minutes** (0 to 299 seconds)
- **`[5-10>`** → Duration is **between 5 and 10 minutes** (300 to 599 seconds)
- **`[10-15>`** → Duration is **between 10 and 15 minutes** (600 to 899 seconds)
- **`15 or more`** → Duration is **15 minutes or more** (900+ seconds)

### **Goal**  
Return a table with two columns:
- **`bin`** → The time category.
- **`total`** → The number of sessions in that category.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
| session_id | duration |
|------------|----------|
| 1          | 30       |
| 2          | 299      |
| 3          | 199      |
| 4          | 580      |
| 5          | 1000     |

#### **Output:**
| bin       | total |
|-----------|-------|
| `[0-5>`   | 3     |
| `[5-10>`  | 1     |
| `[10-15>` | 0     |
| `15 or more` | 1 |

#### **Explanation:**
- **Sessions 1, 2, and 3** lasted **less than 5 minutes**, so they fall into the **`[0-5>`** bin.
- **Session 4** lasted between **5-10 minutes**, so it falls into the **`[5-10>`** bin.
- **No sessions lasted between 10-15 minutes**, so **`[10-15>`** is **0**.
- **Session 5** lasted **more than 15 minutes**, so it goes into the **`15 or more`** bin.

## 🛠 **Approach**
1. **Define Time Bins**  
   - Convert session durations into predefined time bins using **logical conditions**.

2. **Count Sessions in Each Bin**  
   - Use **`query()`** to filter session durations and count occurrences.

3. **Create the Output DataFrame**  
   - Store the bin labels and corresponding counts in a new **DataFrame**.

## 🚀 **Python Solution**
```python
import pandas as pd

def create_bar_chart(sessions: pd.DataFrame) -> pd.DataFrame:
    """
    Categorises user session durations into predefined time bins and counts the number of sessions in each bin.

    Args:
        sessions (pd.DataFrame): A DataFrame containing session durations.

    Returns:
        pd.DataFrame: A DataFrame with session bins and the count of sessions in each bin.
    """
    # Define bins based on duration in seconds
    zero_to_five = len(sessions.query("duration < 300"))
    five_to_ten = len(sessions.query("300 <= duration < 600"))
    ten_to_fifteen = len(sessions.query("600 <= duration < 900"))
    more_than_fifteen = len(sessions.query("duration >= 900"))

    # Construct the result DataFrame
    result = pd.DataFrame({
        "bin": ['[0-5>', '[5-10>', '[10-15>', '15 or more'],
        "total": [zero_to_five, five_to_ten, ten_to_fifteen, more_than_fifteen]
    })

    return result
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Count sessions in each bin | `query()` & `len()` calls | **O(N)** |
| Construct output DataFrame | Creating dictionary & DataFrame | **O(1)** |
| **Total Complexity** | **O(N) time, O(1) space** | ✅ Efficient |

## 📁 **Project Structure**
```
session_bar_chart/
├── session_bar_chart.py   # Python solution
├── README.md              # Documentation
```

## 🏆 **Why This Works**
✔ **Simple and efficient** → Uses **query()** for filtering without extra loops.  
✔ **Handles edge cases** → Works for **empty inputs** and ensures all bins are always present.  
✔ **Scalable** → Works on large datasets efficiently in **O(N) time**.

🚀 **Now you can efficiently categorise session durations with Pandas!** 🎯