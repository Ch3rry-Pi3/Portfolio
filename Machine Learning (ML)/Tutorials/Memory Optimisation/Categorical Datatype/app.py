"""
Memory Optimisation in Pandas

This script optimises memory usage by converting object-type columns to categorical
in a Pandas DataFrame. The script loads a dataset, checks memory usage before
and after conversion, and calculates the percentage decrease in memory usage.
"""

import pandas as pd

def optimise_memory(df, column_name):
    """Convert an object column to categorical and display memory usage."""
    # Compute memory usage before conversion
    mem_before = df[column_name].memory_usage(deep=True)
    print(f"Memory usage of '{column_name}' column before conversion: {mem_before / 1024:.2f} KB\n")

    # Convert column to categorical type
    df[column_name] = df[column_name].astype("category")

    # Compute memory usage after conversion
    mem_after = df[column_name].memory_usage(deep=True)
    print(f"Memory usage of '{column_name}' column after conversion: {mem_after / 1024:.2f} KB\n")

    # Calculate percentage decrease in memory usage
    mem_decrease = ((mem_before - mem_after) / mem_before) * 100
    print(f"Percentage decrease in memory usage: {mem_decrease:.2f}%")

def main():
    """Main function to load data and optimise memory usage."""
    # Load the dataset
    df = pd.read_csv("data/titanic_train.csv")
    
    # Display first few rows
    print("First 5 rows of the dataset:")
    print(df.head(), "\n")
    
    # Optimise memory usage for the 'Gender' column
    optimise_memory(df, "Gender")

if __name__ == "__main__":
    main()
