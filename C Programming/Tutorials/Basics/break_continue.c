#include <stdio.h>

/*
 * This program demonstrates the usage of `break` and `continue` in C loops.
 * Examples include:
 * - Using `break` to exit a loop early when a condition is met.
 * - Using `continue` to skip specific iterations of a loop.
 */

void demonstrate_break(int limit) {
    // Print numbers from 1 to `limit`, but stop when the number is 5
    printf("Demonstrating `break`:\n");
    for (int i = 1; i <= limit; i++) {
        if (i == 5) {
            printf("Breaking out of the loop at %d.\n", i);
            break; // Exit the loop immediately
        }
        printf("%d ", i);
    }
    printf("\n");
}

void demonstrate_continue(int limit) {
    // Print numbers from 1 to `limit`, but skip multiples of 3
    printf("Demonstrating `continue`:\n");
    for (int i = 1; i <= limit; i++) {
        if (i % 3 == 0) {
            printf("Skipping %d (multiple of 3).\n", i);
            continue; // Skip the rest of this iteration
        }
        printf("%d ", i);
    }
    printf("\n");
}

int main() {
    // Example 1: Using `break` to exit a loop early
    printf("=== Example of `break` ===\n");
    demonstrate_break(10);

    // Example 2: Using `continue` to skip specific iterations
    printf("\n=== Example of `continue` ===\n");
    demonstrate_continue(10);

    return 0; // Indicate successful program execution
}
