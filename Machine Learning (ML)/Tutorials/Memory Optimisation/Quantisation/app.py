"""
Integer Memory Optimisation in Pandas

This script optimises memory usage by converting integer columns from the default `int64`
to a lower-memory integer type (`int8`). This technique helps in reducing memory consumption
significantly when working with large datasets.
"""

import pandas as pd
import numpy as np

def optimise_integer_memory(df, column_name):
    """Convert an integer column to a lower-memory integer type and display memory savings."""
    # Compute memory usage before conversion
    mem_before = df[column_name].memory_usage(deep=True)
    print(f"Memory usage of '{column_name}' column before conversion: {mem_before / 1024 / 1024:.2f} MB")
    
    # Find min and max values
    col_min, col_max = df[column_name].min(), df[column_name].max()
    print(f"Minimum value: {col_min}, Maximum value: {col_max}\n")
    
    # Convert column to int8 type
    df[column_name] = df[column_name].astype(np.int8)
    
    # Compute memory usage after conversion
    mem_after = df[column_name].memory_usage(deep=True)
    print(f"Memory usage of '{column_name}' column after conversion: {mem_after / 1024 / 1024:.2f} MB")
    
    # Calculate percentage decrease in memory usage
    mem_decrease = ((mem_before - mem_after) / mem_before) * 100
    print(f"Percentage decrease in memory usage: {mem_decrease:.2f}%\n")

def main():
    """Main function to generate data and optimise memory usage."""
    # Create a large dataset
    df = pd.DataFrame(np.random.randint(1, 100, (10**7, 2)), columns=["A", "B"])
    
    # Optimise memory usage for the 'A' column
    optimise_integer_memory(df, "A")

if __name__ == "__main__":
    main()