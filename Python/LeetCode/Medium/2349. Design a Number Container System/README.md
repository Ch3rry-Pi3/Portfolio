# 📦 **LeetCode 2349: Design a Number Container System**  

## 📌 **Problem Overview**  
Design a **number container system** that allows for the following operations:  

1. **Insert or Replace** a number at a given index in the system.  
2. **Retrieve the smallest index** for a given number.  

You need to implement the **NumberContainers** class:  

- `NumberContainers()`: Initialises the number container system.  
- `void change(int index, int number)`: Fills or updates the number at a specific index.  
- `int find(int number)`: Returns the **smallest index** where the given number is stored or `-1` if not found.  

## 🎯 **Example Walkthrough**  

### **Example 1**  
#### **Input:**
```python
["NumberContainers", "find", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [10], [1, 20], [10]]
```
#### **Output:**
```python
[None, -1, None, None, None, 1, None, 2]
```
#### **Explanation:**  
1. `find(10)`: No index contains `10`, so return **`-1`**.  
2. `change(2, 10)`: Set index **2** to **10**.  
3. `change(1, 10)`: Set index **1** to **10**.  
4. `change(3, 10)`: Set index **3** to **10**.  
5. `find(10)`: The smallest index containing **10** is **1**.  
6. `change(1, 20)`: Replaces **10** at index **1** with **20**.  
7. `find(10)`: The smallest index containing **10** is now **2**.  

## 🛠 **Approach**  

We maintain **two dictionaries**:  

1. **`number_to_indices`**:  
   - Maps **numbers** to a **SortedSet** of indices (ensuring efficient retrieval of the smallest index).  
   
2. **`index_to_number`**:  
   - Maps **indices** to their assigned **numbers**, ensuring efficient lookups when replacing numbers.  

### **Operations Breakdown:**  
- **change(index, number):**  
  1. If the index already contains a number, remove it from its previous entry in `number_to_indices`.  
  2. Update the `index_to_number` dictionary with the new value.  
  3. Insert the index into the new number's **SortedSet** in `number_to_indices`.  

- **find(number):**  
  1. If `number` exists in `number_to_indices`, return the **smallest index**.  
  2. Otherwise, return `-1`.  

## 🚀 **Python Solution**  
```python
from sortedcontainers import SortedSet
import collections

class NumberContainers:
    """
    A number container system that allows inserting/replacing numbers at indices
    and retrieving the smallest index for a given number.
    """

    def __init__(self):
        """Initialises two mappings: one for number-to-indices and another for index-to-number."""
        self.number_to_indices = collections.defaultdict(SortedSet)
        self.index_to_number = {}

    def change(self, index: int, number: int) -> None:
        """
        Inserts or replaces a number at the given index.

        Args:
            index (int): The index where the number is inserted.
            number (int): The number to store at the given index.
        """
        if index in self.index_to_number:
            prev_number = self.index_to_number[index]
            self.number_to_indices[prev_number].remove(index)
            if not self.number_to_indices[prev_number]:
                del self.number_to_indices[prev_number]

        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        """
        Retrieves the smallest index where the given number is stored.

        Args:
            number (int): The number to search for.

        Returns:
            int: The smallest index containing the number, or -1 if not found.
        """
        if number in self.number_to_indices and self.number_to_indices[number]:
            return self.number_to_indices[number][0]
        return -1
```  

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Insert/Replace Number** | `change(index, number)` | **O(log N)** |
| **Find Smallest Index** | `find(number)` | **O(1)** |
| **Overall Complexity** | **O(log N) for change, O(1) for find** | ✅ Efficient |

**Explanation:**  
- **Using `SortedSet`** from `sortedcontainers` ensures that insertion/removal operations run in **O(log N)**.  
- **Retrieval operations (`find`) are O(1)** because we always access the **smallest element** in the set.  

## 📁 **Project Structure**  
```
number_container_system/
├── number_container_system.py   # Python solution
├── README.md                    # Documentation
```

## 🏆 **Why This Works**  
✔ **Efficiently retrieves the smallest index** using `SortedSet`.  
✔ **Optimised for fast updates and lookups** using **hashmaps + sorted sets**.  
✔ **Handles dynamic number changes** without degrading performance.  

🚀 **With this approach, we achieve an efficient number container system that supports fast insertions and queries!** 🎯