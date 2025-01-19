#include <stdio.h>

/*
 * This program demonstrates pointers and arrays in C.
 * Examples include:
 * - Printing the memory address of an array.
 * - Printing the individual memory addresses of elements.
 * - Iterating through an array using pointers.
 * - Using pointer arithmetic to access array elements.
 */

int main() {
    // Step 1: Declare an array
    int numbers[] = {10, 20, 30, 40, 50};
    int size = sizeof(numbers) / sizeof(numbers[0]); // Number of elements in the array

    // Step 2: Print the memory address of the array
    printf("=== Memory Address of the Array ===\n");
    printf("Address of `numbers` array: %p\n", (void*)numbers);

    // Step 3: Print individual memory addresses of each element
    printf("\n=== Memory Addresses of Individual Elements ===\n");
    for (int i = 0; i < size; i++) {
        printf("Address of numbers[%d]: %p (Value: %d)\n", i, (void*)&numbers[i], numbers[i]);
    }

    // Step 4: Access elements using a pointer
    printf("\n=== Accessing Elements Using a Pointer ===\n");
    int *ptr = numbers; // Pointer to the first element of the array
    for (int i = 0; i < size; i++) {
        printf("Pointer at index %d: Address = %p, Value = %d\n", i, (void*)(ptr + i), *(ptr + i));
    }

    // Step 5: Pointer arithmetic
    printf("\n=== Pointer Arithmetic (Incrementing Pointer) ===\n");
    for (int i = 0; i < size; i++) {
        printf("*(ptr + %d) = %d\n", i, *(ptr + i)); // Equivalent to numbers[i]
    }

    return 0; // Indicate successful execution
}
