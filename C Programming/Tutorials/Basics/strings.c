#include <stdio.h>
#include <string.h> // Include string manipulation functions

/*
 * This program demonstrates string operations in C.
 * Examples include:
 * - Initialising and printing strings.
 * - Using standard string functions like strlen, strcpy, strcat, and strcmp.
 * - Modifying and copying strings.
 */

int main() {
    // Example 1: Initialising and Printing Strings
    printf("=== String Initialisation and Printing ===\n");
    char greeting[] = "Hello, World!";
    printf("Greeting: %s\n", greeting);
    printf("Length of greeting: %zu\n", strlen(greeting));

    // Example 2: Copying a String
    printf("\n=== Copying a String ===\n");
    char original[] = "C Programming";
    char copy[50]; // Ensure destination is large enough
    strcpy(copy, original);
    printf("Original: %s\n", original);
    printf("Copied: %s\n", copy);

    // Example 3: Concatenating Strings
    printf("\n=== Concatenating Strings ===\n");
    char firstPart[50] = "Hello";
    char secondPart[] = " there!";
    strcat(firstPart, secondPart);
    printf("Concatenated string: %s\n", firstPart);

    // Example 4: Comparing Strings
    printf("\n=== Comparing Strings ===\n");
    char str1[] = "apple";
    char str2[] = "banana";
    int comparison = strcmp(str1, str2);
    if (comparison == 0) {
        printf("'%s' and '%s' are equal.\n", str1, str2);
    } else if (comparison < 0) {
        printf("'%s' comes before '%s' in lexicographic order.\n", str1, str2);
    } else {
        printf("'%s' comes after '%s' in lexicographic order.\n", str1, str2);
    }

    return 0; // Indicate successful program execution
}
