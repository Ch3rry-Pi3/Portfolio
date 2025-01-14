#include <stdio.h>

/*
 * This program demonstrates variable scope in C.
 * Examples include:
 * - Local variables (specific to functions).
 * - Global variables (shared across all functions).
 * - Shadowing (when a local variable overrides a global variable in scope).
 */

// Global variable declaration
int global_counter = 0;

// Function prototype for incrementing a local counter
void increment_local_counter();

// Function prototype for incrementing the global counter
void increment_global_counter();

int main() {
    // Example 1: Using a local variable
    printf("=== Local Variable Scope ===\n");
    increment_local_counter(); // Call 1
    increment_local_counter(); // Call 2

    // Example 2: Using a global variable
    printf("\n=== Global Variable Scope ===\n");
    increment_global_counter(); // Call 1
    increment_global_counter(); // Call 2

    // Example 3: Shadowing a global variable
    printf("\n=== Shadowing Global Variable ===\n");
    int local_counter = 100; // Local variable shadows the global variable
    printf("Inside main, local_counter = %d (local variable)\n", local_counter);
    printf("Accessing true global_counter = %d (global variable)\n", global_counter);

    return 0; // Indicate successful program execution
}

// Function to increment a local counter
void increment_local_counter() {
    int local_counter = 0; // Local variable, initialized on every function call
    local_counter++;
    printf("Local counter: %d\n", local_counter);
}

// Function to increment the global counter
void increment_global_counter() {
    global_counter++; // Modify the global variable
    printf("Global counter: %d\n", global_counter);
}
