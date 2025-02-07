Of course! Here’s your **beautifully formatted** **`README.md`** for **`friend_requests.py`**, with **clear explanations, examples, and an intuitive walkthrough** to help understand the approach. 🚀😊  

---

# 🤝 **LeetCode 597: Friend Requests I - Overall Acceptance Rate**

## 📌 **Overview**
This project solves **LeetCode Problem 597: Friend Requests I - Overall Acceptance Rate**.  
The goal is to **calculate the overall acceptance rate of friend requests** using given tables.

### **Problem Statement**
We have two tables:

- **FriendRequest**: Contains **all sent friend requests**.
- **RequestAccepted**: Contains **only accepted friend requests**.

#### **Acceptance Rate Formula:**

\[
\text{acceptance_rate} = \frac{\text{Total Accepted Requests}}{\text{Total Friend Requests}}
\]

- If **no requests exist**, return **0.00**.
- Each request **should be counted only once** (i.e., remove duplicates).

---

## 🎯 **Example Walkthrough**
### **Example Input**
#### **FriendRequest Table**
| sender_id | send_to_id | request_date |
|-----------|-----------|--------------|
| 1         | 2         | 2021-07-01   |
| 2         | 3         | 2021-07-02   |
| 3         | 4         | 2021-07-03   |
| 3         | 4         | 2021-07-03   |
| 4         | 5         | 2021-07-04   |
| 4         | 5         | 2021-07-04   |

#### **RequestAccepted Table**
| requester_id | accepter_id | accept_date |
|-------------|-------------|--------------|
| 1           | 2           | 2021-07-02   |
| 3           | 4           | 2021-07-03   |
| 3           | 4           | 2021-07-03   |
| 4           | 5           | 2021-07-05   |

---

### **Step-by-Step Breakdown**
1️⃣ **Remove duplicate friend requests**  
   - **Before deduplication** → `6` requests  
   - **After deduplication** → `4` unique requests  

2️⃣ **Remove duplicate accepted requests**  
   - **Before deduplication** → `4` acceptances  
   - **After deduplication** → `3` unique acceptances  

3️⃣ **Compute acceptance rate**  
\[
\frac{3}{4} = 0.75
\]

### **Expected Output**
```python
Output:
accept_rate
0.75
```

---

## 🧠 **Intuition Behind the Approach**
### **Key Observations**
✔ **Some friend requests might not be accepted.**  
✔ **Some accepted requests might not appear in the friend request table.**  
✔ **Requests and acceptances should be counted uniquely (remove duplicates).**  
✔ **If no requests exist, return `0.00`.**  

---

## 📝 **Step-by-Step Approach**
### **1️⃣ Remove Duplicates**
- Deduplicate both **FriendRequest** and **RequestAccepted** tables.

### **2️⃣ Count Requests and Acceptances**
- Compute:
  - **Total unique friend requests**.
  - **Total unique accepted requests**.

### **3️⃣ Compute Acceptance Rate**
- Use the formula:
  ```python
  acceptance_rate = round(accepted_count / request_count, 2) if request_count != 0 else 0.00
  ```
- Round the result **to 2 decimal places**.

---

## **💡 Implementation**
```python
import pandas as pd

def acceptance_rate(friend_request: pd.DataFrame, request_accepted: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the overall friend request acceptance rate.

    The acceptance rate is calculated as:
        acceptance_rate = (Total Accepted Requests / Total Friend Requests)

    If no requests exist, the function returns 0.00.

    :param friend_request: DataFrame containing 'sender_id', 'send_to_id', and 'request_date'.
    :param request_accepted: DataFrame containing 'requester_id', 'accepter_id', and 'accept_date'.
    :return: DataFrame with a single column 'accept_rate' rounded to 2 decimal places.
    """

    # Drop duplicate requests and accepted requests to count only unique interactions
    distinct_accepted = request_accepted[['requester_id', 'accepter_id']].drop_duplicates()
    distinct_request = friend_request[['sender_id', 'send_to_id']].drop_duplicates()

    # Count distinct requests and acceptances
    accepted_count = len(distinct_accepted)
    request_count = len(distinct_request)

    # Compute acceptance rate, ensuring division by zero is handled
    accept_rate = round(accepted_count / request_count, 2) if request_count != 0 else 0.00

    # Return result as a DataFrame
    return pd.DataFrame({"accept_rate": [accept_rate]})


def main():
    """
    Demonstrates testing the acceptance_rate function on example datasets.
    """
    # Example test data
    friend_request_data = {
        "sender_id": [1, 2, 3, 3, 4, 4],
        "send_to_id": [2, 3, 4, 4, 5, 5],
        "request_date": pd.to_datetime([
            "2021-07-01", "2021-07-02", "2021-07-03",
            "2021-07-03", "2021-07-04", "2021-07-04"
        ])
    }

    request_accepted_data = {
        "requester_id": [1, 3, 3, 4],
        "accepter_id": [2, 4, 4, 5],
        "accept_date": pd.to_datetime([
            "2021-07-02", "2021-07-03", "2021-07-03", "2021-07-05"
        ])
    }

    # Convert dictionaries to DataFrames
    friend_request_df = pd.DataFrame(friend_request_data)
    request_accepted_df = pd.DataFrame(request_accepted_data)

    print("Friend Request DataFrame:")
    print(friend_request_df, "\n")

    print("Request Accepted DataFrame:")
    print(request_accepted_df, "\n")

    # Compute acceptance rate
    result = acceptance_rate(friend_request_df, request_accepted_df)

    print("Acceptance Rate:")
    print(result)


if __name__ == "__main__":
    main()
```

---

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Dropping Duplicates (`O(n)`)** | **O(n)** ✅ | **O(n)** ✅ |

- **Each record is processed once** (`O(n) time complexity`).
- **Stores results in a new DataFrame** (`O(n) space complexity`).

---

## 🏗 **Project Structure**
```
597. Friend Requests Acceptance Rate/
├── friend_requests.py    # Python implementation of the solution
├── README.md             # Detailed explanation & walkthrough
```

✨ **Master friend request acceptance rate calculations with this efficient `O(n)` approach!** 🚀  

---

## 🎯 **Why This Solution?**
✔ **Uses an optimal `O(n)` approach for counting requests**  
✔ **Efficiently handles duplicates before counting**  
✔ **Handles cases where no friend requests exist (`0.00`)**  
✔ **Well-structured and intuitive for learning**  

🔥 Now it's **clean, structured, and ready for your portfolio or coding practice!** 🚀😊 Let me know if you'd like any refinements!