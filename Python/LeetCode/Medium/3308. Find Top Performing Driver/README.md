# 🚗 **Find Top Performing Driver**  

## 📌 **Problem Overview**  

Uber is analysing its drivers based on their trips. The objective is to find the **top-performing driver** for each **fuel type** based on the following criteria:  

1. A driver's performance is calculated as the **average rating** across all their trips, rounded to **2 decimal places**.  
2. If two drivers have the same average rating, the driver with the **longer total distance** traveled should be ranked higher.  
3. If there is still a tie, choose the driver with the **fewest accidents**.  

The result table should be **ordered by `fuel_type`** in ascending order.  



## ✅ **Example Input**  

### **Drivers table:**  
| driver_id | name    | age | experience | accidents |
|-||--|--|-|
| 1        | Alice   | 34  | 10        | 3        |
| 2        | Bob     | 45  | 20        | 1        |
| 3        | Charlie | 28  | 5         | 0        |

### **Vehicles table:**  
| vehicle_id | driver_id | model   | fuel_type | mileage |
|--|--|--|-|--|
| 100       | 1         | Sedan  | Gasoline | 20000  |
| 101       | 2         | SUV    | Electric | 30000  |
| 102       | 3         | Coupe  | Gasoline | 15000  |

### **Trips table:**  
| trip_id | vehicle_id | distance | duration | rating |
|--||||-|
| 201    | 100        | 50      | 30      | 5     |
| 202    | 100        | 60      | 40      | 4     |
| 203    | 101        | 30      | 20      | 5     |
| 204    | 102        | 40      | 40      | 5     |
| 205    | 102        | 60      | 40      | 5     |



## ✅ **Example Output**  
| fuel_type | driver_id | rating | distance |
|-|-|-||
| Electric | 2        | 4.50  | 30      |
| Gasoline | 3        | 5.00  | 100     |

### **Explanation:**  
- **Gasoline:**  
  - Alice (Driver 1) has an average rating of **4.5**, while Charlie (Driver 3) has a perfect **5.0**.  
  - Charlie is selected due to the higher rating.  
- **Electric:**  
  - Bob (Driver 2) is the **only driver** and hence selected with a rating of **4.5**.  



## 🛠 **Approach & Intuition**  

### **Step 1:** Data Merging  
Merge the `Trips`, `Vehicles`, and `Drivers` tables based on common columns:  
- Merge `Trips` with `Vehicles` on `vehicle_id`.  
- Merge the result with `Drivers` on `driver_id`.  

### **Step 2:** Data Aggregation  
Group the merged data by `fuel_type`, `driver_id`, and `accidents` to calculate:  
- **Average rating** (rounded to 2 decimal places).  
- **Total distance** traveled.  

### **Step 3:** Sorting and Ranking  
- Sort the grouped data based on:  
  1. `fuel_type` (ascending)  
  2. `avg_rating` (descending)  
  3. `total_distance` (descending)  
  4. `accidents` (ascending)  
- Select the **top performer** for each `fuel_type`.  



## 📝 **Python Implementation**  

```python
import pandas as pd

def get_top_performing_drivers(drivers_df, vehicles_df, trips_df):
    # Merge the dataframes
    merged_df = pd.merge(trips_df, vehicles_df, on='vehicle_id', how='inner')
    merged_df = pd.merge(merged_df, drivers_df, on='driver_id', how='inner')

    # Group by fuel_type, driver_id, and accidents to calculate avg_rating and total_distance
    performance_df = merged_df.groupby(['fuel_type', 'driver_id', 'accidents']).agg(
        avg_rating=('rating', lambda x: round(x.mean(), 2)),
        total_distance=('distance', 'sum')
    ).reset_index()

    # Sort by fuel_type, avg_rating (descending), total_distance (descending), and accidents (ascending)
    performance_df = performance_df.sort_values(
        by=['fuel_type', 'avg_rating', 'total_distance', 'accidents'],
        ascending=[True, False, False, True]
    )

    # Get the top performer for each fuel_type
    top_performers_df = performance_df.groupby('fuel_type').head(1).reset_index(drop=True)

    # Return the result with the required columns
    result_df = top_performers_df[['fuel_type', 'driver_id', 'avg_rating', 'total_distance']]
    result_df.rename(columns={'avg_rating': 'rating', 'total_distance': 'distance'}, inplace=True)
    
    return result_df
```



## 🚀 **Time Complexity Analysis**  
| Operation                  | Complexity |
|||
| Merging DataFrames         | O(n + m + p) |
| Grouping and Aggregation   | O(n log n)   |
| Sorting                    | O(n log n)   |
| Total                      | O(n log n)   |

### **Space Complexity:** O(n)  
- Due to the storage of intermediate DataFrames during merging and grouping.  



## 💡 **Key Takeaways:**  
- Efficiently combined data from multiple tables using **merge**.  
- Utilised **groupby** and **aggregation** to calculate performance metrics.  
- Applied **sorting** based on multiple criteria to get top-performing drivers.  
- Ensured **result formatting** as required.  

🚀 **Mastering DataFrame operations and aggregation is essential for data analysis and reporting!**