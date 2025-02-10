#include <stdio.h>

/*
 * This program demonstrates the use of functions in C.
 * Examples include:
 * - A `void` function that performs an action (printing a greeting).
 * - A value-returning function that performs a calculation (adding two numbers).
 */

// Function prototype for a void function
void print_greeting(const char *name);

// Function prototype for a value-returning function
int add_numbers(int num1, int num2);

int main() {
    // Example 1: Calling the void function
    printf("=== Calling a void function ===\n");
    print_greeting("Alice");

    // Example 2: Calling the value-returning function
    printf("\n=== Calling a value-returning function ===\n");
    int sum = add_numbers(10, 20); // Call the function and store the result
    printf("The sum of 10 and 20 is: %d\n", sum);

    return 0; // Indicate successful program execution
}

// Definition of the void function
void print_greeting(const char *name) {
    // Print a greeting message
    printf("Hello, %s! Welcome to the program.\n", name);
}

// Definition of the value-returning function
int add_numbers(int num1, int num2) {
    // Calculate and return the sum of two integers
    return num1 + num2;
}
