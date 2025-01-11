#include <stdio.h>

/*
 * This program demonstrates the usage of the `while` loop in C.
 * Examples include:
 * - Simple counting.
 * - Summing numbers until a certain value.
 * - Checking for a condition and using `break` to exit the loop.
 */

void count_to_n(int n) {
    // Print numbers from 1 to n
    int counter = 1; // Initialise counter
    printf("Counting from 1 to %d:\n", n);
    while (counter <= n) {
        printf("%d ", counter);
        counter++; // Increment counter
    }
    printf("\n");
}

void sum_numbers(int limit) {
    // Calculate the sum of numbers from 1 to `limit`
    int sum = 0;  // Initialise sum
    int number = 1;  // Initialise number
    while (number <= limit) {
        sum += number; // Add current number to sum
        number++; // Increment number
    }
    printf("The sum of numbers from 1 to %d is: %d\n", limit, sum);
}

void break_on_condition(int max_attempts) {
    // Simulate user input and exit the loop if a condition is met
    int attempts = 0; // Initialise attempts
    int userInput;
    printf("Enter numbers. Enter -1 to exit (max attempts: %d):\n", max_attempts);
    while (attempts < max_attempts) {
        printf("Attempt %d: ", attempts + 1);
        scanf("%d", &userInput);
        if (userInput == -1) {
            printf("Exit condition met. Exiting the loop.\n");
            break; // Exit the loop
        }
        attempts++; // Increment attempts
    }
    if (attempts == max_attempts) {
        printf("Maximum attempts reached. Exiting the loop.\n");
    }
}

int main() {
    // Example 1: Counting numbers
    printf("=== Counting ===\n");
    count_to_n(10);

    // Example 2: Summing numbers
    printf("\n=== Summing Numbers ===\n");
    sum_numbers(10);

    // Example 3: Breaking on a condition
    printf("\n=== Break on Condition ===\n");
    break_on_condition(5);

    return 0; // Indicate successful program execution
}