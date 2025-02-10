#include <stdio.h>

/*
 * This program demonstrates basic array operations in C.
 * Examples include:
 * - Initializing and printing an array.
 * - Calculating the sum and average of elements.
 * - Modifying array elements.
 * - Simulating appending and popping elements in an array.
 */

#define MAX_SIZE 10 // Define the maximum size of the array

int main() {
    // Example 1: Initializing and printing an array
    printf("=== Array Initialization and Printing ===\n");
    int numbers[MAX_SIZE] = {10, 20, 30, 40, 50}; // Initialize an array with some elements
    int size = 5; // Current number of elements in the array
    printf("Array elements: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    // Example 2: Calculating the sum and average
    printf("\n=== Sum and Average of Array Elements ===\n");
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += numbers[i];
    }
    double average = sum / (double)size; // Calculate the average
    printf("Sum: %d\n", sum);
    printf("Average: %.2f\n", average);

    // Example 3: Modifying array elements
    printf("\n=== Modifying Array Elements ===\n");
    numbers[2] = 100; // Change the third element (index 2) to 100
    printf("Modified array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    // Example 4: Simulating appending an element
    printf("\n=== Appending an Element ===\n");
    if (size < MAX_SIZE) {
        numbers[size] = 60; // Add a new element at the end
        size++; // Increase the current size
        printf("Appended 60. New array: ");
        for (int i = 0; i < size; i++) {
            printf("%d ", numbers[i]);
        }
        printf("\n");
    } else {
        printf("Array is full. Cannot append.\n");
    }

    // Example 5: Simulating popping an element
    printf("\n=== Popping an Element ===\n");
    if (size > 0) {
        int popped = numbers[size - 1]; // Get the last element
        size--; // Decrease the current size
        printf("Popped %d. New array: ", popped);
        for (int i = 0; i < size; i++) {
            printf("%d ", numbers[i]);
        }
        printf("\n");
    } else {
        printf("Array is empty. Cannot pop.\n");
    }

    return 0; // Indicate successful program execution
}
