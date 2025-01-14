#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/*
 * This program demonstrates the usage of standard library functions in C.
 * Examples include:
 * - Input/output functions from <stdio.h>.
 * - Mathematical functions from <math.h>.
 * - String manipulation functions from <string.h>.
 * - Utility functions from <stdlib.h>.
 */

int main() {
    // Example 1: Input/Output (from <stdio.h>)
    printf("=== Input/Output Functions ===\n");
    char name[50];
    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin); // Read a string with spaces
    name[strcspn(name, "\n")] = '\0'; // Remove newline character
    printf("Hello, %s! Welcome to the program.\n", name);

    // Example 2: Mathematical Functions (from <math.h>)
    printf("\n=== Mathematical Functions ===\n");
    double number = 16.0;
    printf("Square root of %.2f is: %.2f\n", number, sqrt(number));

    // Example 3: String Manipulation (from <string.h>)
    printf("\n=== String Manipulation Functions ===\n");
    char str1[50] = "Hello";
    char str2[] = " World!";
    strcat(str1, str2); // Concatenate strings
    printf("Concatenated string: %s\n", str1);
    printf("Length of string '%s' is: %zu\n", str1, strlen(str1));

    // Example 4: Utility Functions (from <stdlib.h>)
    printf("\n=== Utility Functions ===\n");
    int random_number = rand() % 100; // Generate a random number between 0 and 99
    printf("Random number: %d\n", random_number);
    double value = -12.34;
    printf("Absolute value of %.2f is: %.2f\n", value, fabs(value));

    return 0; // Indicate successful program execution
}
