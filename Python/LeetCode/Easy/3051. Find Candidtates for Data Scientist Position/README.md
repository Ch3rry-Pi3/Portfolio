# 🏆 **LeetCode 3051: Find Candidates for Data Scientist Position**  

## 📌 **Problem Overview**  
Given a dataset of **candidates and their skills**, we need to **identify candidates** who are best suited for a **Data Scientist position**.  

✔ The candidate must have **all three required skills**:  
   - **Python**  
   - **Tableau**  
   - **PostgreSQL**  

The output should contain only the **`candidate_id`** of these qualified candidates, sorted in **ascending order**.  

## 🔍 **Example Walkthrough**  

### **Input:**
```python
candidates_data = {
    "candidate_id": [123, 123, 123, 234, 234, 234, 234, 234, 147, 147, 147, 256, 102],
    "skill": ["Python", "R", "Tableau", "PostgreSQL", "PowerBI", "SQL Server", "Python", "Tableau",
              "Java", "PostgreSQL", "Python", "Tableau", "DataAnalysis"]
}
```

### **Processing Logic:**
| Candidate ID | Skill       |
|-------------|------------|
| **123**     | Python     |
| **123**     | R          |
| **123**     | Tableau    |
| **234**     | PostgreSQL |
| **234**     | PowerBI    |
| **234**     | SQL Server |
| **234**     | Python     |
| **234**     | Tableau    |
| **147**     | Java       |
| **147**     | PostgreSQL |
| **147**     | Python     |
| **256**     | Tableau    |
| **102**     | DataAnalysis |

1. **Filter Candidates Who Have at Least One of the Required Skills**  
   - ✅ **Keep**: Python, Tableau, PostgreSQL  
   - ❌ **Ignore**: Other skills (e.g., Java, R, SQL Server)  

2. **Count the Number of Required Skills Per Candidate**  
   - Candidate **123** → **3 skills** ✅  
   - Candidate **234** → **2 skills** ❌  
   - Candidate **147** → **3 skills** ✅  
   - Candidate **256** → **1 skill** ❌  
   - Candidate **102** → **0 skills** ❌  

3. **Filter Candidates Who Have All Three Skills (`Python`, `Tableau`, `PostgreSQL`)**  
   - Qualified Candidates: **123, 147**  

4. **Sort by `candidate_id` in Ascending Order**  
   - **Final Result:** `[123, 147]`

### **Expected Output:**
```plaintext
   candidate_id
0          123
1          147
```

## 🛠 **Python Solution**
```python
import pandas as pd

def find_candidates(candidates: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies candidates best suited for a Data Scientist position. 
    A candidate must be proficient in 'Python', 'Tableau', and 'PostgreSQL'.

    Parameters:
    candidates (pd.DataFrame): A DataFrame containing candidate skill information with columns:
                               - 'candidate_id' (int): Unique identifier for each candidate.
                               - 'skill' (str): Name of the skill.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'candidate_id' (int): Candidates who have all three required skills.
                  The result is sorted in ascending order by 'candidate_id'.
    """
    # Filter candidates who have at least one of the required skills
    filtered_candidates = candidates[candidates["skill"].isin(["Python", "Tableau", "PostgreSQL"])]

    # Count the number of required skills each candidate has
    skill_counts = filtered_candidates.groupby("candidate_id")["skill"].nunique().reset_index()

    # Select candidates who have all three required skills
    qualified_candidates = skill_counts[skill_counts["skill"] == 3][["candidate_id"]].sort_values(by="candidate_id")

    return qualified_candidates
```

## ⏳ **Complexity Analysis**
| Step         | Operation                     | Time Complexity |
|-------------|------------------------------|----------------|
| Filtering   | `.isin(["Python", "Tableau", "PostgreSQL"])` | **O(N)** |
| Grouping    | `.groupby("candidate_id")["skill"].nunique()` | **O(N)** |
| Filtering   | `.loc[skill_counts["skill"] == 3]` | **O(N)** |
| Sorting     | `.sort_values(by="candidate_id")` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

Since sorting dominates, the overall complexity is **O(N log N)**.

## 🚀 **How to Use**
### **1️⃣ Installation**
Ensure you have **Python 3.x** and install Pandas if not installed:  
```bash
pip install pandas
```

### **2️⃣ Running the Script**
```bash
python datascientist_candidates.py
```

### **3️⃣ Sample Output**
```plaintext
   candidate_id
0          123
1          147
```

## 🎯 **Why This Approach?**
✔ Uses **Pandas filtering (`.isin()`)** for efficient skill selection.  
✔ Implements **grouping and `.nunique()`** to ensure unique skill counts.  
✔ Ensures **sorted ordering by `candidate_id`** to match problem requirements.  
✔ 🚀 **Optimised for large datasets with `O(N log N)` complexity.**  

🔥 **This method ensures a structured, efficient, and scalable solution for identifying top candidates for a Data Scientist position!** 📊🚀