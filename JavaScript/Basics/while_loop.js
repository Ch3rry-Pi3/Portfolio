/**
 * Demonstrates a basic while loop.
 * 
 * Iterates as long as the condition is `true`.
 */
function basicWhileLoop() {
    let count = 1;

    while (count <= 5) {
        console.log(`Count is: ${count}`); // Output: Count is: 1, 2, 3, 4, 5
        count++;
    }
}
basicWhileLoop();

/**
 * Demonstrates a while loop with a condition-based exit.
 * 
 * Loops until a certain condition is met.
 */
function conditionBasedWhileLoop() {
    let number = 10;

    while (number > 0) {
        console.log(`Countdown: ${number}`); // Output: Countdown: 10, 9, 8...
        number--;
    }

    console.log("Blast off!"); // Output after loop ends: Blast off!
}
conditionBasedWhileLoop();

/**
 * Demonstrates an infinite loop with an explicit break condition.
 * 
 * The loop continues indefinitely until a specific condition triggers a `break`.
 */
function infiniteLoopWithBreak() {
    let attempts = 0;

    while (true) {
        attempts++;
        console.log(`Attempt ${attempts}`);

        if (attempts === 3) {
            console.log("Stopping the loop after 3 attempts."); // Output after 3 attempts.
            break;
        }
    }
}
infiniteLoopWithBreak();

/**
 * Demonstrates a while loop with user input (simulated).
 * 
 * Simulates user input using a predefined list of responses.
 */
function userInputSimulation() {
    const responses = ["yes", "no", "yes", "stop"];
    let i = 0;
    let input;

    while (input !== "stop") {
        input = responses[i++];
        console.log(`User input: ${input}`); // Output: User input: yes, no, yes, stop
    }

    console.log("Loop exited on 'stop'.");
}
userInputSimulation();

/**
 * Demonstrates a nested while loop.
 * 
 * Useful for handling multi-dimensional data or scenarios.
 */
function nestedWhileLoop() {
    let row = 1;

    while (row <= 3) {
        let column = 1;

        while (column <= 3) {
            console.log(`Row ${row}, Column ${column}`); // Output for a 3x3 grid.
            column++;
        }

        row++;
    }
}
nestedWhileLoop();

/**
 * Demonstrates using a while loop to validate data.
 * 
 * Ensures the input meets a specific condition.
 */
function dataValidationWhileLoop() {
    const inputs = ["", "123", "abc", "validInput"];
    let index = 0;
    let input;

    while (input !== "validInput") {
        input = inputs[index++];
        console.log(`Current input: ${input}`);
    }

    console.log("Valid input received. Exiting loop."); // Output after valid input.
}
dataValidationWhileLoop();

/**
 * Demonstrates a decrementing while loop.
 * 
 * Iterates backwards from a starting value.
 */
function decrementingWhileLoop() {
    let number = 5;

    while (number >= 1) {
        console.log(`Countdown: ${number}`); // Output: Countdown: 5, 4, 3, 2, 1
        number--;
    }

    console.log("Loop completed.");
}
decrementingWhileLoop();

/**
 * Demonstrates a basic do...while loop.
 * 
 * Executes the block at least once, even if the condition is initially `false`.
 */
function basicDoWhileLoop() {
    let count = 1;

    do {
        console.log(`Count is: ${count}`); // Output: Count is: 1, 2, 3, 4, 5
        count++;
    } while (count <= 5);
}
basicDoWhileLoop();

/**
 * Demonstrates a do...while loop with a condition that starts as `false`.
 * 
 * Useful for scenarios where you need to execute the loop at least once.
 */
function conditionFalseDoWhileLoop() {
    let number = 10;

    do {
        console.log(`Number is: ${number}`); // Output: Number is: 10
        number--;
    } while (number < 0); // Condition is `false`, but block executes once.
}
conditionFalseDoWhileLoop();

/**
 * Demonstrates a do...while loop for user input validation (simulated).
 * 
 * Ensures input meets specific criteria and keeps prompting until it does.
 */
function userInputDoWhileLoop() {
    const responses = ["invalid", "wrong", "correct"];
    let i = 0;
    let input;

    do {
        input = responses[i++];
        console.log(`User input: ${input}`); // Output: User input: invalid, wrong, correct
    } while (input !== "correct");

    console.log("Valid input received. Exiting loop."); // Output after "correct" input.
}
userInputDoWhileLoop();