#include <stdio.h>

/*
 * This program demonstrates basic operations on multidimensional arrays in C.
 * Examples include:
 * - Initializing and printing a 2D array.
 * - Calculating the sum of all elements.
 * - Modifying specific elements.
 * - Simulating appending rows to a 2D array.
 */

#define ROWS 3
#define COLS 4
#define MAX_ROWS 5 // Define the maximum number of rows for appending

int main() {
    // Example 1: Initializing and printing a 2D array
    printf("=== Initializing and Printing a 2D Array ===\n");
    int array[MAX_ROWS][COLS] = { // 5 rows, each with 4 columns
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    int current_rows = 3; // Track the number of currently active rows

    // Print the 2D array
    printf("Initial 2D Array:\n");
    for (int i = 0; i < current_rows; i++) {
        for (int j = 0; j < COLS; j++) {
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }

    // Example 2: Calculating the sum of all elements
    printf("\n=== Calculating the Sum of Elements ===\n");
    int sum = 0;
    for (int i = 0; i < current_rows; i++) {
        for (int j = 0; j < COLS; j++) {
            sum += array[i][j];
        }
    }
    printf("Sum of all elements: %d\n", sum);

    // Example 3: Modifying specific elements
    printf("\n=== Modifying Specific Elements ===\n");
    array[1][2] = 99; // Modify the element at row 1, column 2
    printf("Modified 2D Array:\n");
    for (int i = 0; i < current_rows; i++) {
        for (int j = 0; j < COLS; j++) {
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }

    // Example 4: Simulating appending a new row
    printf("\n=== Simulating Appending a Row ===\n");
    if (current_rows < MAX_ROWS) {
        int new_row[COLS] = {13, 14, 15, 16}; // Define the new row
        for (int j = 0; j < COLS; j++) {
            array[current_rows][j] = new_row[j]; // Copy new row into the 2D array
        }
        current_rows++; // Increase the row count
        printf("After appending a new row:\n");
        for (int i = 0; i < current_rows; i++) {
            for (int j = 0; j < COLS; j++) {
                printf("%d ", array[i][j]);
            }
            printf("\n");
        }
    } else {
        printf("Cannot append. Array is full.\n");
    }

    // Example 5: Accessing specific elements
    printf("\n=== Accessing Specific Elements ===\n");
    printf("Element at row 2, column 3: %d\n", array[2][3]); // Access element at row 2, column 3

    return 0; // Indicate successful program execution
}
