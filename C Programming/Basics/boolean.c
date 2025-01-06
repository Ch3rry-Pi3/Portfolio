#include <stdio.h>
#include <stdbool.h> // Include for Boolean values in C

/*
 * This program demonstrates the usage of Boolean values in C.
 * It includes examples of:
 * - Boolean variable declaration and initialization
 * - Implicit type conversion between integers and Booleans
 * - Logical operators (AND, OR, NOT)
 */

void boolean_examples() {
    // Declare Boolean variables using <stdbool.h>
    bool isRaining = true;  // true is defined in <stdbool.h>
    bool isSunny = false;   // false is defined in <stdbool.h>

    // Print the Boolean values
    printf("Is it raining? %s\n", isRaining ? "true" : "false");
    printf("Is it sunny? %s\n", isSunny ? "true" : "false");

    // Logical AND (&&) operation
    bool stayIndoors = isRaining && !isSunny;
    printf("Should we stay indoors? %s\n", stayIndoors ? "true" : "false");

    // Logical OR (||) operation
    bool goOutside = isSunny || !isRaining;
    printf("Can we go outside? %s\n", goOutside ? "true" : "false");

    // Logical NOT (!) operation
    printf("Is it NOT raining? %s\n", !isRaining ? "true" : "false");
}

void boolean_type_conversion_examples() {
    // Boolean values implicitly converted from integers
    int value1 = 0;  // Equivalent to false
    int value2 = 42; // Any non-zero value is equivalent to true

    // Print the Boolean conversion results
    printf("Value1 (0) as Boolean: %s\n", value1 ? "true" : "false");
    printf("Value2 (42) as Boolean: %s\n", value2 ? "true" : "false");

    // Convert Boolean back to integers
    bool isTrue = true;
    bool isFalse = false;

    printf("Boolean true as integer: %d\n", isTrue);
    printf("Boolean false as integer: %d\n", isFalse);
}

int main() {
    // Demonstrate Boolean usage and logical operations
    printf("=== Boolean Examples ===\n");
    boolean_examples();

    // Demonstrate type conversion with Boolean values
    printf("\n=== Boolean Type Conversion Examples ===\n");
    boolean_type_conversion_examples();

    return 0; // Indicate successful program execution
}
