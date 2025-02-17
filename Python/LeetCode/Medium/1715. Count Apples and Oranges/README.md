# 🍏 **LeetCode 1715: Count Apples and Oranges**  

## 📌 **Problem Overview**  
You are given two tables, **Boxes** and **Chests**, that store information about the number of apples and oranges contained in storage units.  

Each box may contain:  
- A **chest** (which itself contains apples and oranges).  
- Some number of **apples** and **oranges** directly.  

The goal is to **compute the total number of apples and oranges** across all boxes, ensuring that if a box contains a chest, the fruit count from the chest is also included.  

## 📊 **Database Schema**  

### **Boxes Table**  
| Column Name   | Type  | Description |
|--------------|------|-------------|
| `box_id`     | int  | Unique identifier for the box. |
| `chest_id`   | int  | (Nullable) ID of the chest stored inside the box. |
| `apple_count`  | int  | Number of apples in the box. |
| `orange_count` | int  | Number of oranges in the box. |

### **Chests Table**  
| Column Name   | Type  | Description |
|--------------|------|-------------|
| `chest_id`   | int  | Unique identifier for the chest. |
| `apple_count`  | int  | Number of apples in the chest. |
| `orange_count` | int  | Number of oranges in the chest. |

## 🛠 **Approach**  

1. **Merge the `Boxes` and `Chests` tables** using a **left join** on `chest_id`.  
   - If a box **does not contain a chest**, fill missing values (`NaN`) with **0**.  

2. **Compute total apples and oranges**  
   - Sum the **apples from boxes + apples from chests**.  
   - Sum the **oranges from boxes + oranges from chests**.  

3. **Aggregate the results** to return a **single row** containing the total apple and orange counts.

## 🚀 **Python Solution**  

```python
import pandas as pd

def count_apples_and_oranges(boxes: pd.DataFrame, chests: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the total number of apples and oranges across all boxes, 
    including fruits contained within chests.

    Args:
        boxes (pd.DataFrame): A DataFrame containing details of the boxes with columns:
                              - "box_id" (int): Unique ID for the box.
                              - "chest_id" (int, nullable): ID of the chest inside the box.
                              - "apple_count" (int): Number of apples in the box.
                              - "orange_count" (int): Number of oranges in the box.
        chests (pd.DataFrame): A DataFrame containing details of the chests with columns:
                               - "chest_id" (int): Unique ID for the chest.
                               - "apple_count" (int): Number of apples in the chest.
                               - "orange_count" (int): Number of oranges in the chest.

    Returns:
        pd.DataFrame: A DataFrame with the total count of apples and oranges.
    """
    # Merge boxes with chests to include fruit counts from chests
    merged_df = (
        pd.merge(left=boxes, right=chests, on="chest_id", how="left")
        .fillna(value={"apple_count_y": 0, "orange_count_y": 0})  # Fill NaN with 0 for chests
        .assign(
            apples=lambda x: x["apple_count_x"] + x["apple_count_y"],
            oranges=lambda x: x["orange_count_x"] + x["orange_count_y"]
        )
    )

    # Compute total sum of apples and oranges
    apples = merged_df["apples"].sum()
    oranges = merged_df["oranges"].sum()

    return pd.DataFrame({"apple_count": [apples], "orange_count": [oranges]})

```

## 📌 **Example Walkthrough**  

### **Example Input**  

#### **Boxes Table**  
| box_id | chest_id | apple_count | orange_count |
|--------|---------|-------------|--------------|
| 2      | NULL    | 6           | 15           |
| 18     | 14      | 4           | 15           |
| 3      | 16      | 16          | 7            |
| 12     | 3       | 19          | 20           |
| 20     | 12      | 12          | 9            |
| 8      | 6       | 9           | 9            |

#### **Chests Table**  
| chest_id | apple_count | orange_count |
|----------|-------------|--------------|
| 6        | 5           | 6            |
| 14       | 20          | 10           |
| 12       | 8           | 8            |
| 16       | 19          | 19           |

---

### **Expected Output**  
```python
   apple_count  orange_count
0         151           123
```

### **Explanation**  
- **Box 2** has **6 apples** and **15 oranges**.  
- **Box 18** has **4 apples + 20 from chest = 24 apples**, **15 oranges + 10 from chest = 25 oranges**.  
- **Box 3** has **16 apples + 19 from chest = 36 apples**, **7 oranges + 19 from chest = 17 oranges**.  
- **Box 12** has **19 apples**, **20 oranges**.  
- **Box 20** has **12 apples + 8 from chest = 20 apples**, **9 oranges + 8 from chest = 17 oranges**.  
- **Box 8** has **9 apples + 5 from chest = 14 apples**, **9 oranges + 6 from chest = 15 oranges**.  

Total apples: **151**  
Total oranges: **123**  

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Merge** `boxes` with `chests` | **O(N)** | ✅ Efficient |
| **Fill NaN values** | **O(N)** | ✅ Efficient |
| **Column-wise computation** | **O(N)** | ✅ Efficient |
| **Sum operation** | **O(N)** | ✅ Efficient |
| **Total Complexity** | **O(N)** | ✅ Optimal |

## 🎯 **Why This Approach?**  
✔ **Uses efficient Pandas operations** (`merge`, `fillna`, `sum`).  
✔ **Preserves required order and performs calculations vectorised**.  
✔ **Scales well for large datasets**.  

🚀 **This solution ensures efficient aggregation of apples and oranges across nested containers!** 🍏🍊