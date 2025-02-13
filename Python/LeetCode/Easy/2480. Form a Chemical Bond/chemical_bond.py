import pandas as pd

def form_bond(elements: pd.DataFrame) -> pd.DataFrame:
    """
    Forms all possible pairs of chemical bonds between elements classified as 'Metal' and 'Nonmetal'.
    
    Parameters:
    elements (pd.DataFrame): A DataFrame containing element information with the columns:
                             - 'symbol' (str): The chemical symbol of the element.
                             - 'type' (str): The classification of the element ('Metal', 'Nonmetal', or 'Noble').
                             - 'electrons' (int): The number of electrons the element can give or take.
    
    Returns:
    pd.DataFrame: A DataFrame containing all valid (Metal, Nonmetal) element pairs.
    """
    # Filter metals and nonmetals from the elements DataFrame
    metals = elements.loc[elements["type"] == "Metal", ["symbol"]].rename(columns={"symbol": "metal"})
    nonmetals = elements.loc[elements["type"] == "Nonmetal", ["symbol"]].rename(columns={"symbol": "nonmetal"})
    
    # Perform a cross join to form all possible metal-nonmetal pairs
    bonds = pd.merge(metals, nonmetals, how="cross")

    return bonds


def main():
    """
    Main function to demonstrate the form_bond function with a sample dataset.
    """
    # Sample input data as a dictionary
    data = {
        "symbol": ["He", "Na", "Ca", "La", "Cl", "O", "N"],
        "type": ["Noble", "Metal", "Metal", "Metal", "Nonmetal", "Nonmetal", "Nonmetal"],
        "electrons": [0, 1, 2, 3, 1, 2, 3]
    }
    
    # Convert dictionary to DataFrame
    elements = pd.DataFrame(data)
    
    # Generate all possible metal-nonmetal bonds
    bond_pairs = form_bond(elements)
    
    # Display the result
    print(bond_pairs)


# Run the script only if executed directly
if __name__ == "__main__":
    main()
