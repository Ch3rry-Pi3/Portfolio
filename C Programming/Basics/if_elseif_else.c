#include <stdio.h>

/*
 * This program demonstrates the use of `if`, `else if`, and `else` statements in C.
 * Examples include:
 * - Checking a number's properties (positive, negative, or zero).
 * - Grading system based on percentage.
 * - Nested conditions for a weather decision.
 */

void check_number_properties(int number) {
    // Check if the number is positive, negative, or zero
    if (number > 0) {
        printf("The number %d is positive.\n", number);
    } else if (number < 0) {
        printf("The number %d is negative.\n", number);
    } else {
        printf("The number is zero.\n");
    }
}

void grading_system(int percentage) {
    // Assign a grade based on percentage
    if (percentage >= 90) {
        printf("Grade: A\n");
    } else if (percentage >= 75) {
        printf("Grade: B\n");
    } else if (percentage >= 50) {
        printf("Grade: C\n");
    } else {
        printf("Grade: F\n");
    }
}

void weather_decision(int temperature, int isRaining) {
    // Nested conditions for weather-based decisions
    if (temperature > 30) {
        if (isRaining) {
            printf("It's hot and raining. Stay indoors.\n");
        } else {
            printf("It's hot outside. Wear light clothing.\n");
        }
    } else if (temperature >= 15) {
        if (isRaining) {
            printf("It's mild and raining. Carry an umbrella.\n");
        } else {
            printf("The weather is pleasant. Enjoy your day!\n");
        }
    } else {
        printf("It's cold. Wear a jacket.\n");
    }
}

int main() {
    // Example 1: Check properties of a number
    printf("=== Check Number Properties ===\n");
    check_number_properties(5);
    check_number_properties(-8);
    check_number_properties(0);

    // Example 2: Grading system
    printf("\n=== Grading System ===\n");
    grading_system(92); // Grade A
    grading_system(78); // Grade B
    grading_system(55); // Grade C
    grading_system(40); // Grade F

    // Example 3: Weather decision
    printf("\n=== Weather Decision ===\n");
    weather_decision(32, 1); // Hot and raining
    weather_decision(20, 0); // Pleasant weather
    weather_decision(10, 0); // Cold weather

    return 0; // Indicate successful program execution
}