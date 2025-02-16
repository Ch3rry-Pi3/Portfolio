# 🧠 Memory Optimisation in Pandas 🚀

A Python script that **optimises memory usage** by converting object columns to categorical data types in Pandas DataFrames. This process significantly reduces memory consumption without affecting data integrity.

## 📌 Features
- ✅ **Efficient Memory Usage** – Converts object columns to categorical types to save memory.
- 📊 **Data Type Analysis** – Identifies original and transformed data types.
- 🔄 **Dynamic Memory Calculation** – Computes memory before and after conversion.
- 📉 **Percentage Reduction Calculation** – Shows the exact memory savings achieved.

## 🖥️ Demo
🎥 **See it in action!**

```bash
First 5 rows of the dataset:
   PassengerId  Survived  Pclass  ...
0           1         0       3  ...
1           2         1       1  ...
2           3         1       3  ...

Original data type of 'Gender': object
Memory usage of 'Gender' column before conversion: 78.82 KB
Memory usage of 'Gender' column after conversion: 1.80 KB
Percentage decrease in memory usage: 97.71%
```

## 🚀 How It Works

1️⃣ **Loads a dataset using Pandas** 📜
```python
import pandas as pd
df = pd.read_csv("data/titanic_train.csv")
```

2️⃣ **Checks and displays memory usage of an object column** 💾
```python
mem_before = df["Gender"].memory_usage(deep=True)
```

3️⃣ **Converts object type to categorical** ⚡
```python
df["Gender"] = df["Gender"].astype("category")
```

4️⃣ **Calculates memory savings** 📉
```python
mem_after = df["Gender"].memory_usage(deep=True)
mem_decrease = ((mem_before - mem_after) / mem_before) * 100
```

## 🏗️ Project Structure
```
📂 Memory Optimisation/
├── app.py                 # Main script
├── data/                  # Dataset folder
│   ├── titanic_train.csv  # Example dataset
└── README.md              # Project documentation
```

## ⚙️ How to Run

1️⃣ **Install dependencies** 📦
```bash
pip install pandas
```

2️⃣ **Run the script** ▶️
```bash
python app.py
```

## 🌟 Future Enhancements
✅ Extend to multiple object columns automatically 📊
✅ Apply categorical conversion selectively for optimal performance ⚡
✅ Add visualisation of memory savings 📉

## 🎉 Enjoy Optimising Your Data! 🚀

