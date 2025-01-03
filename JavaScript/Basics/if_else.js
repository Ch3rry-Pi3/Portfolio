/**
 * Demonstrates a simple `if` statement in JavaScript.
 * 
 * Executes the block only if the condition evaluates to `true`.
 */
function simpleIfStatement() {
    const temperature = 25;

    if (temperature > 20) {
        console.log("It's warm outside!"); // Output: It's warm outside!
    }
}
simpleIfStatement();

/**
 * Demonstrates a simple `if...else` statement in JavaScript.
 * 
 * Executes one block if the condition is `true`, another block if `false`.
 */
function simpleIfElseStatement() {
    const isRaining = true;

    if (isRaining) {
        console.log("Don't forget your umbrella!"); // Output: Don't forget your umbrella!
    } else {
        console.log("Enjoy the sunshine!");
    }
}
simpleIfElseStatement();

/**
 * Demonstrates multiple conditions using `if...else if...else` statements.
 * 
 * Executes different blocks based on which condition is `true`.
 */
function multipleConditions() {
    const score = 85;

    if (score >= 90) {
        console.log("Grade: A");
    } else if (score >= 80) {
        console.log("Grade: B"); // Output: Grade: B
    } else if (score >= 70) {
        console.log("Grade: C");
    } else if (score >= 60) {
        console.log("Grade: D");
    } else {
        console.log("Grade: F");
    }
}
multipleConditions();

/**
 * Demonstrates nested `if` statements in JavaScript.
 * 
 * Useful for checking multiple related conditions.
 */
function nestedIfStatements() {
    const age = 30;
    const hasTicket = true;

    if (age >= 18) {
        if (hasTicket) {
            console.log("You may enter the event."); // Output: You may enter the event.
        } else {
            console.log("You need a ticket to enter.");
        }
    } else {
        console.log("You must be 18 or older to enter.");
    }
}
nestedIfStatements();

/**
 * Demonstrates the use of logical operators with `if...else` statements.
 * 
 * Combines conditions using `&&` and `||`.
 */
function logicalOperatorsInIfElse() {
    const isWeekend = true;
    const isHoliday = false;

    if (isWeekend || isHoliday) {
        console.log("You can relax today!"); // Output: You can relax today!
    } else {
        console.log("It's a working day.");
    }
}
logicalOperatorsInIfElse();

/**
 * Demonstrates handling edge cases with `if...else` statements.
 * 
 * Ensures conditions account for all possible scenarios.
 */
function edgeCaseHandling() {
    const value = null;

    if (value === null) {
        console.log("The value is null."); // Output: The value is null.
    } else if (value === undefined) {
        console.log("The value is undefined.");
    } else if (value === 0) {
        console.log("The value is zero.");
    } else {
        console.log("The value is something else.");
    }
}
edgeCaseHandling();

/**
 * Demonstrates combining conditions in a compact `if...else` statement.
 * 
 * Uses ternary operators for simpler conditions.
 */
function compactIfElse() {
    const age = 16;

    const message = age >= 18 ? "You are an adult." : "You are a minor.";
    console.log(message); // Output: You are a minor.
}
compactIfElse();