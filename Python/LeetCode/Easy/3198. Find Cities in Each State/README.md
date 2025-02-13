# 🌎 **LeetCode 3198: Find Cities in Each State**  

## 📌 **Problem Overview**  
Given a dataset of **states and their cities**, we need to **aggregate all cities within each state into a single comma-separated string**.  

✔ **Sorting Rules:**  
   - Cities within each state should be sorted **alphabetically** before aggregation.  
   - The final result should be sorted **by `state` in ascending order**.  

## 🔍 **Example Walkthrough**  

### **Input:**
```python
cities_data = {
    "state": [
        "California", "California", "California",
        "Texas", "Texas", "Texas",
        "New York", "New York", "New York"
    ],
    "city": [
        "Los Angeles", "San Francisco", "San Diego",
        "Houston", "Austin", "Dallas",
        "New York City", "Buffalo", "Rochester"
    ]
}
```

### **Processing Logic:**
| State      | City           |
|------------|---------------|
| **California** | Los Angeles    |
| **California** | San Francisco  |
| **California** | San Diego      |
| **Texas**      | Houston        |
| **Texas**      | Austin         |
| **Texas**      | Dallas         |
| **New York**   | New York City  |
| **New York**   | Buffalo        |
| **New York**   | Rochester      |

1. **Sort cities alphabetically within each state:**  
   - **California** → `"Los Angeles", "San Diego", "San Francisco"`  
   - **Texas** → `"Austin", "Dallas", "Houston"`  
   - **New York** → `"Buffalo", "New York City", "Rochester"`  

2. **Concatenate cities into a single string for each state.**  

### **Final Result:**
| State       | Cities                                      |
|------------|--------------------------------------------|
| **California** | Los Angeles, San Diego, San Francisco  |
| **New York**   | Buffalo, New York City, Rochester      |
| **Texas**      | Austin, Dallas, Houston               |

## 🛠 **Python Solution**
```python
import pandas as pd

def find_cities(cities: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates all cities within each state into a single comma-separated string.

    The result is sorted by:
    - 'state' (ascending)
    - 'city' (ascending) before aggregation.

    Parameters:
    cities (pd.DataFrame): A DataFrame containing city and state information with columns:
                           - 'state' (str): Name of the state.
                           - 'city' (str): Name of the city.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'state' (str): The name of the state.
                  - 'cities' (str): A comma-separated string of city names sorted alphabetically.
                  The result is sorted by 'state' in ascending order.
    """
    # Sort cities first by state and then by city name
    sorted_cities = cities.sort_values(by=["state", "city"])

    # Group by state and concatenate city names into a comma-separated string
    grouped_cities = sorted_cities.groupby("state", as_index=False).agg(cities=("city", ", ".join))

    # Return sorted result by state
    return grouped_cities.sort_values(by="state")
```

## ⏳ **Complexity Analysis**
| Step         | Operation                     | Time Complexity |
|-------------|------------------------------|----------------|
| Sorting Cities | `.sort_values(by=["state", "city"])` | **O(N log N)** |
| Grouping Cities | `.groupby("state").agg()`  | **O(N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

Since sorting dominates, the overall complexity is **O(N log N)**.

---

## 🚀 **How to Use**
### **1️⃣ Installation**
Ensure you have **Python 3.x** and install Pandas if not installed:  
```bash
pip install pandas
```

### **2️⃣ Running the Script**
```bash
python cities_in_states.py
```

### **3️⃣ Sample Output**
```plaintext
        state                        cities
0  California  Los Angeles, San Diego, San Francisco
1    New York  Buffalo, New York City, Rochester
2      Texas          Austin, Dallas, Houston
```

## 🎯 **Why This Approach?**
✔ Uses **Pandas `.sort_values()`** to ensure cities are alphabetically ordered.  
✔ Implements **`.groupby().agg()`** to efficiently concatenate city names.  
✔ Ensures **sorted ordering by `state`** to match problem requirements.  
✔ 🚀 **Optimised for large datasets with `O(N log N)` complexity.**  

🔥 **This method ensures a structured, efficient, and scalable solution for aggregating cities in each state!** 🏙️🌎🚀