#include <stdio.h>
#include <string.h> // Include string manipulation functions

/*
 * This program demonstrates string operations in C.
 * Examples include:
 * - Initializing and printing strings.
 * - Using standard string functions like strlen, strcpy, strcat, and strcmp.
 * - Taking string input from the user.
 * - Modifying and copying strings.
 */

int main() {
    // Example 1: Initializing and Printing Strings
    printf("=== String Initialization and Printing ===\n");
    char greeting[] = "Hello, World!";
    printf("Greeting: %s\n", greeting);
    printf("Length of greeting: %zu\n", strlen(greeting)); // Get string length

    // Example 2: Copying a String
    printf("\n=== Copying a String ===\n");
    char original[] = "C Programming";
    char copy[50]; // Ensure destination is large enough
    strcpy(copy, original); // Copy contents of original to copy
    printf("Original: %s\n", original);
    printf("Copied: %s\n", copy);

    // Example 3: Concatenating Strings
    printf("\n=== Concatenating Strings ===\n");
    char firstPart[50] = "Hello";
    char secondPart[] = " there!";
    strcat(firstPart, secondPart); // Append secondPart to firstPart
    printf("Concatenated string: %s\n", firstPart);

    // Example 4: Comparing Strings
    printf("\n=== Comparing Strings ===\n");
    char str1[] = "apple";
    char str2[] = "banana";
    int comparison = strcmp(str1, str2); // Compare str1 and str2
    if (comparison == 0) {
        printf("'%s' and '%s' are equal.\n", str1, str2);
    } else if (comparison < 0) {
        printf("'%s' comes before '%s' in lexicographic order.\n", str1, str2);
    } else {
        printf("'%s' comes after '%s' in lexicographic order.\n", str1, str2);
    }

    // Example 5: Taking String Input
    printf("\n=== Taking String Input ===\n");
    char userInput[50];
    printf("Enter your name: ");
    fgets(userInput, sizeof(userInput), stdin); // Read user input
    userInput[strcspn(userInput, "\n")] = '\0'; // Remove newline character
    printf("Hello, %s! Welcome to C programming.\n", userInput);

    return 0; // Indicate successful program execution
}
