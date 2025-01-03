/**
 * Demonstrates a basic for loop.
 * 
 * Iterates a fixed number of times using a counter variable.
 */
function basicForLoop() {
    for (let i = 1; i <= 5; i++) {
        console.log(`Iteration: ${i}`); // Output: Iteration: 1, 2, 3, 4, 5
    }
}
basicForLoop();

/**
 * Demonstrates iterating over an array using a for loop.
 * 
 * Accesses each element of an array using its index.
 */
function arrayIteration() {
    const fruits = ["apple", "banana", "cherry"];

    for (let i = 0; i < fruits.length; i++) {
        console.log(`Fruit: ${fruits[i]}`); // Output: Fruit: apple, banana, cherry
    }
}
arrayIteration();

/**
 * Demonstrates using a for loop with a conditional break.
 * 
 * Exits the loop early if a condition is met.
 */
function forLoopWithBreak() {
    for (let i = 1; i <= 10; i++) {
        if (i === 5) {
            console.log("Breaking at 5."); // Output: Breaking at 5.
            break;
        }
        console.log(`Count: ${i}`); // Output: Count: 1, 2, 3, 4
    }
}
forLoopWithBreak();

/**
 * Demonstrates using a for loop with a conditional continue.
 * 
 * Skips the current iteration if a condition is met.
 */
function forLoopWithContinue() {
    for (let i = 1; i <= 5; i++) {
        if (i === 3) {
            console.log("Skipping 3."); // Output: Skipping 3.
            continue;
        }
        console.log(`Count: ${i}`); // Output: Count: 1, 2, 4, 5
    }
}
forLoopWithContinue();

/**
 * Demonstrates a nested for loop.
 * 
 * Useful for working with multi-dimensional data or grids.
 */
function nestedForLoop() {
    for (let row = 1; row <= 3; row++) {
        for (let col = 1; col <= 3; col++) {
            console.log(`Row: ${row}, Column: ${col}`); // Outputs a 3x3 grid.
        }
    }
}
nestedForLoop();

/**
 * Demonstrates iterating backwards using a for loop.
 * 
 * Decrements the counter variable instead of incrementing.
 */
function reverseForLoop() {
    for (let i = 5; i >= 1; i--) {
        console.log(`Countdown: ${i}`); // Output: Countdown: 5, 4, 3, 2, 1
    }
}
reverseForLoop();

/**
 * Demonstrates iterating over an array with conditional logic.
 * 
 * Filters items during iteration based on conditions.
 */
function conditionalArrayIteration() {
    const numbers = [1, 2, 3, 4, 5, 6, 7];

    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] % 2 === 0) {
            console.log(`Even number: ${numbers[i]}`); // Output: Even number: 2, 4, 6
        }
    }
}
conditionalArrayIteration();

/**
 * Demonstrates iterating over a string using a for loop.
 * 
 * Treats the string as an array of characters.
 */
function stringIteration() {
    const word = "JavaScript";

    for (let i = 0; i < word.length; i++) {
        console.log(`Character at index ${i}: ${word[i]}`); // Output: Characters of "JavaScript"
    }
}
stringIteration();

/**
 * Demonstrates iterating over the keys of an object using a for...in loop.
 * 
 * Iterates through all enumerable properties of an object.
 */
function objectKeyIteration() {
    const student = {
        name: "Roger",
        grade: 9,
        age: 13,
    };

    for (const key in student) {
        if (student.hasOwnProperty(key)) {
            console.log(`${key}: ${student[key]}`);
            // Output:
            // name: Roger
            // grade: 9
            // age: 13
        }
    }
}
objectKeyIteration();