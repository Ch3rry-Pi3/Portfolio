/**
 * Demonstrates basic usage of the ternary operator.
 * 
 * The ternary operator evaluates a condition and returns one of two values.
 */
function basicTernary() {
    const age = 20;

    // Simple ternary operator.
    age >= 18 
        ? console.log("You are an adult.") // Output: You are an adult.
        : console.log("You are a minor.");
}
basicTernary();

/**
 * Demonstrates assigning the result of a ternary operator to a variable.
 */
function ternaryAssignment() {
    const score = 75;

    // Assigning result to a variable.
    const grade = score >= 90 
        ? "A" 
        : score >= 80 
            ? "B" 
            : score >= 70 
                ? "C" 
                : score >= 60 
                    ? "D" 
                    : "F";

    console.log(`Your grade is: ${grade}`); // Output: Your grade is: C
}
ternaryAssignment();

/**
 * Demonstrates using the ternary operator with multiple conditions.
 */
function multipleConditions() {
    const isMember = true;
    const cartValue = 150;

    // Combining multiple conditions in a ternary operator.
    const discount = isMember 
        ? cartValue >= 100 
            ? 20 
            : 10 
        : 0;

    console.log(`Your discount is: ${discount}%`); // Output: Your discount is: 20%
}
multipleConditions();

/**
 * Demonstrates nested ternary operators for decision-making.
 */
function nestedTernary() {
    const temperature = 15;

    // Nested ternary for multiple outcomes.
    const weather = temperature > 30 
        ? "Hot" 
        : temperature > 20 
            ? "Warm" 
            : temperature > 10 
                ? "Cool" 
                : "Cold";

    console.log(`The weather is: ${weather}`); // Output: The weather is: Cool
}
nestedTernary();

/**
 * Demonstrates ternary operators for quick checks.
 */
function quickCheck() {
    const num = 7;

    // Checking if a number is even or odd.
    const parity = num % 2 === 0 ? "Even" : "Odd";
    console.log(`The number ${num} is ${parity}.`); // Output: The number 7 is Odd.

    // Checking if a string is empty.
    const str = "";
    const isEmpty = str === "" ? "String is empty." : "String is not empty.";
    console.log(isEmpty); // Output: String is empty.
}
quickCheck();