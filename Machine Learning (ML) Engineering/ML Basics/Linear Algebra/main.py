from typing import List, Union

Number = Union[int, float]

def matrix_dot_vector(a: List[List[Number]], b: List[Number]) -> List[Number] | int:
    """
    Computes the dot product of a matrix and a vector.

    Each row of the matrix is multiplied element-wise with the vector,
    and the results are summed to produce a resulting vector.

    :param a: 2D list representing the matrix (m x n)
    :param b: 1D list representing the vector (length n)
    :return: A list representing the resulting vector of length m,
             or -1 if the matrix and vector dimensions do not match.
    """
    if len(a[0]) != len(b):
        return -1

    result = []
    for row in a:
        total = 0
        for i in range(len(row)):
            total += row[i] * b[i]
        result.append(total)
    return result


def main():
    """
    Demonstrates the use of the matrix_dot_vector function with various test cases.
    """
    # Test case 1: Valid multiplication
    matrix1 = [[1, 2, 3], [2, 4, 5], [6, 8, 9]]
    vector1 = [1, 2, 3]
    print(f"Input: {matrix1} x {vector1}")
    print(f"Output: {matrix_dot_vector(matrix1, vector1)}\n")  # Expected: [14, 25, 50]

    # Test case 2: Another valid multiplication
    matrix2 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
    vector2 = [7, 8, 9]
    print(f"Input: {matrix2} x {vector2}")
    print(f"Output: {matrix_dot_vector(matrix2, vector2)}\n")  # Expected: [9, 7, 8]

    # Test case 3: Invalid multiplication (dimension mismatch)
    matrix3 = [[1, 2], [3, 4]]
    vector3 = [1, 2, 3]
    print(f"Input: {matrix3} x {vector3}")
    print(f"Output: {matrix_dot_vector(matrix3, vector3)}\n")  # Expected: -1

    # Test case 4: Mixed floats and ints
    matrix4 = [[1.5, 2], [3, 4.5]]
    vector4 = [2, 3]
    print(f"Input: {matrix4} x {vector4}")
    print(f"Output: {matrix_dot_vector(matrix4, vector4)}\n")  # Expected: [1.5*2 + 2*3 = 3 + 6 = 9.0, 3*2 + 4.5*3 = 6 + 13.5 = 19.5]


if __name__ == "__main__":
    main()
