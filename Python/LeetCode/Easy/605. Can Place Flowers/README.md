# 🌱 LeetCode 605: Can Place Flowers

## 📝 Overview
This project solves **LeetCode Problem 605: Can Place Flowers**.
The goal is to determine whether a given number of flowers can be planted in a flowerbed without violating the **no-adjacent-flowers rule**.

### **Problem Statement**
You are given a flowerbed represented as an array `flowerbed` where:
- `0` represents an **empty plot**.
- `1` represents an **occupied plot**.

You are also given an integer `n`, which represents the number of new flowers you want to plant.
Return `True` if it is possible to plant `n` flowers while following the rules, otherwise return `False`.

🔹 **Constraints:**
- `1 <= flowerbed.length <= 2 * 10^4`
- `flowerbed[i]` is `0` or `1`.
- `0 <= n <= flowerbed.length`

## 🎯 Example Walkthrough

### **Example 1**
```python
Input: flowerbed = [1, 0, 0, 0, 1], n = 1
Output: True
```
**Explanation:**
- The flowerbed initially looks like: `[1, 0, 0, 0, 1]`
- The second `0` (middle empty plot) is **valid** for planting because both adjacent plots are empty.
- The updated flowerbed becomes `[1, 0, 1, 0, 1]`.
- Since `1` flower was successfully planted, return `True`.

### **Example 2**
```python
Input: flowerbed = [1, 0, 0, 0, 1], n = 2
Output: False
```
**Explanation:**
- The flowerbed initially looks like: `[1, 0, 0, 0, 1]`
- Only **one** valid position exists to plant a flower.
- Since `n = 2` flowers are required but only `1` can be placed, return `False`.

### **Example 3**
```python
Input: flowerbed = [0, 0, 1], n = 1
Output: True
```
**Explanation:**
- We pretend there are empty plots at both ends: `[0, 0, 1]` becomes `[0, 0, 1, 0]`.
- The first `0` can be planted without violating the rule.
- The final flowerbed is `[1, 0, 1]`, so return `True`.

## 🚀 Understanding the Approach
### **Key Observations**
✔ We **pad the flowerbed** with extra `0`s at the beginning and end to simplify edge cases.
✔ We **iterate through the array** and check each position to see if a flower can be placed.
✔ If a flower is placed, we **decrement `n`**, and if `n` reaches `0`, we return `True` early.
✔ If the loop completes without placing `n` flowers, return `False`.

## 📝 Step-by-Step Algorithm
1️⃣ **Pad the flowerbed** with an extra `0` at both ends to handle edge cases.
2️⃣ **Iterate through each plot**, skipping the first and last (virtual) plots.
3️⃣ **Check conditions**:
   - The **current plot** must be empty (`0`).
   - The **left and right neighbors** must also be empty (`0`).
4️⃣ **Place a flower** if conditions are met, update the flowerbed, and decrement `n`.
5️⃣ **Return `True` early** if all flowers are placed (`n <= 0`).
6️⃣ If loop finishes and `n > 0`, return `False`.

## 🔍 Example Walkthrough with Code Execution

### **Input: flowerbed = [1, 0, 0, 0, 1], n = 1**
#### **Step 1: Pad the Array**
```python
flowerbed = [1, 0, 0, 0, 1] → Add virtual zeros → [0, 1, 0, 0, 0, 1, 0]
```

#### **Step 2: Check Each Position**
- `i = 1`: `1` (occupied) → **Skip**
- `i = 2`: `0` (empty), left is `1` → **Skip**
- `i = 3`: `0` (empty), left is `0`, right is `0` → **Plant flower** ✅
- Updated flowerbed: `[1, 0, 1, 0, 1]`
- `n` is now `0`, return `True` ✅

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Iterate through flowerbed & check conditions** | **O(N)** ✅ | **O(1)** ✅ |

- We **iterate once** through `flowerbed`, making the approach **O(N)**.
- No additional space is used beyond the input array, making it **O(1)**.

## **🏗 Project Structure**
```
605. Can Place Flowers/
├── place_flowers.py    # Python implementation of the solution
├── README.md           # Detailed explanation & walkthrough
```

✨ **Master greedy placement problems with an intuitive approach!** 🚀

