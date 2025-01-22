#include <stdio.h>

/*
 * This program demonstrates the use of enums in C.
 * Examples include:
 * - Defining an enum for shoe sizes.
 * - Assigning enum values to variables.
 * - Printing enum variables as integers.
 * - Using a function to display the shoe size as text.
 */

// Step 1: Define an enumeration for Shoe Sizes
enum ShoeSize {
    Small = 5,    // Starts from size 5
    Medium = 7,   // Assigns 7 explicitly
    Large = 9,    // Assigns 9 explicitly
    ExtraLarge = 11  // Assigns 11 explicitly
};

// Function prototype to display shoe size as a string
void printShoeSize(enum ShoeSize size);

int main() {
    // Step 2: Declare variables of type `enum ShoeSize`
    printf("=== Enum Example: Shoe Sizes ===\n");
    enum ShoeSize mySize = Medium;
    enum ShoeSize friendSize = Large;
    enum ShoeSize anotherPersonSize = ExtraLarge;

    // Step 3: Print the integer values of the enums
    printf("Integer value of Small: %d\n", Small);
    printf("Integer value of Medium: %d\n", Medium);
    printf("Integer value of Large: %d\n", Large);
    printf("Integer value of ExtraLarge: %d\n", ExtraLarge);

    // Step 4: Print the shoe size using a function
    printf("\n=== Displaying Shoe Sizes as Strings ===\n");
    printShoeSize(mySize);
    printShoeSize(friendSize);
    printShoeSize(anotherPersonSize);

    return 0; // Indicate successful execution
}

// Function to print shoe size as a readable string
void printShoeSize(enum ShoeSize size) {
    printf("Shoe size selected: ");
    switch (size) {
        case Small:
            printf("Small (Size 5)\n");
            break;
        case Medium:
            printf("Medium (Size 7)\n");
            break;
        case Large:
            printf("Large (Size 9)\n");
            break;
        case ExtraLarge:
            printf("Extra Large (Size 11)\n");
            break;
        default:
            printf("Unknown Size\n");
    }
}
