# 🌆 **LeetCode 2987: Find Expensive Cities**  

## 📌 **Problem Overview**  
Given a dataset of **real estate listings**, we need to identify **cities where the average home price exceeds the national average home price**.  

### **Key Concepts:**
1. **Calculate the national average home price**:  
   \[
   \text{national\_average} = \frac{\sum \text{price}}{\text{total listings}}
   \]
2. **Compute the average price per city**:
   \[
   \text{city\_average} = \frac{\sum \text{price in city}}{\text{total listings in city}}
   \]
3. **Filter cities where**:
   \[
   \text{city\_average} > \text{national\_average}
   \]

4. **Sort the output alphabetically by city name**.  

## 🔍 **Example Walkthrough**  

### **Input:**
```python
listings_data = {
    "listing_id": [113, 136, 92, 60, 8, 79, 37, 15, 178, 51],
    "city": ["LosAngeles", "SanFrancisco", "Chicago", "Chicago", "Chicago", 
             "SanFrancisco", "Chicago", "LosAngeles", "SanFrancisco", "NewYork"],
    "price": [7560386, 2380268, 9833299, 5147582, 5274441, 
              8372065, 7395095, 4965123, 999027, 5951718]
}
```

### **Processing Logic:**
| Listing ID | City          | Price     |
|------------|--------------|-----------|
| **113**    | LosAngeles   | 7,560,386 |
| **136**    | SanFrancisco | 2,380,268 |
| **92**     | Chicago      | 9,833,299 |
| **60**     | Chicago      | 5,147,582 |
| **8**      | Chicago      | 5,274,441 |
| **79**     | SanFrancisco | 8,372,065 |
| **37**     | Chicago      | 7,395,095 |
| **15**     | LosAngeles   | 4,965,123 |
| **178**    | SanFrancisco | 999,027   |
| **51**     | NewYork      | 5,951,718 |

1. **Calculate National Average Price:**  
   \[
   \frac{7,560,386 + 2,380,268 + 9,833,299 + 5,147,582 + 5,274,441 + 8,372,065 + 7,395,095 + 4,965,123 + 999,027 + 5,951,718}{10} = 5,687,108.4
   \]

2. **Calculate Average Price per City:**  
   - **Chicago:** \( \frac{9,833,299 + 5,147,582 + 5,274,441 + 7,395,095}{4} = 6,412,354.25 \)  
   - **LosAngeles:** \( \frac{7,560,386 + 4,965,123}{2} = 6,262,754.5 \)  
   - **SanFrancisco:** \( \frac{2,380,268 + 8,372,065 + 999,027}{3} = 3,917,120 \)  
   - **NewYork:** \( 5,951,718 \)  

3. **Filter Cities where City Average > National Average:**  
   - **Chicago**: 6,412,354.25 **✅**
   - **LosAngeles**: 6,262,754.5 **✅**
   - **SanFrancisco**: 3,917,120 ❌
   - **NewYork**: 5,951,718 **✅**

4. **Final Cities Sorted Alphabetically:**  
   - **Chicago**
   - **LosAngeles**

### **Expected Output:**
```plaintext
         city
2    Chicago
3  LosAngeles
```

## 🛠 **Python Solution**
```python
import pandas as pd

def find_expensive_cities(listings: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies cities where the average home price exceeds the national average home price.

    Parameters:
    listings (pd.DataFrame): A DataFrame containing real estate listings with columns:
                             - 'listing_id' (int): Unique identifier for each listing.
                             - 'city' (str): Name of the city.
                             - 'price' (int): Price of the listing.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'city' (str): Cities where the average price exceeds the national average.
                  The result is sorted in ascending order by 'city'.
    """
    # Calculate the national average home price
    national_avg = listings["price"].mean()

    # Compute the average home price per city
    city_avg_prices = listings.groupby("city", as_index=False)["price"].mean()

    # Filter cities with an average price above the national average and sort alphabetically
    expensive_cities = city_avg_prices.loc[city_avg_prices["price"] > national_avg, ["city"]].sort_values(by="city")

    return expensive_cities
```

## ⏳ **Complexity Analysis**
| Step         | Operation                           | Time Complexity |
|-------------|------------------------------------|----------------|
| Mean Calculation | `listings["price"].mean()`   | **O(N)** |
| Grouping    | `.groupby("city")["price"].mean()` | **O(N)** |
| Filtering   | `.loc[]` operation                 | **O(N)** |
| Sorting     | `.sort_values(by="city")`         | **O(N log N)** |
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
python expensive_cities.py
```

### **3️⃣ Sample Output**
```plaintext
         city
2    Chicago
3  LosAngeles
```

## 🎯 **Why This Approach?**
✔ Uses **Pandas `.groupby()`** for efficient data aggregation.  
✔ Computes **city-level and national-level averages efficiently**.  
✔ Implements **sorted ordering by city name** to match requirements.  
✔ 🚀 **Optimised for large datasets with O(N log N) complexity.**  

🔥 **This method ensures a structured, efficient, and scalable solution for identifying expensive cities!** 🏙️💰