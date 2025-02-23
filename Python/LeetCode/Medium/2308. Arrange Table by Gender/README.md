# 📋 **LeetCode 2308: Arrange Table by Gender**  

## 📌 **Problem Overview**  

Given a table containing **user IDs** and their **gender**, rearrange the rows so that they alternate in the following order:  

- **Female** (`female`)
- **Other** (`other`)
- **Male** (`male`)

Additionally, the **user IDs within each gender must be sorted in ascending order**.  

Each gender appears in equal numbers in the dataset, ensuring an equal distribution of **female, other, and male** users.  

## 🔍 **Example 1**  

### **Input: Genders Table**  

| user_id | gender  |
|---------|--------|
| 4       | male   |
| 7       | female |
| 1       | other  |
| 5       | male   |
| 3       | female |
| 6       | other  |
| 9       | female |
| 8       | male   |
| 2       | other  |

### **Output: Arranged Table**  

| user_id | gender  |
|---------|--------|
| 3       | female |
| 1       | other  |
| 4       | male   |
| 7       | female |
| 2       | other  |
| 5       | male   |
| 9       | female |
| 6       | other  |
| 8       | male   |

### **Explanation**  
- **Female IDs:** `3, 7, 9` (Sorted ascending)
- **Other IDs:** `1, 2, 6` (Sorted ascending)
- **Male IDs:** `4, 5, 8` (Sorted ascending)
- The table is rearranged to **alternate** between `female`, `other`, and `male`, while keeping the order within each gender.

## 🚀 **Approach & Intuition**  

### **🔹 Key Idea: Sorting with Rank-based Grouping**  

1. **Rank Users Within Each Gender:**  
   - Assign a **rank (`rn`)** to each user **within their gender**, based on their `user_id` **in ascending order**.  
2. **Map Genders to Sorting Order:**  
   - Assign **numeric values** to genders for ordering:  
     - `female → 1`
     - `other → 2`
     - `male → 3`  
3. **Sort the Table Using Rank First, Then Gender Order:**  
   - This ensures the final order cycles through `female → other → male` while keeping **user IDs ordered within their gender**.

## 📝 **Implementation**  

```python
import pandas as pd

def arrange_table(genders: pd.DataFrame) -> pd.DataFrame:
    """
    Rearranges the Genders table so that rows alternate between 'female', 'other', and 'male',
    with user IDs sorted in ascending order within each gender.

    Args:
        genders (pd.DataFrame): A DataFrame containing:
            - "user_id" (int): The unique ID of the user.
            - "gender" (str): The gender of the user ('female', 'male', 'other').

    Returns:
        pd.DataFrame: A table with:
            - "user_id" (int): The unique user ID.
            - "gender" (str): The gender of the user.

        The table is arranged in a cyclic order of ('female', 'other', 'male') while maintaining 
        ascending order within each gender.
    """

    # Assign a rank within each gender based on user_id's ascending order
    genders['rn'] = genders.groupby('gender')['user_id'].rank(method='first', ascending=True).astype(int)

    # Assign numerical ordering for cyclic sorting: female -> 1, other -> 2, male -> 3
    genders['rn2'] = genders['gender'].map({'female': 1, 'other': 2, 'male': 3})

    # Sort by rank first, then by gender order
    genders = genders.sort_values(by=['rn', 'rn2'])

    return genders[['user_id', 'gender']]
```

## ⏳ **Time Complexity Analysis**  

| **Operation**         | **Complexity**  |
|----------------------|----------------|
| Assign rank per gender  | **O(n)** |
| Map genders to numeric values | **O(n)** |
| Sort table by rank and gender | **O(n log n)** |
| **Overall Complexity** | **O(n log n)** ✅ |

## 🎯 **Key Takeaways**  

✔ **Cyclic Gender Ordering:** Ensures that the table alternates between `female → other → male`.  
✔ **Stable Sorting:** Maintains order within each gender using **ascending user IDs**.  
✔ **Efficient Ranking & Mapping:** Uses **grouping, ranking, and sorting** to achieve the final output in **O(n log n)**.  

🚀 **Mastering sorting problems like this improves your skills in ranking, ordering, and structured data manipulation!** 🔥  
