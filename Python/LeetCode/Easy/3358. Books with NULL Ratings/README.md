# 📚 **LeetCode 3358: Books with NULL Ratings**  

## 📌 **Problem Overview**  
Given a dataset of **books and their ratings**, we need to **identify books** that **have not been rated yet** (i.e., have a **NULL rating**).  

The output should include only the **book ID, title, author, and published year**, sorted in **ascending order by `book_id`**.  

## 🔍 **Example Walkthrough**  

### **Input:**
```python
books_data = {
    "book_id": [1, 2, 3, 4, 5, 6],
    "title": [
        "The Great Gatsby", "To Kill a Mockingbird", "Pride and Prejudice",
        "The Catcher in the Rye", "Animal Farm", "Lord of the Flies"
    ],
    "author": [
        "F. Scott", "Harper Lee", "Jane Austen", 
        "J.D. Salinger", "George Orwell", "William Golding"
    ],
    "published_year": [1925, 1960, 1813, 1951, 1945, 1954],
    "rating": [4.5, None, 4.8, None, 4.2, None]
}
```

### **Processing Logic:**
| Book ID | Title                    | Author           | Published Year | Rating |
|---------|--------------------------|-----------------|---------------|--------|
| **1**   | The Great Gatsby         | F. Scott       | 1925          | **4.5**  |
| **2**   | To Kill a Mockingbird    | Harper Lee     | 1960          | **NULL**  |
| **3**   | Pride and Prejudice      | Jane Austen    | 1813          | **4.8**  |
| **4**   | The Catcher in the Rye   | J.D. Salinger  | 1951          | **NULL**  |
| **5**   | Animal Farm              | George Orwell  | 1945          | **4.2**  |
| **6**   | Lord of the Flies        | William Golding| 1954          | **NULL**  |

1. **Filter books that have a NULL rating**  
   - ✅ **Keep**:  
     - `To Kill a Mockingbird`  
     - `The Catcher in the Rye`  
     - `Lord of the Flies`  
   - ❌ **Ignore**:  
     - `The Great Gatsby` (Has a rating: `4.5`)  
     - `Pride and Prejudice` (Has a rating: `4.8`)  
     - `Animal Farm` (Has a rating: `4.2`)  

2. **Drop the `rating` column**  

3. **Sort by `book_id` in Ascending Order**  

### **Final Result:**
| Book ID | Title                   | Author          | Published Year |
|---------|-------------------------|----------------|---------------|
| **2**   | To Kill a Mockingbird   | Harper Lee    | 1960          |
| **4**   | The Catcher in the Rye  | J.D. Salinger | 1951          |
| **6**   | Lord of the Flies       | William Golding | 1954          |

## 🛠 **Python Solution**
```python
import pandas as pd

def find_unrated_books(books: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies books that have not been rated yet (i.e., have a NULL rating).

    Parameters:
    books (pd.DataFrame): A DataFrame containing book information with columns:
                          - 'book_id' (int): Unique identifier for each book.
                          - 'title' (str): Title of the book.
                          - 'author' (str): Author of the book.
                          - 'published_year' (int): Year the book was published.
                          - 'rating' (float or NaN): Rating of the book (NULL if not rated).

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'book_id' (int): Unique book identifier.
                  - 'title' (str): Book title.
                  - 'author' (str): Book author.
                  - 'published_year' (int): Year of publication.
                  The result is sorted in ascending order by 'book_id'.
    """
    # Filter books that have a NULL rating
    unrated_books = books[books["rating"].isna()]

    # Drop the 'rating' column and sort by 'book_id'
    return unrated_books.drop(columns=["rating"]).sort_values(by="book_id")
```

## ⏳ **Complexity Analysis**
| Step         | Operation                     | Time Complexity |
|-------------|------------------------------|----------------|
| Filtering   | `.isna()` to find NULL ratings | **O(N)** |
| Dropping    | `.drop(columns=["rating"])`    | **O(1)** |
| Sorting     | `.sort_values(by="book_id")`  | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

Since sorting dominates, the overall complexity is **O(N log N)**.

## 🚀 **How to Use**
### **1️⃣ Installation**
Ensure you have **Python 3.x** and install Pandas if not installed:  
```bash
pip install pandas
```

### **2️⃣ Running the Script**
```bash
python null_rating.py
```

### **3️⃣ Sample Output**
```plaintext
   book_id                   title          author  published_year
1       2  To Kill a Mockingbird    Harper Lee            1960
3       4  The Catcher in the Rye  J.D. Salinger        1951
5       6  Lord of the Flies      William Golding      1954
```

## 🎯 **Why This Approach?**
✔ Uses **Pandas `.isna()`** to efficiently find NULL (`NaN`) ratings.  
✔ Implements **`.drop(columns=["rating"])`** for clarity instead of `.iloc[:, :-1]`.  
✔ Ensures **sorted ordering by `book_id`** to match problem requirements.  
✔ 🚀 **Optimised for large datasets with `O(N log N)` complexity.**  

🔥 **This method ensures a structured, efficient, and scalable solution for identifying books with missing ratings!** 📚✨