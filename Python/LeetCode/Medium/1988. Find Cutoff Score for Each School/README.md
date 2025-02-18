# 🎯 **LeetCode 1988: Find Cutoff Score for Each School**  

## 📌 **Problem Overview**  
Each year, schools announce a **minimum score requirement** for student applications. The goal is to determine the **cutoff score** for each school based on the exam results.

### **Rules for Determining the Cutoff Score**
1. The **minimum score** is chosen **such that every student meeting the requirement** can be accepted.
2. The **maximum possible number of students** should be able to apply.
3. The **cutoff score must exist in the Exam table**.
4. If **no valid score exists**, return `-1` for that school.

## 📊 **Database Schema**  

### **`Schools` Table**  
| Column Name | Type | Description |
|------------|------|-------------|
| `school_id` | int | Unique ID for each school |
| `capacity` | int | Maximum number of students the school can accept |

### **`Exam` Table**  
| Column Name | Type | Description |
|------------|------|-------------|
| `score` | int | Exam score value |
| `student_count` | int | Number of students who scored **at least** this score |

## 🚀 **Solution Approach**  

### **1️⃣ Cross Join Schools with Exam Scores**  
Since every school must choose a cutoff score **from the Exam table**, we use a **cross join** to associate each school with all available exam scores.

### **2️⃣ Filter Out Invalid Scores**  
- A score is **valid** if the **total number of students meeting the requirement** is **≤ the school’s capacity**.
- Scores where **`student_count > capacity`** are **discarded**.

### **3️⃣ Select the Minimum Valid Score for Each School**  
- Among the remaining valid scores, **pick the smallest score**.
- If **no valid score exists**, return `-1`.

## 📝 **Implementation**
```python
import pandas as pd

def find_cutoff_score(schools: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:
    """
    Determines the minimum score required for students to apply to each school.

    Args:
        schools (pd.DataFrame): School information containing:
            - "school_id" (int): Unique school ID.
            - "capacity" (int): Maximum number of students the school can accept.
        exam (pd.DataFrame): Exam results containing:
            - "score" (int): Exam score.
            - "student_count" (int): Number of students who scored at least this score.

    Returns:
        pd.DataFrame: A DataFrame with:
            - "school_id" (int): Unique school ID.
            - "score" (int): Minimum valid cutoff score, or -1 if none exist.
    """

    # Perform a cross join to associate each school with all exam records
    df = schools.merge(exam, how="cross")

    # Filter scores where student count exceeds school capacity
    result = (
        df[df.capacity >= df.student_count]
        .groupby("school_id")["score"]
        .min()
        .reset_index()
        .merge(schools, how="right")
        .fillna(-1)                         # Assign -1 if no valid score exists
    )

    return result[["school_id", "score"]]
```

## 📌 **Example Walkthrough**  

### **Example Input**  

#### **Schools Table**  
| school_id | capacity |
|-----------|---------|
| 1 | 5 |
| 2 | 15 |
| 3 | 20 |

#### **Exam Table**  
| score | student_count |
|-------|--------------|
| 80    | 10          |
| 90    | 5           |
| 85    | 15          |
| 70    | 20          |
| 75    | 25          |

### **Step-by-Step Execution**  
| School ID | Possible Scores | Valid Scores (Capacity Check) | Chosen Cutoff |
|-----------|----------------|------------------------------|---------------|
| **1** | [80, 90, 85, 70, 75] | [90] (Only `≤5` students allowed) | **90** |
| **2** | [80, 90, 85, 70, 75] | [80, 85, 90] (`≤15` students allowed) | **80** |
| **3** | [80, 90, 85, 70, 75] | [70, 80, 85, 90] (`≤20` students allowed) | **70** |

### **Final Output**  
| school_id | score |
|-----------|------|
| 1 | 90 |
| 2 | 80 |
| 3 | 70 |

## ⏳ **Time Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Cross Join** | `schools.merge(exam, how="cross")` | **O(NM)** |
| **Filtering** | `df[df.capacity >= df.student_count]` | **O(NM)** |
| **Grouping & Aggregation** | `groupby("school_id")["score"].min()` | **O(N)** |
| **Final Merge & Cleaning** | `.merge(schools, how="right")` | **O(N)** |
| **Total Complexity** | **O(NM)** | ✅ Efficient |

📌 **`N` is the number of schools, `M` is the number of unique scores in the Exam table.**  

## 🏗 **Project Structure**
```
1988. Find Cutoff Score for Each School/
├── cutoff_score.py      # Python implementation
├── README.md            # Detailed explanation
```

## 🎯 **Key Takeaways**  
✅ Uses **cross join** to associate each school with all possible scores.  
✅ Efficiently filters out scores that exceed capacity.  
✅ **Returns the smallest valid score** to maximise student applications.  
✅ If no valid score exists, returns **`-1`**.  

🚀 **Now you can determine the cutoff scores for any school efficiently!** 🎓