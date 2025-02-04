# 📌 LeetCode 302: Longest Increasing Subsequence&#x20;

## 📝 Overview

This project solves **LeetCode Problem 300: Longest Increasing Subsequence**.
The goal is to determine the **length** of the longest subsequence in a given list where elements are **strictly increasing**.

### **Problem Statement**

Given an integer array `nums`, return the **length** of the longest strictly increasing subsequence.

🔹 **Constraints:**

- `1 <= nums.length <= 2500`
- `-10⁴ <= nums[i] <= 10⁴`

## 🎯 Example Walkthrough

### **Example 1**

```python
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
```

**Explanation:**

- The longest increasing subsequence is `[2, 3, 7, 101]`, which has length `4`.

### **Example 2**

```python
Input: nums = [0,1,0,3,2,3]
Output: 4
```

**Explanation:**

- The longest increasing subsequence is `[0, 1, 2, 3]`.

### **Example 3**

```python
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

**Explanation:**

- Since all elements are the same, the longest subsequence consists of a single element.

## 🚀 Understanding the Approach

### **1️⃣ Key Observations**

✔ A valid subsequence consists of elements where each number is strictly greater than the previous one.
✔ The **order must be preserved** (elements cannot be rearranged).
✔ The problem can be solved using **Dynamic Programming (DP)**.

## 📝 Step-by-Step Algorithm

### **Approach: Dynamic Programming (O(n²))**

1️⃣ **Initialise a DP list** `lis` where every index starts with `1` (each number alone is an increasing subsequence of length 1).

```python
lis = [1] * len(nums)
```

2️⃣ **Iterate through the array in reverse order**:

- For each index `i`, check all elements ahead (`j > i`).
- If `nums[i] < nums[j]`, update `lis[i]`:

```python
lis[i] = max(lis[i], 1 + lis[j])
```

3️⃣ **Find the maximum value** in `lis`, which represents the **length** of the longest increasing subsequence.

```python
return max(lis)
```

## 🔍 Example Walkthrough with Code Execution

### **Input: nums = [10,9,2,5,3,7,101,18]**

#### **Step 1: Initialise DP Array**

```python
lis = [1, 1, 1, 1, 1, 1, 1, 1]  # Every number starts as its own subsequence
```

#### **Step 2: Iterate Backward and Update DP**

| Index `i` | Compare with `j`                | `nums[i] < nums[j]` | Update `lis[i]`              |
| --------- | ------------------------------- | ------------------- | ---------------------------- |
| `6 (101)` | `7 (18)`                        | ❌                   | No change                    |
| `5 (7)`   | `6 (101), 7 (18)`               | ✅                   | `lis[5] = max(1, 1 + 1) = 2` |
| `4 (3)`   | `5 (7), 6 (101), 7 (18)`        | ✅                   | `lis[4] = max(1, 1 + 2) = 3` |
| `2 (2)`   | `4 (3), 5 (7), 6 (101), 7 (18)` | ✅                   | `lis[2] = max(1, 1 + 3) = 4` |

Final `lis` array:

```python
[1, 1, 4, 3, 3, 2, 1, 1]
```

\*\*Maximum value in ****`lis`****: \*\***`4`** → This is the length of the LIS.

## ⏳ **Time Complexity Analysis**

| Approach                     | Time Complexity | Space Complexity |
| ---------------------------- | --------------- | ---------------- |
| **Dynamic Programming (DP)** | **O(n²)** ✅     | **O(n)** ✅       |

- **Iterating through the array** takes `O(n²)`.
- **Space complexity is O(n)** since we store `lis` values.

## **🏗 Project Structure**

```
300. Longest Increasing Subsequence/
├── longest_increasing_subsequence.py    # Python implementation of the solution
├── README.md                            # Detailed explanation & walkthrough
```

✨ **Master dynamic programming with sequence-based problems!** 🚀