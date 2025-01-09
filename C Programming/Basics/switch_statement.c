#include <stdio.h>

/*
 * This program demonstrates the usage of the `switch` statement in C.
 * It includes:
 * - Determining the day of the week.
 * - Performing basic arithmetic operations.
 * - Checking if a character is a vowel or consonant (grouped cases).
 */

void day_of_week(int day) {
    // Use switch to determine the day of the week
    switch (day) {
        case 1:
            printf("Monday\n");
            break;
        case 2:
            printf("Tuesday\n");
            break;
        case 3:
            printf("Wednesday\n");
            break;
        case 4:
            printf("Thursday\n");
            break;
        case 5:
            printf("Friday\n");
            break;
        case 6:
            printf("Saturday\n");
            break;
        case 7:
            printf("Sunday\n");
            break;
        default:
            printf("Invalid day: %d. Please enter a value between 1 and 7.\n", day);
    }
}

void calculator(char operator, int num1, int num2) {
    // Use switch to perform basic arithmetic operations
    switch (operator) {
        case '+':
            printf("Result: %d + %d = %d\n", num1, num2, num1 + num2);
            break;
        case '-':
            printf("Result: %d - %d = %d\n", num1, num2, num1 - num2);
            break;
        case '*':
            printf("Result: %d * %d = %d\n", num1, num2, num1 * num2);
            break;
        case '/':
            if (num2 != 0) {
                printf("Result: %d / %d = %.2f\n", num1, num2, (double)num1 / num2);
            } else {
                printf("Error: Division by zero is not allowed.\n");
            }
            break;
        default:
            printf("Invalid operator '%c'. Please use +, -, *, or /.\n", operator);
    }
}

void vowel_or_consonant(char letter) {
    // Use switch to determine if a character is a vowel or consonant
    switch (letter) {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
        case 'A':
        case 'E':
        case 'I':
        case 'O':
        case 'U':
            printf("The letter '%c' is a vowel.\n", letter);
            break;
        default:
            printf("The letter '%c' is a consonant.\n", letter);
    }
}

int main() {
    // Example 1: Determine the day of the week
    printf("=== Day of the Week ===\n");
    day_of_week(1);
    day_of_week(5);
    day_of_week(8);

    // Example 2: Basic calculator using switch
    printf("\n=== Basic Calculator ===\n");
    calculator('+', 10, 20);
    calculator('-', 15, 5);
    calculator('*', 6, 7);
    calculator('/', 42, 7);
    calculator('/', 42, 0);
    calculator('x', 42, 7);

    // Example 3: Check if a character is a vowel or consonant
    printf("\n=== Vowel or Consonant ===\n");
    vowel_or_consonant('a'); // Vowel
    vowel_or_consonant('E'); // Vowel
    vowel_or_consonant('z'); // Consonant
    vowel_or_consonant('H'); // Consonant

    return 0; // Indicate successful program execution
}
