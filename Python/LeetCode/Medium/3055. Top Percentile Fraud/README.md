# 🏛 **LeetCode 3055: Top Percentile Fraud**  

## 📌 **Problem Overview**  
A predictive **fraud detection model** has flagged insurance claims with a **fraud score**. To efficiently allocate fraud investigators, we need to **identify the top 5% of fraudulent claims** for each state.

### **Table Schema**  
- **Fraud Table**
  - `policy_id` (**int**) → The unique ID of the insurance policy.
  - `state` (**varchar**) → The state in which the policy is registered.
  - `fraud_score` (**float**) → The likelihood of fraud, with higher values indicating a greater risk.

### **Goal**  
- Identify **the top 5% of claims** within each state, based on `fraud_score`.
- If multiple claims have the same fraud score within the **top 5%**, they are all included.
- Return results **sorted by**:
  1. **`state` (ascending)**
  2. **`fraud_score` (descending)**
  3. **`policy_id` (ascending)**

## 🖼 **Example**  
### **Input: Fraud Table**
```
+-----------+------------+-------------+
| policy_id |   state    | fraud_score |
+-----------+------------+-------------+
|     1     | California |     0.92    |
|     2     | California |     0.68    |
|     3     | California |     0.17    |
|     4     | New York   |     0.94    |
|     5     | New York   |     0.81    |
|     6     | New York   |     0.77    |
|     7     | Texas      |     0.98    |
|     8     | Texas      |     0.95    |
|     9     | Texas      |     0.97    |
|    10     | Florida    |     0.98    |
|    11     | Florida    |     0.78    |
|    12     | Florida    |     0.94    |
|    13     | Florida    |     0.88    |
|    14     | Florida    |     0.66    |
+-----------+------------+-------------+
```

### **Output:**
```
+-----------+------------+-------------+
| policy_id |   state    | fraud_score |
+-----------+------------+-------------+
|     1     | California |     0.92    |
|    10     | Florida    |     0.98    |
|     4     | New York   |     0.94    |
|     7     | Texas      |     0.98    |
+-----------+------------+-------------+
```

✅ **Explanation:**  
- **California:** Only `policy_id = 1` is in the top 5% (`fraud_score = 0.92`).
- **Florida:** Only `policy_id = 10` is in the top 5% (`fraud_score = 0.98`).
- **New York:** Only `policy_id = 4` is in the top 5% (`fraud_score = 0.94`).
- **Texas:** Only `policy_id = 7` is in the top 5% (`fraud_score = 0.98`).

The output is **sorted by state, fraud_score (descending), and policy_id (ascending).**

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Percentile Ranking by State**
1. **Calculate the percentile rank** of each `fraud_score` within its respective `state`.
2. **Filter for scores in the top 5% (`≥ 0.95` percentile).**
3. **Sort results by:**
   - `state` **(ascending)**
   - `fraud_score` **(descending)**
   - `policy_id` **(ascending)**

## 📝 **Implementation**  

```python
# top_percentile_fraud.py

import pandas as pd

def top_percentile_fraud(fraud: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies the top 5% of fraudulent claims per state based on fraud scores.

    Args:
        fraud (pd.DataFrame): Contains claim data with columns:
            - "policy_id" (int): The unique ID of the insurance policy.
            - "state" (str): The state in which the policy is registered.
            - "fraud_score" (float): The fraud likelihood score.

    Returns:
        pd.DataFrame: A table containing:
            - "policy_id" (int): The ID of the policy flagged as fraudulent.
            - "state" (str): The state associated with the policy.
            - "fraud_score" (float): The fraud score of the policy.
        
        The result is filtered to only include the top 5% of fraudulent claims in each state.
        The table is sorted by:
            1. "state" (ascending order),
            2. "fraud_score" (descending order),
            3. "policy_id" (ascending order).
    """
    return (
        fraud
        # Compute the percentile rank for fraud scores within each state
        .assign(percentile=lambda x: x.groupby("state")["fraud_score"].rank(method="dense", pct=True))
        # Filter for the top 5% fraudulent claims
        .query("percentile >= 0.95")
        # Drop the percentile column since it's no longer needed
        .drop(columns="percentile")
        # Sort by state (asc), fraud_score (desc), policy_id (asc)
        .sort_values(["state", "fraud_score", "policy_id"], ascending=[True, False, True])
    )
```

## ⏳ **Time Complexity Analysis**  

| Operation                                  | Complexity |
|--------------------------------------------|------------|
| Calculating percentile ranks per state     | **O(N log N)** (grouping & ranking) |
| Filtering for top 5%                       | **O(N)** |
| Sorting results                            | **O(N log N)** |
| **Overall Complexity**                      | **O(N log N)** ✅ |

> **N = number of claims in the dataset**  

## 📂 **Project Structure**  

```
3055. Top Percentile Fraud/
├── top_percentile_fraud.py  # Python solution
├── README.md                # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses `rank(pct=True)` to compute percentile rankings** efficiently.  
✔ **Filters only the top 5% of claims per state** for focused fraud detection.  
✔ **Sorting ensures results follow required output format.**  

🚀 **Mastering percentile ranking techniques is key for fraud detection and risk analysis!** 🔥