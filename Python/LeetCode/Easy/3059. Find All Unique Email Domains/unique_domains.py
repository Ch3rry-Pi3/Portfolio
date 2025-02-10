import pandas as pd

def find_unique_email_domains(emails: pd.DataFrame) -> pd.DataFrame:
    """
    Finds unique email domains ending with '.com' and counts the number of occurrences.

    Args:
        emails (pd.DataFrame): A DataFrame containing email addresses with columns:
            - "id" (int): Unique identifier for each email.
            - "email" (str): The email address.

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


def main():
    """
    Runs example test cases for the find_unique_email_domains function.
    """
    # Sample email data
    email_data = {
        "id": [336, 489, 499, 95, 320, 411],
        "email": [
            "hwkiy@test.edu",
            "adcmaf@outlook.com",
            "vrzmyum@yahoo.com",
            "toft@test.edu",
            "jxbahgkm@example.org",
            "zxcf@outlook.com",
        ],
    }

    # Convert to DataFrame
    emails_df = pd.DataFrame(email_data)

    # Find unique email domains
    result = find_unique_email_domains(emails_df)
    print(result)


if __name__ == "__main__":
    main()
