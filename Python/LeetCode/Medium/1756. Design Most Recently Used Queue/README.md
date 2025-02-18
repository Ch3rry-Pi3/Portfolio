Here is your **beautifully formatted** `README.md` for **LeetCode 1756: Design Most Recently Used Queue**:

---

# 🔄 **LeetCode 1756: Design Most Recently Used Queue**  

## 📌 **Problem Overview**  
You need to design a **queue-like data structure** that **moves the most recently used (MRU) element** to the end of the queue when accessed.  

### **Implementation Requirements**  
You must implement the following:  

1. **MRUQueue(int n)**  
   - Initialises a queue with elements `[1, 2, ..., n]` (1-based indexing).  
   
2. **int fetch(int k)**  
   - Fetches the `k`-th (1-indexed) element from the queue.  
   - Moves it to the **end of the queue**.  
   - Returns the fetched element.  

## 🚀 **Example Walkthrough**  

### **Example Input**  
```python
["MRUQueue", "fetch", "fetch", "fetch", "fetch"]
[[8], [3], [5], [2], [8]]
```

### **Example Output**  
```python
[null, 3, 6, 2, 2]
```

### **Step-by-Step Execution**  
| Step | Operation | Queue State | Returned Value |
|------|------------|-------------|---------------|
| 1️⃣ | Initialise `MRUQueue(8)` | `[1, 2, 3, 4, 5, 6, 7, 8]` | `null` |
| 2️⃣ | `fetch(3)` → Move 3 to the end | `[1, 2, 4, 5, 6, 7, 8, 3]` | `3` |
| 3️⃣ | `fetch(5)` → Move 6 to the end | `[1, 2, 4, 5, 7, 8, 3, 6]` | `6` |
| 4️⃣ | `fetch(2)` → Move 2 to the end | `[1, 4, 5, 7, 8, 3, 6, 2]` | `2` |
| 5️⃣ | `fetch(8)` → 2 is already last | `[1, 4, 5, 7, 8, 3, 6, 2]` | `2` |

## 🧠 **Approach & Intuition**  
- We maintain a **list-based queue** (`self.queue`) initialised with elements `[1, 2, ..., n]`.  
- When we **fetch** an element:
  - Remove it from its current position using `pop(k - 1)`.  
  - Append it to the **end** of the queue using `append(value)`.  
- The `fetch()` operation runs in **O(n) time complexity**, as removing an element from a list takes **O(n)** in the worst case.

## 🔥 **Optimised Approach Using Deques (Alternative Solution)**  
A more optimised approach would involve using a **deque (double-ended queue)** from `collections.deque`, allowing for **O(1) removals** and **O(1) insertions** instead of the O(n) removals in lists.  

---

## 📝 **Python Implementation**  

```python
class MRUQueue:
    """
    A queue-like data structure that moves the most recently used element 
    to the end of the queue when accessed.

    Methods:
    - __init__(n): Initialises the queue with elements [1, 2, ..., n].
    - fetch(k): Moves the k-th (1-indexed) element to the end of the queue and returns it.
    """

    def __init__(self, n: int):
        """
        Initialises the MRUQueue with n elements [1, 2, ..., n].

        :param n: Number of elements in the queue.
        """
        self.queue = list(range(1, n + 1))

    def fetch(self, k: int) -> int:
        """
        Fetches the k-th element (1-indexed), moves it to the end of the queue, and returns it.

        :param k: The position (1-based index) of the element to fetch.
        :return: The fetched element.
        """
        value = self.queue.pop(k - 1)       # Remove the k-th element (adjusting for 0-indexing)
        self.queue.append(value)            # Move it to the end of the queue
        return value
```

---

## ⏳ **Time Complexity Analysis**  
| Operation | Time Complexity |
|------------|----------------|
| **Initialisation (`__init__`)** | O(n) |
| **Fetching (`fetch(k)`)** | O(n) (removal is O(n), insertion is O(1)) |

> **Alternative:** Using **`deque` from `collections`** could improve the performance for large `n` by reducing `fetch(k)` time complexity.

## 📂 **Project Structure**  
```
1756. Design Most Recently Used Queue/
├── most_recent_queue.py   # Python implementation
├── README.md              # Explanation, walkthrough, and complexity analysis
```

## 🎯 **Key Takeaways**
- This problem demonstrates **modifying a queue dynamically** based on access patterns.
- **List-based queues** work but can be slow due to **O(n) removals**.
- **Deques (double-ended queues)** are a more optimal solution for large `n`.

🚀 **Master queue modifications with this structured approach!** 🎯

---

This README:
✅ **Uses tables and examples** for clarity.  
✅ **Provides time complexity analysis** and **alternative solutions**.  
✅ **Includes a complete walkthrough** with an **optimised approach discussion**.  

**Enjoy your polished, well-documented README!** 🚀