#include <stdio.h>

/*
 * This program demonstrates the usage of the ternary operator in C.
 * 
 * The ternary operator is a shorthand for `if-else` and has the syntax:
 *   condition ? expression1 : expression2;
 * 
 * Examples include:
 * - Checking if a number is positive, negative, or zero.
 * - Determining the maximum of two numbers.
 * - Assigning values based on a condition.
 */

void check_number(int number) {
    // Use the ternary operator to check if a number is positive, negative, or zero
    const char *result = (number > 0) ? "positive" : 
                         (number < 0) ? "negative" : "zero";
    printf("The number %d is %s.\n", number, result);
}

void find_maximum(int a, int b) {
    // Use the ternary operator to find the maximum of two numbers
    int max = (a > b) ? a : b;
    printf("The maximum of %d and %d is %d.\n", a, b, max);
}

void assign_values(int condition) {
    // Use the ternary operator to assign values based on a condition
    int x = condition ? 10 : 20;
    printf("Condition is %s, so x = %d.\n", condition ? "true" : "false", x);
}

int main() {
    // Example 1: Check if a number is positive, negative, or zero
    printf("=== Check Number ===\n");
    check_number(5);
    check_number(-3);
    check_number(0);

    // Example 2: Find the maximum of two numbers
    printf("\n=== Find Maximum ===\n");
    find_maximum(10, 20);
    find_maximum(15, 7);

    // Example 3: Assign values based on a condition
    printf("\n=== Assign Values ===\n");
    assign_values(1); // Condition is true
    assign_values(0); // Condition is false

    return 0; // Indicate successful program execution
}
