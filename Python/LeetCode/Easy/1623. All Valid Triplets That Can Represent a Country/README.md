# **🌍 LeetCode 1623: All Valid Triplets That Can Represent a Country**  

## 📌 **Problem Overview**  
There is a country with three schools: **SchoolA, SchoolB, and SchoolC**. Each student is enrolled in exactly one school. The country is selecting **one student from each school** to form a triplet that represents the country in a competition.  

The valid triplet must satisfy the following conditions:  
✅ **One student** is selected from **each** school.  
✅ **No two students share the same name**.  
✅ **No two students share the same ID**.  

**Goal:** Find all valid triplets of students that satisfy the conditions.  

---
## 🎯 **Example Walkthrough**  

### **Example 1**  
#### **Input:**  
**SchoolA Table:**  
| student_id | student_name |  
|------------|--------------|  
| 1          | Alice        |  
| 2          | Bob         |  

**SchoolB Table:**  
| student_id | student_name |  
|------------|--------------|  
| 3          | Tom         |  

**SchoolC Table:**  
| student_id | student_name |  
|------------|--------------|  
| 3          | Tom         |  
| 2          | Jerry       |  
| 10         | Alice       |  

#### **Output:**  
| member_A | member_B | member_C |  
|----------|----------|----------|  
| Alice    | Tom      | Jerry    |  
| Bob      | Tom      | Alice    |  

#### **Explanation:**  
- Each triplet consists of one student from **each** school.  
- The students in a triplet **must have unique IDs and names**.  
- **Valid Triplets:**  
  - **(Alice, Tom, Jerry)**  
  - **(Bob, Tom, Alice)**  

---
## 🛠 **Approach**  

We solve this problem using **cross join and filtering**:  

1️⃣ **Rename columns** for clarity (`member_A`, `member_B`, `member_C`).  
2️⃣ **Cross join** all three tables to generate all possible triplets.  
3️⃣ **Filter out invalid triplets** by ensuring that:  
   - IDs are unique across the three students.  
   - Names are unique across the three students.  
4️⃣ **Return the valid triplets**.  

---
## 🚀 **Python Solution**  

```python
import pandas as pd

def find_valid_triplets(school_a: pd.DataFrame, school_b: pd.DataFrame, school_c: pd.DataFrame) -> pd.DataFrame:
    """
    Finds all valid student triplets that can represent the country.

    Args:
        school_a (pd.DataFrame): DataFrame containing students from SchoolA.
        school_b (pd.DataFrame): DataFrame containing students from SchoolB.
        school_c (pd.DataFrame): DataFrame containing students from SchoolC.

    Returns:
        pd.DataFrame: A DataFrame containing valid triplets (member_A, member_B, member_C).
    """
    # Rename columns for clarity
    school_a = school_a.rename(columns={"student_id": "id_a", "student_name": "member_A"})
    school_b = school_b.rename(columns={"student_id": "id_b", "student_name": "member_B"})
    school_c = school_c.rename(columns={"student_id": "id_c", "student_name": "member_C"})

    # Perform a cross join to generate all possible triplets
    joined = school_a.merge(school_b, how="cross").merge(school_c, how="cross")

    # Apply filtering to ensure unique IDs and names
    mask = (
        (joined["id_a"] != joined["id_b"]) & (joined["id_a"] != joined["id_c"]) & (joined["id_b"] != joined["id_c"]) &
        (joined["member_A"] != joined["member_B"]) & (joined["member_A"] != joined["member_C"]) & (joined["member_B"] != joined["member_C"])
    )

    return joined.loc[mask, ["member_A", "member_B", "member_C"]]
```

---
## ⏳ **Complexity Analysis**  

| Step | Operation | Complexity |  
|------|------------|------------|  
| Rename Columns | Adjust column names | **O(1)** |  
| Cross Join | Generate all possible triplets | **O(N × M × P)** |  
| Filtering | Remove invalid triplets | **O(N × M × P)** |  
| **Total Complexity** | **O(N × M × P)** |  

---
## 📁 **Project Structure**  
```
valid_triplets/
├── valid_triplets.py   # Python solution
├── README.md           # Documentation
```

---
## 🏆 **Why This Works**  
✔ **Efficiently generates all possible triplets**.  
✔ **Uses filtering to eliminate invalid cases**.  
✔ **Ensures unique student IDs and names in each triplet**.  

---
🚀 **With this solution, we can efficiently generate all valid student triplets that can represent the country in the competition!** 🎯