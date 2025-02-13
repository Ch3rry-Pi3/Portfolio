# 🏅 **LeetCode 2377: Olympic Medal Table Sorting**  

## 📌 **Problem Overview**  
In the Olympics, countries are ranked based on the number of medals they win. The ranking follows these rules:  

1. **Gold medals** take the highest priority.  
2. If two countries have the same number of gold medals, the one with more **silver medals** ranks higher.  
3. If there's still a tie, the country with more **bronze medals** ranks higher.  
4. If all medals are equal, the countries are sorted **alphabetically** by their names.  

Given an **Olympic medal table**, our goal is to sort the table based on the above rules.

## 🔍 **Sorting Criteria**
The sorting is performed in **descending order** for medals and **ascending order** for country names:

- **Gold medals** → Descending  
- **Silver medals** → Descending  
- **Bronze medals** → Descending  
- **Country Name** → Ascending (A-Z)  

## 🏆 **Example Walkthrough**  

### **Input:**
```python
olympic_data = {
    "country": ["USA", "China", "Russia", "UK", "Germany"],
    "gold_medals": [39, 38, 22, 20, 17],
    "silver_medals": [41, 32, 21, 21, 20],
    "bronze_medals": [33, 18, 20, 22, 19],
}
```

### **Sorting Logic:**
| Country  | 🥇 Gold | 🥈 Silver | 🥉 Bronze |
|----------|--------|--------|--------|
| USA      | **39** | **41** | **33** |
| China    | **38** | **32** | **18** |
| Russia   | **22** | **21** | **20** |
| UK       | **20** | **21** | **22** |
| Germany  | **17** | **20** | **19** |

- The **USA** has the most gold medals, so it ranks **1st**.
- **China** follows with **38** gold medals.
- **Russia** ranks **3rd** as it has **22** gold medals, more than the UK and Germany.
- **UK** ranks **4th** since it has more **gold medals** than Germany.
- **Germany** is **5th**.

### **Output (Sorted Table):**
```python
    country  gold_medals  silver_medals  bronze_medals
0      USA           39             41             33
1    China           38             32             18
2   Russia           22             21             20
3       UK           20             21             22
4  Germany           17             20             19
```

## 🛠 **Python Solution**
```python
import pandas as pd

def sort_table(olympic: pd.DataFrame) -> pd.DataFrame:
    """
    Sorts the Olympic medal table based on the number of medals won.
    Sorting order:
        - Gold medals (Descending)
        - Silver medals (Descending)
        - Bronze medals (Descending)
        - Country name (Ascending, in case of a tie)

    Args:
        olympic (pd.DataFrame): A DataFrame containing columns "country", "gold_medals",
                                "silver_medals", and "bronze_medals".

    Returns:
        pd.DataFrame: The sorted DataFrame.
    """

    return olympic.sort_values(
        by=["gold_medals", "silver_medals", "bronze_medals", "country"],
        ascending=[False, False, False, True]
    )
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Sorting | `sort_values()` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🎯 **Why This Approach?**
✔ Uses **Pandas sorting** for efficiency.  
✔ Ensures **correct ranking based on Olympic rules**.  
✔ Handles **ties using alphabetical ordering**.  

🚀 **With this approach, we can efficiently rank countries based on their Olympic medal count!** 🏆🔥