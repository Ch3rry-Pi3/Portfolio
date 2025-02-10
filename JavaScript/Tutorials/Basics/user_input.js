/**
 * Shows basic usage of user input in JavaScript.
 * 
 * Uses the `prompt` method to capture input from the user.
 * Note: The `prompt` function works in browser environments, not Node.js.
 */
function basicInput() {
    const name = prompt("What is your name?");
    console.log(`Hello, ${name}!`); // Greets the user by name.
}
basicInput();

/**
 * Shows that user input can be stored and printed.
 */
function storingInput() {
    const favouriteColor = prompt("What is your favourite color?");
    console.log(`Your favourite color is: ${favouriteColor}`); // Prints the stored input.
}
storingInput();

/**
 * Shows converting user input to an integer using `parseInt`.
 * 
 * Highlights that `parseInt` ignores anything after the first non-numeric character.
 */
function parseIntConversion() {
    const ageInput = prompt("Enter your age (as a whole number):");
    const age = parseInt(ageInput, 10); // Converts the input to an integer.
    console.log(`Your age is: ${age}`); // Outputs the converted integer.

    // Example: Inputting "25.5" results in 25.
    console.log("Note: Decimals are ignored by parseInt.");
}
parseIntConversion();

/**
 * Shows how a decimal number loses its fractional part with `parseInt`.
 * 
 * Corrects this issue using `parseFloat`.
 */
function parseFloatConversion() {
    const decimalInput = prompt("Enter a decimal number (e.g., 25.5):");
    const asInteger = parseInt(decimalInput, 10); // Converts to integer, truncating the decimal part.
    const asFloat = parseFloat(decimalInput); // Converts to a floating-point number.

    console.log(`As an integer: ${asInteger}`); // Output: Integer part only.
    console.log(`As a floating-point number: ${asFloat}`); // Output: Full decimal number.

    // Example: Inputting "25.5" results in:
    // As an integer: 25
    // As a floating-point number: 25.5
}
parseFloatConversion();

/**
 * Shows how to use parseFloat to handle decimal values in calculations.
 */
function decimalCorrection() {
    const num1 = parseFloat(prompt("Enter the first decimal number:"));
    const num2 = parseFloat(prompt("Enter the second decimal number:"));

    const sum = num1 + num2;
    console.log(`The sum of ${num1} and ${num2} is: ${sum}`); // Outputs the correct sum of decimals.

    // Example: Inputting "1.5" and "2.3" results in:
    // The sum of 1.5 and 2.3 is: 3.8
}
decimalCorrection();