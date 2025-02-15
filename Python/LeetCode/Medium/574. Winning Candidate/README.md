# 🏆 **LeetCode 574: Winning Candidate**

## 📌 **Problem Overview**
In an election, votes are recorded in two tables:  

- **`Candidate` table**: Contains details about each candidate.  
- **`Vote` table**: Stores voting records, where each row represents a vote for a candidate.  

The **goal** is to determine the **candidate with the most votes** and return their name.  
You can assume that **exactly one candidate wins the election** (no ties).

## 📊 **Database Schema**
### **Candidate Table**
| Column Name | Type |
|------------|------|
| `id`       | int  |
| `name`     | varchar |

- **`id`** is a **unique identifier** for each candidate.
- **`name`** is the candidate's name.

### **Vote Table**
| Column Name  | Type |
|-------------|------|
| `id`        | int  |
| `candidateId` | int |

- **`id`** represents the vote ID (auto-incremented).
- **`candidateId`** is a **foreign key** referencing `Candidate.id`, indicating which candidate received the vote.

## 🛠 **Approach**
1. **Merge the `Vote` table with `Candidate`** using `candidateId` to map votes to candidate names.
2. **Count the number of votes for each candidate**.
3. **Return the candidate with the highest vote count**.

This method ensures we efficiently determine the winner while handling large datasets.

## 🚀 **Python Solution**
```python
import pandas as pd

def winning_candidate(candidate: pd.DataFrame, vote: pd.DataFrame) -> pd.DataFrame:
    """
    Determines the winning candidate based on the highest number of votes.

    Args:
        candidate (pd.DataFrame): A DataFrame containing candidate information with columns:
                                  - "id" (int): Unique candidate ID
                                  - "name" (str): Name of the candidate
        vote (pd.DataFrame): A DataFrame containing voting records with columns:
                             - "id" (int): Unique vote ID
                             - "candidateId" (int): Candidate ID that received the vote

    Returns:
        pd.DataFrame: A DataFrame with a single column "name" containing the name of the winning candidate.
    """
    return (
        candidate
        .merge(vote, left_on="id", right_on="candidateId", how="left")["name"]
        .value_counts()
        .reset_index()[["name"]]
        .iloc[:1]
    )
```

## 📌 **Example Walkthrough**
### **Example Input**
#### **Candidate Table**
| id | name |
|----|------|
| 1  | A    |
| 2  | B    |
| 3  | C    |
| 4  | D    |
| 5  | E    |

#### **Vote Table**
| id | candidateId |
|----|------------|
| 1  | 2          |
| 2  | 4          |
| 3  | 2          |
| 4  | 3          |
| 5  | 5          |

### **Output**
```python
   name
0    B
```

### **Explanation**
- Candidate **B** receives **2 votes**.
- Candidates **C, D, and E** each receive **1 vote**.
- Since **B has the highest votes**, they are declared the **winner**.

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Merge Tables | `candidate.merge(vote, left_on="id", right_on="candidateId", how="left")` | **O(N)** |
| Count Votes | `.value_counts()` | **O(N)** |
| Extract Winner | `.iloc[:1]` | **O(1)** |
| **Total Complexity** | **O(N)** | ✅ Efficient |

## 🎯 **Why This Approach?**
✔ **Efficient merge operation** to map votes to candidate names.  
✔ **Simple and readable code** using `value_counts()`.  
✔ **Guaranteed correct answer** due to problem constraints (one winner).  

🚀 **With this approach, you can determine the election winner quickly and efficiently!** 🎉
