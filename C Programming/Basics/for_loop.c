#include <stdio.h>

/*
 * This program demonstrates the usage of the `for` loop in C.
 * Examples include:
 * - Counting numbers.
 * - Calculating the factorial of a number.
 * - Printing a multiplication table.
 * - Iterating over an array.
 */

void count_numbers(int n) {
    // Print numbers from 1 to n
    printf("Counting from 1 to %d:\n", n);
    for (int i = 1; i <= n; i++) {
        printf("%d ", i);
    }
    printf("\n");
}

void calculate_factorial(int number) {
    // Calculate the factorial of a given number
    int factorial = 1; // Initialise factorial to 1
    for (int i = 1; i <= number; i++) {
        factorial *= i; // Multiply factorial by i
    }
    printf("The factorial of %d is: %d\n", number, factorial);
}

void print_multiplication_table(int num, int range) {
    // Print the multiplication table for a given number up to a given range
    printf("Multiplication table for %d:\n", num);
    for (int i = 1; i <= range; i++) {
        printf("%d x %d = %d\n", num, i, num * i);
    }
}

void iterate_array() {
    // Iterate over an array and print its elements
    int numbers[] = {10, 20, 30, 40, 50};
    int size = sizeof(numbers) / sizeof(numbers[0]); // Calculate the number of elements in the array

    printf("Array elements:\n");
    for (int i = 0; i < size; i++) {
        printf("Element %d: %d\n", i + 1, numbers[i]);
    }
}

int main() {
    // Example 1: Counting numbers
    printf("=== Counting Numbers ===\n");
    count_numbers(10);

    // Example 2: Calculating factorial
    printf("\n=== Calculating Factorial ===\n");
    calculate_factorial(5);

    // Example 3: Printing multiplication table
    printf("\n=== Multiplication Table ===\n");
    print_multiplication_table(7, 10);

    // Example 4: Iterating over an array
    printf("\n=== Iterating Over an Array ===\n");
    iterate_array();

    return 0; // Indicate successful program execution
}
