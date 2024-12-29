#include <stdio.h>

/*
 * This program demonstrates the usage of various data types in C
 * and their associated properties.
 * 
 * Author: [Your Name]
 * Date: [Date]
 * 
 * Description:
 * - The program covers:
 *   1. Declaring and initializing variables of different data types:
 *      - int (integer)
 *      - double (double-precision floating-point)
 *      - float (single-precision floating-point)
 *      - char (character)
 *   2. Printing values of these data types using the printf function.
 *   3. Demonstrating format specifiers for different data types:
 *      - %d for integers
 *      - %lf for double
 *      - %f for float
 *      - %c for char
 *   4. Using `sizeof` to determine the size (in bytes) of data types.
 * 
 * Key Concepts:
 * - Data types and their memory requirements.
 * - Format specifiers for printf.
 * - Precision formatting for floating-point numbers.
 * - Using the sizeof operator to inspect memory usage.
 */

int main() {
    
    // Declare and initialize an integer variable
    int integer = 10;
    printf("Integer = %d", integer);

    // Declare and initialize a double variable
    double double1 = 12.45;
    printf("\nDouble = %lf", double1);

    // Print the double value with 2 decimal places
    printf("\nDouble (2 dp) = %.2lf", double1);

    // Declare and initialize a float variable
    float floating = 10.9f;
    printf("\nFloating point = %f", floating);

    // Declare and initialize a char variable
    char character = 'z';
    printf("\nCharacter = %c", character);

    // Declare variables without initialization
    int integer2;
    double double2;

    // Print the memory size of an integer and a double
    printf("\nInteger size (bytes) = %zu", sizeof(integer2));
    printf("\nDouble size (bytes) = %zu", sizeof(double2));

    return 0;                       // Indicate successful program execution
}