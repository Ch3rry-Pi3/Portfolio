#include <stdio.h>
#include <string.h> // Include string functions

/*
 * This program demonstrates various C string functions.
 * Examples include:
 * - Finding string length using `strlen`
 * - Copying strings using `strcpy` and `strncpy`
 * - Concatenating strings using `strcat` and `strncat`
 * - Comparing strings using `strcmp` and `strncmp`
 * - Finding characters and substrings using `strchr` and `strstr`
 * - Tokenizing strings using `strtok`
 */

int main() {
    // Example 1: Getting the length of a string
    printf("=== String Length (`strlen`) ===\n");
    char text[] = "Hello, World!";
    printf("String: %s\n", text);
    printf("Length: %zu\n", strlen(text));

    // Example 2: Copying a string
    printf("\n=== Copying Strings (`strcpy` and `strncpy`) ===\n");
    char original[] = "C Programming";
    char copy[50]; 
    strcpy(copy, original); // Copy entire string
    printf("Copied using `strcpy`: %s\n", copy);

    char partial_copy[10];
    strncpy(partial_copy, original, 9); // Copy only 9 characters
    partial_copy[9] = '\0'; // Ensure null termination
    printf("Copied using `strncpy`: %s\n", partial_copy);

    // Example 3: Concatenating strings
    printf("\n=== Concatenating Strings (`strcat` and `strncat`) ===\n");
    char first[50] = "Hello";
    char second[] = " there!";
    strcat(first, second); // Append second to first
    printf("Concatenated string: %s\n", first);

    char limited[50] = "Hello";
    strncat(limited, second, 3); // Append only first 3 characters of `second`
    printf("Partially concatenated string: %s\n", limited);

    // Example 4: Comparing strings
    printf("\n=== Comparing Strings (`strcmp` and `strncmp`) ===\n");
    char str1[] = "apple";
    char str2[] = "banana";
    int cmp = strcmp(str1, str2);
    printf("Comparing '%s' and '%s': %d\n", str1, str2, cmp);

    char prefix1[] = "apple";
    char prefix2[] = "apricot";
    int cmp2 = strncmp(prefix1, prefix2, 3); // Compare only first 3 characters
    printf("Comparing first 3 characters of '%s' and '%s': %d\n", prefix1, prefix2, cmp2);

    // Example 5: Finding a character in a string
    printf("\n=== Finding Characters in a String (`strchr`) ===\n");
    char *ch = strchr(text, 'W'); // Find 'W' in "Hello, World!"
    if (ch) {
        printf("Character 'W' found at position: %ld\n", ch - text);
    } else {
        printf("Character not found.\n");
    }

    // Example 6: Finding a substring in a string
    printf("\n=== Finding a Substring (`strstr`) ===\n");
    char *sub = strstr(text, "World"); // Find "World" in "Hello, World!"
    if (sub) {
        printf("Substring 'World' found at position: %ld\n", sub - text);
    } else {
        printf("Substring not found.\n");
    }

    // Example 7: Tokenizing a string
    printf("\n=== Tokenizing Strings (`strtok`) ===\n");
    char sentence[] = "C is a powerful programming language.";
    char *token = strtok(sentence, " "); // Split by space
    while (token != NULL) {
        printf("Token: %s\n", token);
        token = strtok(NULL, " "); // Get next token
    }

    return 0; // Indicate successful execution
}
