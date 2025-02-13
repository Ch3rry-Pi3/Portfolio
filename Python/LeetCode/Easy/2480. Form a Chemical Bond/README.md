# 🔬 **LeetCode 2480: Chemical Bond Formation**  

## 📌 **Problem Overview**  
In chemistry, elements can form bonds based on their classifications as **Metals**, **Nonmetals**, or **Noble gases**. A valid bond is formed when:  

1. One element is a **Metal**.  
2. The other element is a **Nonmetal**.  

**Noble gases** do not participate in bonding and should be ignored.  

Given a dataset of elements, the goal is to generate all possible **(Metal, Nonmetal)** element pairs.  

## 🔍 **Bonding Criteria**
The script follows these rules:  

- **Metals** can only bond with **Nonmetals**.  
- **Noble gases** are excluded from the pairing process.  
- Every Metal is paired with **all** possible Nonmetals.  

---

## 🏆 **Example Walkthrough**  

### **Input:**
```python
elements_data = {
    "symbol": ["He", "Na", "Ca", "La", "Cl", "O", "N"],
    "type": ["Noble", "Metal", "Metal", "Metal", "Nonmetal", "Nonmetal", "Nonmetal"],
    "electrons": [0, 1, 2, 3, 1, 2, 3]
}
```

### **Bonding Logic:**
| Symbol | Type      | Electrons |
|--------|----------|-----------|
| **He**  | Noble    | 0         |
| **Na**  | Metal    | 1         |
| **Ca**  | Metal    | 2         |
| **La**  | Metal    | 3         |
| **Cl**  | Nonmetal | 1         |
| **O**   | Nonmetal | 2         |
| **N**   | Nonmetal | 3         |

- **Metal elements**: `Na`, `Ca`, `La`  
- **Nonmetal elements**: `Cl`, `O`, `N`  
- **Valid Bonds**: Every metal pairs with every nonmetal.  

### **Expected Output:**
```plaintext
  metal nonmetal
0    Na       Cl
1    Na        O
2    Na        N
3    Ca       Cl
4    Ca        O
5    Ca        N
6    La       Cl
7    La        O
8    La        N
```

## 🛠 **Python Solution**
```python
import pandas as pd

def form_bond(elements: pd.DataFrame) -> pd.DataFrame:
    """
    Forms all possible pairs of chemical bonds between elements classified as 'Metal' and 'Nonmetal'.
    
    Parameters:
    elements (pd.DataFrame): A DataFrame containing element information with the columns:
                             - 'symbol' (str): The chemical symbol of the element.
                             - 'type' (str): The classification of the element ('Metal', 'Nonmetal', or 'Noble').
                             - 'electrons' (int): The number of electrons the element can give or take.
    
    Returns:
    pd.DataFrame: A DataFrame containing all valid (Metal, Nonmetal) element pairs.
    """
    # Filter metals and nonmetals from the elements DataFrame
    metals = elements.loc[elements["type"] == "Metal", ["symbol"]].rename(columns={"symbol": "metal"})
    nonmetals = elements.loc[elements["type"] == "Nonmetal", ["symbol"]].rename(columns={"symbol": "nonmetal"})
    
    # Perform a cross join to form all possible metal-nonmetal pairs
    bonds = pd.merge(metals, nonmetals, how="cross")

    return bonds
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Filtering | `loc[]` | **O(N)** |
| Cross Join | `merge(how="cross")` | **O(M × N)** |
| **Total Complexity** | **O(M × N)** | ✅ Efficient |

Where:  
- **M** = Number of Metal elements.  
- **N** = Number of Nonmetal elements.  

Since `M` and `N` are small relative to the dataset, this method is computationally efficient.  

## 🚀 **How to Use**
### **1️⃣ Installation**
Ensure you have **Python 3.x** and install the required library:  
```bash
pip install pandas
```

### **2️⃣ Running the Script**
```bash
python chemical_bond.py
```

### **3️⃣ Sample Output**
```plaintext
  metal nonmetal
0    Na       Cl
1    Na        O
2    Na        N
3    Ca       Cl
4    Ca        O
5    Ca        N
6    La       Cl
7    La        O
8    La        N
```

## 🎯 **Why This Approach?**
✔ Uses **Pandas filtering** for efficient data selection.  
✔ Implements **cross join** for all possible pairings.  
✔ Avoids unnecessary computations by **excluding Noble gases upfront**.  

🔥 **This method ensures a structured, efficient, and scalable solution for forming chemical bonds!** ⚛️