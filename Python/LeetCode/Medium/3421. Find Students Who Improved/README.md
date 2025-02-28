# 🎓 **LeetCode 3421: Find Students Who Improved**  

## 📌 **Problem Overview**  

You are given a dataset that contains student scores for different subjects across multiple exam dates. Your task is to **find students who have shown improvement** in any subject.  

A student is considered to have **improved** if they satisfy both conditions:  
1. They have taken exams in the **same subject** on at least two different dates.  
2. Their **latest score** in that subject is **higher than their first score**.  

🔹 The result must be ordered by **student_id** and **subject** in **ascending order**.  

## 💡 **Example 1**  

### **Input**  

### **Scores Table**  
| student_id | subject  | score | exam_date  |  
|------------|----------|-------|------------|  
| 101        | Math     | 70    | 2023-01-15 |  
| 101        | Math     | 85    | 2023-02-15 |  
| 101        | Physics  | 65    | 2023-01-15 |  
| 101        | Physics  | 60    | 2023-02-15 |  
| 102        | Math     | 80    | 2023-01-15 |  
| 102        | Math     | 85    | 2023-02-15 |  
| 103        | Math     | 90    | 2023-02-15 |  
| 104        | Physics  | 75    | 2023-01-15 |  
| 104        | Physics  | 85    | 2023-02-15 |  

### **Output**  

| student_id | subject  | first_score | latest_score |  
|------------|----------|-------------|--------------|  
| 101        | Math     | 70          | 85           |  
| 102        | Math     | 80          | 85           |  
| 104        | Physics  | 75          | 85           |  

### **Explanation**  

- ✅ **Student 101 (Math):** Improved from **70 → 85** ✅  
- ❌ **Student 101 (Physics):** Score **decreased** from **65 → 60** ❌  
- ✅ **Student 102 (Math):** Improved from **80 → 85** ✅  
- ❌ **Student 103 (Math):** Only one exam, not eligible ❌  
- ✅ **Student 104 (Physics):** Improved from **75 → 85** ✅  

## 🚀 **Approach & Intuition**  

1️⃣ **Sort the Data**  
   - Sort by `student_id`, `subject`, and `exam_date` in ascending order.  
   - This ensures the **earliest and latest** scores are correctly identified.  

2️⃣ **Group by Student and Subject**  
   - Use `groupby()` to **extract the first and last scores** for each student-subject pair.  

3️⃣ **Filter Students Who Showed Improvement**  
   - Retain only the students where **latest_score > first_score**.  

## 📝 **Implementation**  

```python
import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies students who have shown improvement in their scores across multiple exam dates.

    A student is considered to have improved in a subject if:
    1. They have taken exams in the same subject on at least two different dates.
    2. Their latest score in that subject is higher than their first score.

    Parameters:
    scores (pd.DataFrame): A DataFrame containing student scores with the following columns:
        - student_id (int): The ID of the student.
        - subject (str): The subject of the exam.
        - score (int): The score achieved in the exam (0 to 100).
        - exam_date (str): The date of the exam in YYYY-MM-DD format.

    Returns:
    pd.DataFrame: A DataFrame with columns:
        - student_id
        - subject
        - first_score (earliest score in the subject)
        - latest_score (most recent score in the subject)
    """

    # Sort values to ensure correct first and last scores
    scores_sorted = scores.sort_values(by=["student_id", "subject", "exam_date"], ascending=True)

    # Compute first and last score for each student-subject pair
    scores_sorted["first_score"] = scores_sorted.groupby(["student_id", "subject"])["score"].transform("first")
    scores_sorted["latest_score"] = scores_sorted.groupby(["student_id", "subject"])["score"].transform("last")

    # Filter only students who showed improvement
    improved_students = scores_sorted.query("first_score < latest_score")[["student_id", "subject", "first_score", "latest_score"]].drop_duplicates()

    return improved_students
```

## ⏳ **Time Complexity Analysis**  

| Operation                      | Complexity |
|--------------------------------|------------|
| **Sorting DataFrame**          | **O(n log n)** |
| **Grouping and Transformations** | **O(n)** |
| **Filtering Improved Students** | **O(n)** |
| **Overall Complexity**          | **O(n log n)** |

✅ **Optimised for performance**  
✅ **Scalable for large datasets**  

---

## 📂 **Project Structure**  

```
students_who_improved/
├── students_who_improved.py  # Python solution
├── README.md                 # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Efficient use of pandas groupby()** for processing grouped records.  
✔ **Sorting ensures correct first and last exam scores** for each subject.  
✔ **Filters only students who have genuinely improved**.  

🚀 **Great for analysing educational progress tracking!** 📚📊  
