#include <stdio.h>

/*
 * This program demonstrates basic concepts of variables in C programming.
 * 
 * Author: [Your Name]
 * Date: [Date]
 * 
 * Description:
 * - The program covers:
 *   1. Declaring variables and initialising them with values.
 *   2. Reassigning new values to variables after initialisation.
 *   3. Assigning the value of one variable to another variable.
 *   4. Printing variable values using the printf function.
 * - The program is a practical example for beginners to understand
 *   how variables are used and manipulated in C.
 * 
 * Key Concepts:
 * - Variable declaration and initialisation
 * - Variable reassignment
 * - Assigning one variable's value to another
 * - Outputting variables using format specifiers (%d for integers)
 */

int main() {

    // Declare and initialise a variable
    int age = 25;
    printf("Age: %d", age);

    // Reassign a new value to the variable
    age = 31;
    printf("\nNew age: %d", age);

    // Declare and initialise a variable
    int firstNumber = 33;
    printf("\n\nfirstNumber = %d", firstNumber);

    // Assign the value of one variable to another
    int secondNumber = firstNumber;
    printf("\nsecondNumber = %d", firstNumber);

    // Declare multiple variables and assign values
    int variable1, variable2 = 25;
    variable1 = 13;

    // Print the values of the variables
    printf("\n\nvariable1: %d", variable1);
    printf("\nvariable2: %d", variable2);
    
    return 0;                       // Indicate successful program execution
}
