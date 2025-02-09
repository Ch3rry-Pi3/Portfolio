# 🌍 **LeetCode 1294: Weather Type in Each Country**

## 📌 **Problem Overview**
Given two tables, **Countries** and **Weather**, determine the **weather type** for each country in **November 2019** based on the **average** weather state.

**Weather Classification Rules:**
- **Cold** → Average `weather_state` **≤ 15**
- **Hot** → Average `weather_state` **≥ 25**
- **Warm** → Otherwise

The result should include the country name and its corresponding **weather type**.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
#### **Countries Table**
| country_id | country_name |
|------------|-------------|
| 1          | USA         |
| 2          | Canada      |
| 3          | Mexico      |

#### **Weather Table**
| country_id | weather_state | day        |
|------------|--------------|------------|
| 1          | 30           | 2019-11-01 |
| 1          | 28           | 2019-11-15 |
| 2          | 10           | 2019-11-10 |
| 2          | 12           | 2019-11-25 |
| 3          | 20           | 2019-11-05 |
| 3          | 26           | 2019-11-20 |

#### **Output:**
| country_name | weather_type |
|--------------|-------------|
| USA         | Hot         |
| Canada      | Cold        |
| Mexico      | Warm        |

#### **Explanation:**
- **USA:** Average weather = `(30 + 28) / 2 = 29` → **Hot**
- **Canada:** Average weather = `(10 + 12) / 2 = 11` → **Cold**
- **Mexico:** Average weather = `(20 + 26) / 2 = 23` → **Warm**

## 🛠 **Approach**
### **1️⃣ Filter Data for November**
- Extract only rows where the **month** in the `day` column is `11` (November).

### **2️⃣ Compute Average Weather Per Country**
- **Group by `country_id`** and compute the **mean** of `weather_state`.

### **3️⃣ Assign Weather Type**
- **Hot** if average `weather_state ≥ 25`
- **Cold** if average `weather_state ≤ 15`
- **Warm** otherwise

### **4️⃣ Merge with Country Names**
- Use `merge()` to join with the **Countries table**.

### **5️⃣ Drop Missing Data**
- Some countries may not have **weather data** for November → **drop them**.

## 🚀 **Python Solution**
```python
import pandas as pd

def weather_type(countries: pd.DataFrame, weather: pd.DataFrame) -> pd.DataFrame:
    """
    Determines the type of weather for each country in November 2019.

    Args:
        countries (pd.DataFrame): DataFrame containing country_id and country_name.
        weather (pd.DataFrame): DataFrame containing country_id, weather_state, and day.

    Returns:
        pd.DataFrame: A DataFrame with country_name and weather_type.
    """

    # Filter for weather data in November
    weather_nov = weather[weather["day"].dt.month == 11]

    # Compute the average weather_state per country
    avg_weather = (
        weather_nov.groupby("country_id", as_index=False)["weather_state"]
        .mean()
        .assign(
            weather_type=lambda df: df["weather_state"].map(
                lambda x: "Hot" if x >= 25 else "Cold" if x <= 15 else "Warm"
            )
        )
    )

    # Merge with countries data to get country names
    result = (
        countries.merge(avg_weather, on="country_id", how="left")
        [["country_name", "weather_type"]]
        .dropna(subset=["weather_type"])  # Remove countries with no weather data
    )

    return result
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Filter for November | `weather["day"].dt.month == 11` | **O(N)** |
| Group & Compute Mean | `groupby().mean()` | **O(N)** |
| Assign Weather Type | `map(lambda x: ...)` | **O(N)** |
| Merge with Country Data | `merge()` | **O(N)** |
| Drop Missing Data | `dropna()` | **O(N)** |
| **Total Complexity** | **O(N) Time, O(1) Space** | ✅ Efficient |

## 📁 **Project Structure**
```
weather_type/
├── weather_type.py   # Python solution
├── README.md         # Documentation
```

## 🏆 **Why This Works**
✔ **Efficient filtering & aggregation** ensures optimal performance.  
✔ **Vectorised operations** make the solution **fast and readable**.  
✔ **Handles missing data gracefully**, avoiding errors.  

🚀 **Now you can efficiently determine the weather type in any country using Pandas!** 🎯