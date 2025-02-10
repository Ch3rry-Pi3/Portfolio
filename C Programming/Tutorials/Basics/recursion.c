#include <stdio.h>

/*
 * This program demonstrates recursion in C.
 * Examples include:
 * - Calculating the factorial of a number using recursion.
 * - Generating Fibonacci numbers using recursion.
 */

// Function prototype for factorial calculation
int factorial(int n);

// Function prototype for Fibonacci number generation
int fibonacci(int n);

int main() {
    // Example 1: Factorial calculation
    printf("=== Factorial Calculation ===\n");
    int num = 5;
    printf("Factorial of %d is: %d\n", num, factorial(num));

    // Example 2: Fibonacci sequence generation
    printf("\n=== Fibonacci Sequence ===\n");
    int terms = 7;
    printf("First %d terms of the Fibonacci sequence:\n", terms);
    for (int i = 0; i < terms; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");

    return 0; // Indicate successful program execution
}

// Recursive function to calculate factorial of a number
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1; // Base case: Factorial of 0 or 1 is 1
    }
    return n * factorial(n - 1); // Recursive case
}

// Recursive function to generate the nth Fibonacci number
int fibonacci(int n) {
    if (n == 0) {
        return 0; // Base case: First Fibonacci number is 0
    }
    if (n == 1) {
        return 1; // Base case: Second Fibonacci number is 1
    }
    return fibonacci(n - 1) + fibonacci(n - 2); // Recursive case
}
