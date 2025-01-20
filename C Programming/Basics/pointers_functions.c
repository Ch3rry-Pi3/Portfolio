#include <stdio.h>

/*
 * This program demonstrates using pointers as function arguments in C.
 * Examples include:
 * - Passing a pointer to a function to modify a variable.
 * - Calculating the square of a number using a pointer.
 * - Swapping two numbers using pointers.
 */

// Function prototype to calculate the square (modifies original variable)
void square(int *num);

// Function prototype to swap two numbers using pointers
void swap(int *a, int *b);

int main() {
    // Example 1: Calculating the square of a number using a pointer
    printf("=== Calculating Square Using Pointers ===\n");
    int number = 5;
    printf("Original number: %d\n", number);
    square(&number); // Pass the address of the variable
    printf("Squared number: %d\n", number);

    // Example 2: Swapping two numbers using pointers
    printf("\n=== Swapping Two Numbers Using Pointers ===\n");
    int x = 10, y = 20;
    printf("Before swap: x = %d, y = %d\n", x, y);
    swap(&x, &y); // Pass the addresses of x and y
    printf("After swap: x = %d, y = %d\n", x, y);

    return 0; // Indicate successful execution
}

// Function definition: Calculates the square of a number using a pointer
void square(int *num) {
    *num = (*num) * (*num); // Modify the value at the pointer's address
}

// Function definition: Swaps two numbers using pointers
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
