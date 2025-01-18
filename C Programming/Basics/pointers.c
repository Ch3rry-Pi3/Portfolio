#include <stdio.h>

/*
 * This program demonstrates the basics of pointers in C.
 * Examples include:
 * - Declaring and initialising a pointer.
 * - Getting the memory address of a variable using `&`.
 * - Accessing the variable's value using a pointer with `*`.
 * - Modifying a variable using a pointer.
 */

int main() {
    // Step 1: Declare a variable
    int number = 42;
    printf("=== Declaring a Variable ===\n");
    printf("Value of 'number': %d\n", number);

    // Step 2: Get the memory address of the variable
    printf("\n=== Getting Memory Address Using `&` ===\n");
    printf("Memory address of 'number': %p\n", &number);

    // Step 3: Declare and initialise a pointer
    int *ptr = &number; // Pointer stores the address of 'number'
    printf("\n=== Initialising a Pointer ===\n");
    printf("Pointer 'ptr' stores address: %p\n", ptr);

    // Step 4: Access the value using the pointer
    printf("\n=== Accessing Value Using Pointer `*` ===\n");
    printf("Value at address stored in 'ptr': %d\n", *ptr);

    // Step 5: Modify the value using the pointer
    printf("\n=== Modifying Variable Using Pointer ===\n");
    *ptr = 100; // Modify 'number' via pointer
    printf("New value of 'number': %d\n", number);
    printf("Value accessed via pointer: %d\n", *ptr);

    return 0; // Indicate successful execution
}