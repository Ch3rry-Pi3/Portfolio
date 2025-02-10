/**
 * Shows the use of boolean values in JavaScript.
 * 
 * Booleans represent logical values: `true` or `false`.
 */
function booleans() {
    const isSunny = true;
    const isRaining = false;

    console.log(`Is it sunny? ${isSunny}`); // Output: Is it sunny? true
    console.log(`Is it raining? ${isRaining}`); // Output: Is it raining? false

    // Booleans are often used in conditional statements.
    if (isSunny) {
        console.log("It's a sunny day!"); // Output: It's a sunny day!
    } else {
        console.log("It's not sunny.");
    }
}
booleans();

/**
 * Shows comparison operators in JavaScript.
 * 
 * Includes equality, strict equality, inequality, greater than, less than, and others.
 */
function comparisonOperators() {
    const a = 10;
    const b = 20;
    const c = "10";

    console.log(`a == c: ${a == c}`); // Output: true (loose equality, type coercion)
    console.log(`a === c: ${a === c}`); // Output: false (strict equality, no type coercion)

    console.log(`a != b: ${a != b}`); // Output: true
    console.log(`a !== c: ${a !== c}`); // Output: true

    console.log(`a > b: ${a > b}`); // Output: false
    console.log(`a < b: ${a < b}`); // Output: true

    console.log(`a >= 10: ${a >= 10}`); // Output: true
    console.log(`b <= 15: ${b <= 15}`); // Output: false
}
comparisonOperators();

/**
 * Shows logical operators in JavaScript.
 * 
 * Includes AND (&&), OR (||), and NOT (!).
 */
function logicalOperators() {
    const hasDriverLicense = true;
    const knowsHowToDrive = false;

    // Logical AND (&&): Both conditions must be true.
    console.log(`Can drive: ${hasDriverLicense && knowsHowToDrive}`); // Output: false

    // Logical OR (||): At least one condition must be true.
    console.log(`Can apply for driving lessons: ${hasDriverLicense || knowsHowToDrive}`); // Output: true

    // Logical NOT (!): Negates a condition.
    console.log(`Does not have a driver's license: ${!hasDriverLicense}`); // Output: false
}
logicalOperators();

/**
 * Combines comparison and logical operators in conditional statements.
 * 
 * Demonstrates how to use these operators together.
 */
function combinedOperators() {
    const age = 25;
    const hasID = true;

    // Example: Age verification with logical AND.
    if (age >= 18 && hasID) {
        console.log("Access granted."); // Output: Access granted.
    } else {
        console.log("Access denied.");
    }

    // Example: Age verification with logical OR.
    const isChild = age < 13 || !hasID;
    console.log(`Is the person a child or without ID? ${isChild}`); // Output: false
}
combinedOperators();

/**
 * Demonstrates truthy and falsy values in JavaScript.
 * 
 * JavaScript treats certain values as "truthy" or "falsy" in logical operations.
 */
function truthyFalsyValues() {
    console.log(`Truthy (non-empty string): ${!!"Hello"}`); // Output: true
    console.log(`Falsy (empty string): ${!!""}`); // Output: false
    console.log(`Truthy (non-zero number): ${!!42}`); // Output: true
    console.log(`Falsy (zero): ${!!0}`); // Output: false
    console.log(`Falsy (null): ${!!null}`); // Output: false
    console.log(`Falsy (undefined): ${!!undefined}`); // Output: false
    console.log(`Truthy (array): ${!![1, 2, 3]}`); // Output: true
}
truthyFalsyValues();