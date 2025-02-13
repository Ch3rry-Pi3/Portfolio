# 🏷 **LeetCode 2854: Name and Profession Formatting**  

## 📌 **Problem Overview**  
Given a dataset of individuals, each containing their **person ID, name, and profession**, the task is to **modify the name column** to include the **first letter of the profession in parentheses**. The final output should:  

1. **Append the first letter of each person's profession to their name** (e.g., `"Alice (Engineer)"` → `"Alice(E)"`).  
2. **Sort the table in descending order by `person_id`**.  

## 🔍 **Transformation Criteria**
- The **first letter** of the `profession` column should be extracted, converted to uppercase, and appended to the `name` column.
- The result should **retain only `person_id` and the modified `name` column**.
- Sorting should be done in **descending order** based on `person_id`.  

## 🏆 **Example Walkthrough**  

### **Input:**
```python
person_data = {
    "person_id": [101, 102, 103, 104],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "profession": ["engineer", "doctor", "artist", "scientist"]
}
```

### **Transformation Logic:**
| Person ID | Name    | Profession |
|-----------|---------|------------|
| **101**   | Alice   | Engineer   |
| **102**   | Bob     | Doctor     |
| **103**   | Charlie | Artist     |
| **104**   | David   | Scientist  |

- **Alice** is an **Engineer**, so her name becomes `"Alice(E)"`.  
- **Bob** is a **Doctor**, so his name becomes `"Bob(D)"`.  
- **Charlie** is an **Artist**, so his name becomes `"Charlie(A)"`.  
- **David** is a **Scientist**, so his name becomes `"David(S)"`.  

### **Expected Output:**
```plaintext
   person_id        name
0       104  David(S)
1       103  Charlie(A)
2       102  Bob(D)
3       101  Alice(E)
```

## 🛠 **Python Solution**
```python
import pandas as pd

def concatenate_info(person: pd.DataFrame) -> pd.DataFrame:
    """
    Modifies the 'name' column by appending the first letter of the 'profession' in parentheses.
    Sorts the DataFrame in descending order by 'person_id'.

    Parameters:
    person (pd.DataFrame): A DataFrame containing columns:
                           - 'person_id' (int): Unique ID for each person.
                           - 'name' (str): Person's name.
                           - 'profession' (str): Profession of the person.

    Returns:
    pd.DataFrame: A DataFrame with two columns:
                  - 'person_id': Unique ID (sorted in descending order).
                  - 'name': Modified name in the format "Name(P)" where P is the first letter of 'profession'.
    """
    # Modify the 'name' column to include the first letter of 'profession' in parentheses
    person["name"] = person.apply(lambda x: f"{x['name']}({x['profession'][0].upper()})", axis=1)

    # Return the DataFrame with selected columns, sorted by 'person_id' in descending order
    return person[["person_id", "name"]].sort_values(by="person_id", ascending=False)
```

## ⏳ **Complexity Analysis**
| Step         | Operation                  | Time Complexity |
|-------------|---------------------------|----------------|
| Column Update | `apply()` (Row-wise operation) | **O(N)** |
| Sorting | `sort_values(by='person_id', ascending=False)` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

Since sorting dominates the complexity, the overall complexity is **O(N log N)**.

## 🚀 **How to Use**
### **1️⃣ Installation**
Ensure you have **Python 3.x** and install the required library:  
```bash
pip install pandas
```

### **2️⃣ Running the Script**
```bash
python name_and_profession.py
```

### **3️⃣ Sample Output**
```plaintext
   person_id        name
0       104  David(S)
1       103  Charlie(A)
2       102  Bob(D)
3       101  Alice(E)
```

## 🎯 **Why This Approach?**
✔ Uses **Pandas `apply()`** for efficient transformation.  
✔ Implements **string manipulation** cleanly using `f-strings`.  
✔ Ensures **descending sorting by `person_id`** for proper order.  
✔ 🚀 **Optimised for scalability and clarity**.

🔥 **This approach ensures a structured, efficient, and readable solution for name formatting!** 🏷✨