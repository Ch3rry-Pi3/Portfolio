#include <stdio.h>

/*
 * This program demonstrates basic user input and output operations in C.
 * 
 * Author: [Your Name]
 * Date: [Date]
 * 
 * Description:
 * - The program prompts the user to input their age (integer), a double value, 
 *   and a character. 
 * - It uses `scanf` to read user inputs and stores them in respective variables.
 * - It then displays the entered values using `printf`.
 * 
 * Key Concepts:
 * - Using `scanf` for input and referencing variable addresses with `&`.
 * - Format specifiers for different data types:
 *   - `%d` for integers
 *   - `%lf` for double-precision floating-point numbers
 *   - `%c` for characters
 * - Understanding how to handle newline characters when using `scanf`.
 */

int main() {
    int age;                        // Declare an integer variable to store the user's age
    double number;                  // Declare a double variable to store a floating-point number
    char alphabet;                  // Declare a character variable to store a single character

    // Prompt the user for their age
    printf("What is your age? ");
    scanf("%d", &age);              // Read the user's input and store it in the variable 'age'

    // Display the entered age (Note: '$%d' has been corrected to '%d')
    printf("\nAge = %d", age);

    // Prompt the user to enter a double value
    printf("\nEnter double input: ");
    scanf("%lf", &number);          // Read the user's input and store it in the variable 'number'

    // Prompt the user to enter a character
    printf("\nEnter a character: ");
    scanf(" %c", &alphabet);        // Read the user's input and store it in the variable 'alphabet'

    // Display the entered double value and character
    printf("\nNumber: %lf", number);
    printf("\nCharacter: %c", alphabet);

    return 0; 
}
