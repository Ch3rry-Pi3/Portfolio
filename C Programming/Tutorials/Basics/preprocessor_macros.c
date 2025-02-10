#include <stdio.h>

// Step 1: Define simple macros
#define PI 3.14159
#define MAX_SIZE 10

// Step 2: Define a macro function to calculate the square of a number
#define SQUARE(x) ((x) * (x))

// Step 3: Conditional compilation macros
#define DEBUG_MODE // Uncomment to enable debugging

// Step 4: Using predefined macros
#define SHOW_INFO() printf("Compiled in file: %s, Line: %d\n", __FILE__, __LINE__)

// Step 5: Macro for conditional inclusion
#ifndef APP_VERSION
#define APP_VERSION "1.0.0"
#endif

int main() {
    // Example 1: Using simple macros
    printf("=== Using Simple Macros ===\n");
    printf("Value of PI: %.5f\n", PI);
    printf("Maximum size: %d\n", MAX_SIZE);

    // Example 2: Using a macro function
    printf("\n=== Using Macro Functions ===\n");
    int num = 5;
    printf("Square of %d: %d\n", num, SQUARE(num));

    // Example 3: Using predefined macros
    printf("\n=== Using Predefined Macros ===\n");
    SHOW_INFO(); // Prints file name and line number

    // Example 4: Conditional compilation
    printf("\n=== Conditional Compilation ===\n");
#ifdef DEBUG_MODE
    printf("Debug mode is enabled!\n");
#else
    printf("Debug mode is disabled.\n");
#endif

    // Example 5: Using macros for version control
    printf("\n=== Application Version ===\n");
    printf("Application Version: %s\n", APP_VERSION);

    return 0;
}
