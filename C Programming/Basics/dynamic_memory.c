#include <stdio.h>
#include <stdlib.h> // Required for malloc, calloc, realloc, free

/*
 * This program demonstrates dynamic memory allocation in C.
 * Examples include:
 * - Allocating memory using `malloc` (single block).
 * - Allocating memory using `calloc` (multiple blocks with initialization).
 * - Resizing allocated memory using `realloc`.
 * - Freeing allocated memory using `free`.
 */

int main() {
    // Step 1: Allocating memory using malloc
    printf("=== Allocating Memory Using `malloc` ===\n");
    int *ptr = (int*) malloc(sizeof(int)); // Allocate memory for one integer
    if (ptr == NULL) {
        printf("Memory allocation failed!\n");
        return 1; // Exit program if allocation fails
    }
    *ptr = 42; // Assign a value
    printf("Value stored at allocated memory: %d\n", *ptr);

    // Step 2: Allocating memory using calloc
    printf("\n=== Allocating Memory Using `calloc` ===\n");
    int n = 5; // Number of elements
    int *arr = (int*) calloc(n, sizeof(int)); // Allocate array of 5 integers (all initialized to 0)
    if (arr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    printf("Allocated array elements (initialized to 0): ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Step 3: Resizing allocated memory using realloc
    printf("\n=== Resizing Memory Using `realloc` ===\n");
    n = 8; // Resize array to hold 8 integers
    arr = (int*) realloc(arr, n * sizeof(int));
    if (arr == NULL) {
        printf("Memory reallocation failed!\n");
        return 1;
    }
    printf("Array resized to %d elements.\n", n);

    // Assigning new values after reallocation
    for (int i = 5; i < n; i++) {
        arr[i] = i * 10;
    }
    printf("Updated array elements: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Step 4: Freeing allocated memory
    printf("\n=== Freeing Allocated Memory ===\n");
    free(ptr);  // Free single integer memory
    free(arr);  // Free array memory
    printf("Memory successfully freed.\n");

    return 0; // Indicate successful execution
}
