# 🧠 Integer Memory Optimisation in Pandas 🚀

A Python script that **optimises memory usage** by reducing integer column data types from `int64` to a more memory-efficient type (`int8`). This technique is crucial when working with large datasets, significantly reducing memory consumption.

## 📌 Features
- ✅ **Automatic Integer Type Reduction** – Converts large `int64` columns to a smaller integer type.
- 📊 **Memory Usage Analysis** – Shows memory usage before and after conversion.
- 🔄 **Dynamic Range Checking** – Identifies the minimum and maximum values to select the best type.
- 📉 **Significant Memory Savings** – Reduces unnecessary memory consumption without data loss.

## 🖥️ Demo
🎥 **See it in action!**

```bash
Original memory usage of 'A': 76.29 MB
Minimum value: 1, Maximum value: 99
Memory usage of 'A' after conversion: 9.54 MB
```

## 🚀 How It Works

1️⃣ **Creates a large dataset using NumPy and Pandas** 📜
```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 100, (10**7, 2)), columns=["A", "B"])
```

2️⃣ **Checks and displays initial memory usage** 💾
```python
print(df["A"].memory_usage(deep=True))
```

3️⃣ **Finds the minimum and maximum values** 🔍
```python
print(df["A"].min(), df["A"].max())
```

4️⃣ **Converts `A` column to a more efficient integer type (`int8`)** ⚡
```python
df["A"] = df["A"].astype(np.int8)
```

5️⃣ **Computes memory savings** 📉
```python
print(df["A"].memory_usage(deep=True))
```

## 🏗️ Project Structure
```
📂 Integer Memory Optimisation/
├── app.py                 # Main script
└── README.md              # Project documentation
```

## ⚙️ How to Run

1️⃣ **Install dependencies** 📦
```bash
pip install pandas numpy
```

2️⃣ **Run the script** ▶️
```bash
python app.py
```

## 🌟 Future Enhancements
✅ Automatically determine the best integer type for multiple columns 📊
✅ Expand support for float columns using downcasting ⚡
✅ Add visualisation of memory savings 📉

## 🎉 Enjoy Efficient Data Processing! 🚀