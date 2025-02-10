#include <stdio.h>

/*
 * This program demonstrates both implicit and explicit type conversions in C.
 * 
 * - Implicit Type Conversion:
 *   Occurs automatically when variables of different data types are used in the same expression.
 *   Examples include conversions from lower to higher data types in arithmetic operations.
 * 
 * - Explicit Type Conversion:
 *   Performed manually using type casting to convert a variable to a specific data type.
 */

void implicit_conversion_examples() {
    // Implicit Conversion Examples

    // Declare integer variables and perform addition
    int a = 5;
    int b = 9;
    int result = a + b;
    printf("Result (int + int): %d\n", result);

    // Declare a char and an integer, then add them
    char c = '5';
    int d = 9;
    int result2 = c + d; // '5' (char) is implicitly converted to its ASCII value (53)
    printf("Result2 (char + int): %d\n", result2);

    // Declare a double and an integer, then add them
    double e = 5.67;
    int f = 9;
    int result3 = e + f; // 'f' is converted to double, but the result is cast back to int
    printf("Result3 (double + int, stored as int): %d\n", result3);

    // Declare a double and an integer, then add them with the result stored as double
    double g = 5.67;
    int h = 9;
    double result4 = g + h; // 'h' is converted to double
    printf("Result4 (double + int, stored as double): %lf\n", result4);
}

void explicit_conversion_examples() {
    // Explicit Conversion Examples

    // Convert a double to an integer
    double x = 7.89;
    int y = (int)x; // Cast double to int, truncating the fractional part
    printf("Explicit Conversion (double to int): %d\n", y);

    // Convert an integer to a double
    int p = 12;
    double q = (double)p; // Cast int to double for precise division
    printf("Explicit Conversion (int to double): %.2lf\n", q);

    // Force integer division to perform floating-point division
    int m = 5, n = 2;
    double result = (double)m / n; // Cast numerator to double
    printf("Explicit Conversion (int to double for division): %.2lf\n", result);

    // Mix data types in arithmetic
    float r = 3.14f;
    int s = 2;
    double result2 = (double)r * s; // Cast float to double for higher precision
    printf("Explicit Conversion (float to double): %.6lf\n", result2);
}

int main() {
    // Display implicit conversion examples
    printf("=== Implicit Type Conversion Examples ===\n");
    implicit_conversion_examples();

    // Display explicit conversion examples
    printf("\n=== Explicit Type Conversion Examples ===\n");
    explicit_conversion_examples();

    return 0; // Indicate successful program execution
}