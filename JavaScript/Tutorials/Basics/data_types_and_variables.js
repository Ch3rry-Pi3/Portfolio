/**
 * Shows the use of strings in JavaScript.
 * 
 * Strings are sequences of characters used to represent text.
 * You can use single or double quotes to define a string.
 */
function strings() {
    const greeting = "Hello, World!";
    const singleQuoteExample = 'JavaScript is fun!';
    console.log(greeting); // Output: Hello, World!
    console.log(singleQuoteExample); // Output: JavaScript is fun!
}
strings();

/**
 * Shows the use of numbers in JavaScript.
 * 
 * JavaScript has only one number type, used for integers and floating-point numbers.
 */
function numbers() {
    const integer = 42;
    const floatingPoint = 3.14;
    console.log(integer); // Output: 42
    console.log(floatingPoint); // Output: 3.14
}
numbers();

/**
 * Shows the creation and printing of variables.
 * Highlights the advantages of `let` over `var`.
 */
function variables() {
    // Using `let` allows block-scoping, unlike `var`.
    let message = "This is a let variable.";
    console.log(message); // Output: This is a let variable.

    if (true) {
        let blockScoped = "Accessible only in this block.";
        console.log(blockScoped); // Output: Accessible only in this block.
    }

    // Uncommenting the next line will throw a ReferenceError.
    // console.log(blockScoped);
}
variables();

/**
 * Shows assigning one variable value to another.
 */
function variableAssignment() {
    let original = 10;
    let copy = original;
    console.log(copy); // Output: 10

    original = 20; // Changing original doesn't affect the copy.
    console.log(copy); // Output: 10
}
variableAssignment();

/**
 * Shows the use of constant variables.
 * 
 * Constants are immutable and cannot be reassigned after their initial declaration.
 */
function constants() {
    const pi = 3.14159;
    console.log(`Value of pi: ${pi}`); // Output: Value of pi: 3.14159

    // Uncommenting the next line will throw a TypeError.
    // pi = 3.15;
}
constants();

/**
 * Shows the `undefined` keyword in JavaScript.
 * 
 * `undefined` is the default value for uninitialized variables.
 */
function undefinedKeyword() {
    let uninitialized;
    console.log(uninitialized); // Output: undefined
}
undefinedKeyword();

/**
 * Shows concatenating strings and variables.
 */
function stringConcatenation() {
    const city = "New York";

    // Using traditional string concatenation.
    console.log("City: " + city); // Output: City: New York

    // Using template literals (preferred method).
    console.log(`City: ${city}`); // Output: City: New York
}
stringConcatenation();

/**
 * Shows other data types in JavaScript.
 */
function otherDataTypes() {
    const booleanExample = true;
    const nullExample = null; // Represents the intentional absence of any value.
    const arrayExample = [1, 2, 3, 4, 5];
    const objectExample = { name: "Alice", age: 30 };

    console.log(booleanExample); // Output: true
    console.log(nullExample); // Output: null
    console.log(arrayExample); // Output: [1, 2, 3, 4, 5]
    console.log(objectExample); // Output: { name: "Alice", age: 30 }
}
otherDataTypes();

/**
 * Shows dynamic typing in JavaScript.
 * 
 * JavaScript variables can hold values of any type, and their types can change.
 */
function dynamicTyping() {
    let dynamicVariable = "I am a string.";
    console.log(dynamicVariable); // Output: I am a string.

    dynamicVariable = 42; // Now it's a number.
    console.log(dynamicVariable); // Output: 42
}
dynamicTyping();

/**
 * Shows type coercion in JavaScript.
 * 
 * JavaScript automatically converts values between types when necessary.
 */
function typeCoercion() {
    const coercedValue = "5" * 2; // String "5" is coerced into a number.
    console.log(coercedValue); // Output: 10

    const concatenatedValue = "5" + 2; // Number 2 is coerced into a string.
    console.log(concatenatedValue); // Output: 52
}
typeCoercion();