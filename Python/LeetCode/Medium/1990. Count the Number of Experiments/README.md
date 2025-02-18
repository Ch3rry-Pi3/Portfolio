# 🔬 **LeetCode 1990: Count the Number of Experiments**  

## 📌 **Problem Overview**  
You are given a table `Experiments` that records experiments conducted on different platforms. The goal is to count the number of experiments conducted for each **platform** and **experiment type**, ensuring that all possible (platform, experiment) pairs are included in the output, even if no experiments were conducted.  

### **Problem Constraints**  
Each row in the table contains:  
- The **platform** used (`'Android'`, `'IOS'`, `'Web'`).
- The **experiment name** (`'Reading'`, `'Sports'`, `'Programming'`).
- A unique `experiment_id` for each experiment.

## 🎯 **Goal**  
Return a table containing:  
- Each possible **(platform, experiment_name)** pair.  
- The **number of experiments** conducted for each pair (`num_experiments`).  
- If no experiments exist for a given pair, return **0**.  

## 📝 **Example Walkthrough**  

### **Example Input**  

#### **Experiments Table**  
| experiment_id | platform | experiment_name  |
|--------------|---------|------------------|
| 4            | IOS     | Programming      |
| 13           | IOS     | Sports           |
| 9            | Android | Reading          |
| 12           | Web     | Reading          |
| 18           | Web     | Programming      |

### **Expected Output**  
| platform  | experiment_name | num_experiments |
|-----------|----------------|-----------------|
| Android   | Reading        | 1               |
| Android   | Sports         | 0               |
| Android   | Programming    | 0               |
| IOS       | Reading        | 0               |
| IOS       | Sports         | 1               |
| IOS       | Programming    | 1               |
| Web       | Reading        | 1               |
| Web       | Sports         | 0               |
| Web       | Programming    | 1               |

### **Explanation**  
- **Android** has **1** "Reading" experiment but **0** for "Sports" and "Programming".  
- **IOS** has **1** "Sports" and **1** "Programming" experiment but **0** for "Reading".  
- **Web** has **1** "Reading" and **1** "Programming" experiment but **0** for "Sports".  
- All **(platform, experiment_name)** combinations are included, even if the count is **0**.  

## 💡 **Approach**  

### **1️⃣ Generate All Possible Platform-Experiment Pairs**  
- Define a DataFrame for **all platforms** (`'Android'`, `'IOS'`, `'Web'`).  
- Define another DataFrame for **all experiment types** (`'Reading'`, `'Sports'`, `'Programming'`).  
- Use **cross join** (`merge(how='cross')`) to create a **complete set** of all possible `(platform, experiment_name)` pairs.

### **2️⃣ Count Existing Experiments**  
- Group the given `experiments` table by `(platform, experiment_name)`.  
- Count occurrences of each **(platform, experiment_name)** pair.  

### **3️⃣ Merge with All Possible Pairs**  
- Merge the counted experiments with the **full set of possible pairs**.  
- Fill missing values (`NaN`) with `0` to account for missing experiment counts.

## 🚀 **Python Solution**  

```python
import pandas as pd

def count_experiments(experiments: pd.DataFrame) -> pd.DataFrame:
    """
    Counts the number of experiments conducted on each platform for each experiment type.
    Ensures that all (platform, experiment_name) pairs are included, even if no experiments exist.

    Args:
        experiments (pd.DataFrame): A DataFrame containing experiment details with columns:
                                    - "experiment_id" (int): Unique ID of the experiment.
                                    - "platform" (str): Platform used ('Android', 'IOS', 'Web').
                                    - "experiment_name" (str): Experiment type ('Reading', 'Sports', 'Programming').

    Returns:
        pd.DataFrame: A DataFrame with columns:
                      - "platform" (str): The platform name.
                      - "experiment_name" (str): The experiment type.
                      - "num_experiments" (int): The count of experiments for each platform-experiment pair.
    """

    # Define all possible platform and experiment name combinations
    platforms = pd.DataFrame({'platform': ['Android', 'IOS', 'Web']})
    experiment_names = pd.DataFrame({'experiment_name': ['Reading', 'Sports', 'Programming']})

    # Create a complete cross-product of platforms and experiment names
    all_combinations = platforms.merge(experiment_names, how='cross')

    # Group by platform and experiment name, counting occurrences
    experiment_counts = (
        experiments
        .groupby(['platform', 'experiment_name'])
        .size()
        .reset_index(name='num_experiments')
    )

    # Merge with all possible combinations to ensure missing values are included
    result = all_combinations.merge(experiment_counts, on=['platform', 'experiment_name'], how='left').fillna(0)

    return result
```

## ⏳ **Time Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Cross Join for All Pairs** | `merge(how='cross')` | **O(1)** (fixed size 3x3) |
| **Group Experiments by Platform & Name** | `groupby(['platform', 'experiment_name'])` | **O(N)** |
| **Merge Results** | `merge(how='left')` | **O(N)** |
| **Fill Missing Values** | `.fillna(0)` | **O(N)** |
| **Total Complexity** | **O(N)** ✅ **Efficient** |

- Since there are only **3 platforms** and **3 experiment types**, the **cross join is constant time**.
- The overall complexity **scales linearly with the number of experiments (`O(N)`)**, making it efficient.

## 🏗 **Project Structure**  

```
LeetCode_1990_Count_Experiments/
├── number_of_experiments.py    # Python implementation of the solution
├── README.md                   # Detailed problem explanation & approach
```

## 🎯 **Key Takeaways**  
✔ **Ensures all (platform, experiment_name) pairs are represented, even if count = 0**  
✔ **Uses Pandas `groupby`, `merge`, and `fillna` efficiently**  
✔ **Linear time complexity `O(N)`, scales well with large datasets**  

🚀 **This approach ensures that all experiments are counted correctly, even if a category is missing!** 🎯  
