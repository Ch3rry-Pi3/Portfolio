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


def main():
    """
    Main function to demonstrate the find_unrated_books function with a sample dataset.
    """
    # Sample books data
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

    # Convert dictionary to DataFrame
    books_df = pd.DataFrame(books_data)

    # Find books with NULL ratings
    result = find_unrated_books(books_df)

    # Display result
    print(result)


# Run the script only if executed directly
if __name__ == "__main__":
    main()
