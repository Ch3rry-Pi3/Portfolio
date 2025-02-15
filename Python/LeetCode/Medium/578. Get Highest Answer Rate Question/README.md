# 📊 **LeetCode 578: Get Highest Answer Rate Question**

## 📌 **Problem Overview**
You are given a `SurveyLog` table that tracks users interacting with survey questions. The actions taken by users fall into three categories:  
- **"show"**: The question is displayed to the user.  
- **"answer"**: The user responds to the question.  
- **"skip"**: The user skips the question without answering.  

A question's **answer rate** is calculated as:

\[
\text{Answer Rate} = \frac{\text{Number of "answer" actions}}{\text{Number of "show" actions}}
\]

### **Goal**
Find the **question with the highest answer rate**.  
- If multiple questions have the same **maximum answer rate**, return the one with the **smallest `question_id`**.

## 📊 **Database Schema**
### **SurveyLog Table**
| Column Name  | Type  | Description |
|-------------|------|-------------|
| `id`         | int  | Unique record ID |
| `action`     | ENUM | Action taken by the user (`"show"`, `"answer"`, `"skip"`) |
| `question_id` | int  | Question ID |
| `answer_id`  | int (nullable) | Answer ID if action is `"answer"`, else `NULL` |
| `q_num`      | int  | Order of the question in the session |
| `timestamp`  | int  | Timestamp of the action |

## 🛠 **Approach**
1. **Group by `question_id`** and compute:
   - The **count of "answer" actions**.
   - The **count of "show" actions**.
2. **Calculate the answer rate**:
   - **Answer Rate** = **(Total answers) / (Total shows)**.
3. **Sort by answer rate in descending order**.
4. **Return the `question_id` with the highest answer rate**.
   - If multiple questions have the same highest answer rate, return the **smallest `question_id`**.

## 🚀 **Python Solution**
```python
import pandas as pd

def get_the_question(survey_log: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the question with the highest answer rate.

    Args:
        survey_log (pd.DataFrame): A DataFrame containing survey interaction logs with columns:
                                   - "id" (int): Unique record ID
                                   - "action" (str): "show", "answer", or "skip"
                                   - "question_id" (int): Question ID
                                   - "answer_id" (int, nullable): ID of the answer if action is "answer", else NULL
                                   - "q_num" (int): Order of the question in the session
                                   - "timestamp" (int): Action timestamp

    Returns:
        pd.DataFrame: A DataFrame containing the question ID with the highest answer rate.
    """
    return (
        survey_log
        .groupby("question_id", as_index=False)
        .agg(answer_rate=("action", lambda x: (x == "answer").sum() / (x == "show").sum()))
        .rename(columns={"question_id": "survey_log"})
        .sort_values(by=["answer_rate", "survey_log"], ascending=[False, True])
        .loc[:, ["survey_log"]]
        .head(1)
    )
```

## 📌 **Example Walkthrough**
### **Example Input**
#### **SurveyLog Table**
| id | action | question_id | answer_id | q_num | timestamp |
|----|--------|------------|-----------|-------|-----------|
| 1  | show   | 285        | NULL      | 1     | 124       |
| 2  | answer | 285        | 12424     | 1     | 125       |
| 3  | show   | 369        | NULL      | 1     | 126       |
| 4  | skip   | 369        | NULL      | 1     | 127       |

### **Answer Rate Calculation**
| Question ID | Shows | Answers | Answer Rate |
|-------------|-------|---------|-------------|
| 285         | 1     | 1       | **1.0**     |
| 369         | 1     | 0       | **0.0**     |

### **Output**
```python
   survey_log
0         285
```

### **Explanation**
- **Question 285** has an **answer rate of 1.0 (100%)**.
- **Question 369** has an **answer rate of 0.0 (0%)**.
- Since 285 has the highest answer rate, it is returned.

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Group by `question_id` | `groupby("question_id")` | **O(N)** |
| Compute Answer Rate | `(x == "answer").sum() / (x == "show").sum()` | **O(N)** |
| Sort by Answer Rate | `sort_values(by="answer_rate", ascending=False)` | **O(N log N)** |
| Extract Top Result | `.head(1)` | **O(1)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🎯 **Why This Approach?**
✔ **Uses efficient Pandas operations** (`groupby`, `agg`, `sort_values`).  
✔ **Handles edge cases** (e.g., questions that were shown but never answered).  
✔ **Guaranteed to return exactly one question** due to sorting by `question_id` as a tie-breaker.  

🚀 **With this approach, you can quickly determine the most engaging question in any survey dataset!** 🎯
