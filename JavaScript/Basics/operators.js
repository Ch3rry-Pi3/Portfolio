/**
 * Shows standard arithmetic operators in JavaScript.
 * 
 * Includes addition, subtraction, multiplication, and division.
 */
function arithmeticOperators() {
    const a = 10;
    const b = 5;

    console.log(`Addition: ${a} + ${b} = ${a + b}`); // Output: 15
    console.log(`Subtraction: ${a} - ${b} = ${a - b}`); // Output: 5
    console.log(`Multiplication: ${a} * ${b} = ${a * b}`); // Output: 50
    console.log(`Division: ${a} / ${b} = ${a / b}`); // Output: 2
}
arithmeticOperators();

/**
 * Shows the remainder operator (%) in JavaScript.
 * 
 * The remainder operator returns the remainder of a division.
 */
function remainderOperator() {
    const dividend = 10;
    const divisor = 3;

    console.log(`Remainder: ${dividend} % ${divisor} = ${dividend % divisor}`); // Output: 1
}
remainderOperator();

/**
 * Shows the increment (++) and decrement (--) operators.
 * 
 * These operators increase or decrease a value by 1.
 */
function incrementDecrement() {
    let counter = 5;

    console.log(`Initial value: ${counter}`); // Output: 5
    console.log(`Post-increment: ${counter++}`); // Output: 5 (then counter becomes 6)
    console.log(`After post-increment: ${counter}`); // Output: 6

    console.log(`Pre-increment: ${++counter}`); // Output: 7 (counter becomes 7, then prints)

    console.log(`Post-decrement: ${counter--}`); // Output: 7 (then counter becomes 6)
    console.log(`After post-decrement: ${counter}`); // Output: 6

    console.log(`Pre-decrement: ${--counter}`); // Output: 5 (counter becomes 5, then prints)
}
incrementDecrement();

/**
 * Shows the exponentiation operator (**) in JavaScript.
 * 
 * Raises a base to the power of an exponent.
 */
function exponentiation() {
    const base = 2;
    const exponent = 3;

    console.log(`Exponentiation: ${base} ** ${exponent} = ${base ** exponent}`); // Output: 8
}
exponentiation();

/**
 * Shows assignment operators between variables.
 * 
 * Includes addition, subtraction, multiplication, division, and remainder assignments.
 */
function assignmentOperators() {
    let x = 10;

    console.log(`Initial value: ${x}`); // Output: 10

    x += 5; // x = x + 5
    console.log(`After addition assignment (x += 5): ${x}`); // Output: 15

    x -= 3; // x = x - 3
    console.log(`After subtraction assignment (x -= 3): ${x}`); // Output: 12

    x *= 2; // x = x * 2
    console.log(`After multiplication assignment (x *= 2): ${x}`); // Output: 24

    x /= 4; // x = x / 4
    console.log(`After division assignment (x /= 4): ${x}`); // Output: 6

    x %= 4; // x = x % 4
    console.log(`After remainder assignment (x %= 4): ${x}`); // Output: 2
}
assignmentOperators();

/**
 * Shows comparison operators in JavaScript.
 * 
 * Includes equality, strict equality, inequality, and relational operators.
 */
function comparisonOperators() {
    const a = 10;
    const b = 5;
    const c = "10";

    console.log(`Equality: ${a} == ${c} -> ${a == c}`); // Output: true (type coercion)
    console.log(`Strict Equality: ${a} === ${c} -> ${a === c}`); // Output: false (no type coercion)

    console.log(`Inequality: ${a} != ${b} -> ${a != b}`); // Output: true
    console.log(`Strict Inequality: ${a} !== ${c} -> ${a !== c}`); // Output: true

    console.log(`Greater than: ${a} > ${b} -> ${a > b}`); // Output: true
    console.log(`Less than: ${a} < ${b} -> ${a < b}`); // Output: false
}
comparisonOperators();

/**
 * Shows logical operators in JavaScript.
 * 
 * Includes AND (&&), OR (||), and NOT (!).
 */
function logicalOperators() {
    const isTrue = true;
    const isFalse = false;

    console.log(`Logical AND: ${isTrue} && ${isFalse} -> ${isTrue && isFalse}`); // Output: false
    console.log(`Logical OR: ${isTrue} || ${isFalse} -> ${isTrue || isFalse}`); // Output: true
    console.log(`Logical NOT: !${isTrue} -> ${!isTrue}`); // Output: false
}
logicalOperators();

/**
 * Shows concatenation operator (+) with strings.
 * 
 * The `+` operator can concatenate strings.
 */
function stringConcatenationOperator() {
    const firstName = "John";
    const lastName = "Doe";

    console.log(`Full Name: ${firstName} + " " + ${lastName} -> ${firstName + " " + lastName}`); // Output: John Doe
}
stringConcatenationOperator();