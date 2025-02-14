import pandas as pd
import numpy as np

def type_of_triangle(triangles: pd.DataFrame) -> pd.DataFrame:
    """
    Classifies triangles based on their side lengths.

    Args:
        triangles (pd.DataFrame): DataFrame with columns ['A', 'B', 'C']
                                  representing the side lengths of triangles.

    Returns:
        pd.DataFrame: A DataFrame with a single column ['triangle_type']
                      containing the classification of each triangle.
    """

    # Check if the given sides can form a valid triangle using the triangle inequality theorem
    invalid_triangle = (
        (triangles['A'] + triangles['B'] <= triangles['C']) |
        (triangles['B'] + triangles['C'] <= triangles['A']) |
        (triangles['A'] + triangles['C'] <= triangles['B'])
    )

    # Classify the triangles using NumPy's vectorised `where` function
    triangles['triangle_type'] = np.where(
        invalid_triangle, 'Not A Triangle',
        np.where(
            (triangles['A'] == triangles['B']) & (triangles['B'] == triangles['C']),
            'Equilateral',
            np.where(
                (triangles['A'] == triangles['B']) |
                (triangles['B'] == triangles['C']) |
                (triangles['A'] == triangles['C']),
                'Isosceles',
                'Scalene'
            )
        )
    )

    return triangles[['triangle_type']]


def main():
    """Main function to test the triangle classification."""
    # Example DataFrame
    data = {
        'A': [5, 20, 20, 13],
        'B': [5, 20, 21, 14],
        'C': [5, 22, 22, 30]
    }
    triangles_df = pd.DataFrame(data)

    # Classify the triangles
    result = type_of_triangle(triangles_df)

    # Display the results
    print(result)


if __name__ == "__main__":
    main()
