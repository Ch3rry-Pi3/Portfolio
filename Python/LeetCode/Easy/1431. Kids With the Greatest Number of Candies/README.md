# 🍬 Kids With the Greatest Number of Candies

## 📝 Overview
This project solves **LeetCode Problem 1431: Kids With the Greatest Number of Candies**.  
The goal is to determine which kids will have the most candies if given extra candies.

### **Problem Statement**
Given an array `candies`, where `candies[i]` represents the number of candies the `i`th kid has, and an integer `extraCandies`, return a boolean array where:
- `True` means that the `i`th kid can have the **greatest number of candies** after receiving the extra candies.
- `False` otherwise.

🔹 **Constraints:**
- `2 <= candies.length <= 100`
- `1 <= candies[i] <= 100`
- `1 <= extraCandies <= 50`

## 🎯 Example Walkthrough

### **Example 1**
```python
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [True, True, True, False, True]
```
**Explanation:**
- Kid 1: `2 + 3 = 5` ✅ (max)
- Kid 2: `3 + 3 = 6` ✅ (max)
- Kid 3: `5 + 3 = 8` ✅ (max)
- Kid 4: `1 + 3 = 4` ❌ (not max)
- Kid 5: `3 + 3 = 6` ✅ (max)

### **Example 2**
```python
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [True, False, False, False, False]
```
**Explanation:**
- Kid 1: `4 + 1 = 5` ✅ (max)
- Kid 2: `2 + 1 = 3` ❌
- Kid 3: `1 + 1 = 2` ❌
- Kid 4: `1 + 1 = 2` ❌
- Kid 5: `2 + 1 = 3` ❌

## 🚀 Understanding the Approach
### **1️⃣ Key Observations**
✔ We first determine the **maximum number of candies** among all kids.
✔ For each kid, check if `candies[i] + extraCandies` reaches or exceeds this maximum.
✔ Store the results in a boolean list.

## 📝 Step-by-Step Algorithm
1️⃣ Find the **maximum candies** a kid currently has.
2️⃣ Iterate through the list and check if `candies[i] + extraCandies >= max_candies`.
3️⃣ Return a list of boolean values indicating whether each kid can reach the maximum number of candies.

## 🔍 Example Walkthrough with Code Execution

### **Input: candies = [2,3,5,1,3], extraCandies = 3**
#### **Step 1: Compute Maximum Candies**
```python
max_candy = max([2,3,5,1,3]) = 5
```

#### **Step 2: Check Each Kid's Candies**
| Kid # | Candies | After Extra | Can Have Max? |
|--------|---------|-------------|--------------|
| 1      | 2       | 5           | ✅ True      |
| 2      | 3       | 6           | ✅ True      |
| 3      | 5       | 8           | ✅ True      |
| 4      | 1       | 4           | ❌ False     |
| 5      | 3       | 6           | ✅ True      |

✅ **Final Output:** `[True, True, True, False, True]`

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Iterate through candies** | **O(N)** ✅ | **O(1)** ✅ |

- **We iterate through `candies` once**, making the approach **O(N)**.
- **No extra space is used except for the output list**, making it **O(1)**.

## **🏗 Project Structure**
```
1431. Kids With the Greatest Number of Candies/
├── max_candies.py    # Python implementation of the solution
├── README.md         # Detailed explanation & walkthrough
```

✨ **Solve problems efficiently using simple list operations!** 🚀

