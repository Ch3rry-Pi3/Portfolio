import pandas as pd

def active_businesses(events: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies active businesses that have more than one event type 
    where their occurrences are strictly greater than the average occurrences 
    for that event type.

    Args:
        events (pd.DataFrame): A DataFrame containing event records with columns:
                               - "business_id" (int): Unique ID for the business.
                               - "event_type" (str): Type of event.
                               - "occurrences" (int): Number of times the event occurred.

    Returns:
        pd.DataFrame: A DataFrame containing a single column "business_id"
                      listing all active businesses.
    """
    # Compute the average occurrences per event type
    avg_event_counts = (
        events.groupby("event_type", as_index=False)
        .agg(avg_event_count=("occurrences", "mean"))
    )

    # Merge original events with the average occurrences
    merged_events = events.merge(avg_event_counts, on="event_type", how="left")

    # Mark events where occurrences are strictly greater than the event's average
    merged_events["active"] = (merged_events["occurrences"] > merged_events["avg_event_count"]).astype(int)

    # Count the number of active event types per business
    active_businesses = (
        merged_events.groupby("business_id", as_index=False)["active"]
        .sum()
        .query("active > 1")  # Select businesses with more than one active event type
        [["business_id"]]
    )

    return active_businesses
