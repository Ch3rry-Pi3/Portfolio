# 📧 **LeetCode 3059: Find All Unique Email Domains**  

## 📌 **Problem Overview**  
You are given a table called **Emails** containing email addresses. Your task is to:  
✅ Find **all unique email domains** ending with `.com`.  
✅ Count the number of individuals associated with each domain.  
✅ Return the result **sorted by email domain in ascending order**.

### 🔹 **Table Structure**  

| Column Name | Type  | Description |
|-------------|-------|-------------|
| `id` | int | Unique identifier for each email. |
| `email` | varchar | The email address. |

## 🎯 **Example Walkthrough**  

### **Example 1**  
#### **Input:**  

| id  | email               |
|-----|---------------------|
| 336 | hwkiy@test.edu      |
| 489 | adcmaf@outlook.com  |
| 499 | vrzmyum@yahoo.com   |
| 95  | toft@test.edu       |
| 320 | jxbahgkm@example.org |
| 411 | zxcf@outlook.com    |

#### **Output:**  

| email_domain | count |
|-------------|------|
| outlook.com | 2 |
| yahoo.com   | 1 |

#### **Explanation:**  
- The valid domains ending with `.com` are `"outlook.com"` and `"yahoo.com"`.  
- `"outlook.com"` appears **twice**, while `"yahoo.com"` appears **once**.  
- The result is **sorted alphabetically** by `email_domain`.

## 🛠 **Approach**  

We solve this problem using **Pandas DataFrame operations**:

1️⃣ **Filter out emails that do not end with `.com`**.  
2️⃣ **Extract the domain part** (everything after `@`).  
3️⃣ **Group by email domain** and **count occurrences**.  
4️⃣ **Sort the result alphabetically by `email_domain`**.  

This approach runs in **O(N) time complexity**, making it highly efficient.

## 🚀 **Python Solution**  

```python
import pandas as pd

def find_unique_email_domains(emails: pd.DataFrame) -> pd.DataFrame:
    """
    Finds unique email domains ending with '.com' and counts the number of occurrences.

    Args:
        emails (pd.DataFrame): A DataFrame containing email addresses.

    Returns:
        pd.DataFrame: A DataFrame with:
            - "email_domain" (str): Unique email domains ending with '.com'.
            - "count" (int): Number of individuals associated with each domain.
    """
    # Filter emails ending with '.com' and extract the domain
    filtered_emails = (
        emails.loc[emails["email"].str.endswith(".com"), "email"]
        .str.split("@", n=1, expand=True)[1]                    # Extract domain part
        .to_frame(name="email_domain")
        .groupby("email_domain", as_index=False)
        .size()                                                 # Count occurrences of each domain
        .rename(columns={"size": "count"})                      # Rename column for clarity
        .sort_values(by="email_domain", ascending=True)         # Sort alphabetically
    )

    return filtered_emails
```

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Filter emails** ending with `.com` | `emails["email"].str.endswith(".com")` | **O(N)** |
| **Extract domains** | `str.split("@", n=1, expand=True)` | **O(N)** |
| **Group and count occurrences** | `groupby().size()` | **O(N)** |
| **Sort results alphabetically** | `sort_values(by="email_domain")` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 📁 **Project Structure**  

```
unique_email_domains/
├── unique_domains.py   # Python solution
├── README.md           # Documentation
```

## 🏆 **Why This Works**  

✔ **Uses efficient Pandas operations** to handle large datasets.  
✔ **Filters only `.com` domains**, ensuring correct results.  
✔ **Runs in O(N log N) complexity**, making it **scalable** for large email datasets.  

🚀 **With this solution, you can efficiently extract and count unique email domains!** 🎯