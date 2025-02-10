#include <stdio.h>

/*
 * This program demonstrates basic arithmetic operations in C, 
 * including addition, division, increment, and the application of 
 * operator precedence (BODMAS).
 */

int main() {
    // Declare an integer variable and initialise it
    int x = 12;

    // Perform addition and store the result
    int addition = x + 8;
    // Print the result of the addition
    printf("Addition: %d\n", addition);

    // Perform floating-point division by casting x to double
    double division = (double)x / 8;
    // Print the result of the division with 2 decimal places
    printf("Floating-Point Division: %.2f\n", division);

    // Increment the value of x and store the new value
    int increment = ++x;
    // Print the incremented value
    printf("Increment: %d\n", increment);

    // Perform a complex arithmetic operation using BODMAS
    int y = 4 / 2 + 6 * 5 - 1;
    // Print the result of the BODMAS operation
    printf("BODMAS: %d", y);

    return 0; 
}