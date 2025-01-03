/**
 * Demonstrates implicit type conversions (type coercion) in JavaScript.
 * 
 * Implicit type conversions occur automatically during operations.
 */
function implicitConversions() {
    // String concatenation with a number converts the number to a string.
    const result1 = "The number is " + 42;
    console.log(result1); // Output: The number is 42

    // Arithmetic operation with a string containing a number coerces to a number.
    const result2 = "5" * 2;
    console.log(result2); // Output: 10

    // Adding a string and a boolean converts the boolean to a string.
    const result3 = "Value is " + true;
    console.log(result3); // Output: Value is true

    // Boolean coercion in logical operations.
    const result4 = !!0; // 0 is falsy, coerced to false.
    const result5 = !!"Hello"; // Non-empty strings are truthy.
    console.log(`Boolean of 0: ${result4}`); // Output: Boolean of 0: false
    console.log(`Boolean of "Hello": ${result5}`); // Output: Boolean of "Hello": true
}
implicitConversions();

/**
 * Demonstrates explicit type conversions in JavaScript.
 * 
 * Explicit conversions are performed using specific methods or operators.
 */
function explicitConversions() {
    // Converting a string to a number using Number().
    const strNum = "123";
    const num = Number(strNum);
    console.log(`String "${strNum}" converted to number: ${num}`); // Output: 123

    // Converting a string to an integer using parseInt().
    const floatStr = "45.67";
    const intNum = parseInt(floatStr, 10);
    console.log(`String "${floatStr}" converted to integer: ${intNum}`); // Output: 45

    // Converting a string to a float using parseFloat().
    const floatNum = parseFloat(floatStr);
    console.log(`String "${floatStr}" converted to float: ${floatNum}`); // Output: 45.67

    // Converting a number to a string using String().
    const numToStr = String(456);
    console.log(`Number 456 converted to string: "${numToStr}"`); // Output: "456"

    // Boolean to string.
    const boolToStr = String(true);
    console.log(`Boolean true converted to string: "${boolToStr}"`); // Output: "true"

    // Converting a number to a boolean using Boolean().
    const zeroToBool = Boolean(0); // 0 is falsy.
    const nonZeroToBool = Boolean(100); // Non-zero numbers are truthy.
    console.log(`Number 0 converted to boolean: ${zeroToBool}`); // Output: false
    console.log(`Number 100 converted to boolean: ${nonZeroToBool}`); // Output: true
}
explicitConversions();

/**
 * Shows edge cases in type conversions.
 */
function edgeCaseConversions() {
    // Converting a non-numeric string to a number results in NaN.
    const invalidNum = Number("abc");
    console.log(`String "abc" converted to number: ${invalidNum}`); // Output: NaN

    // Using parseInt() on a non-numeric string parses until invalid character.
    const partialParse = parseInt("123abc", 10);
    console.log(`String "123abc" partially parsed to integer: ${partialParse}`); // Output: 123

    // Converting an empty string to a number results in 0.
    const emptyStrToNum = Number("");
    console.log(`Empty string converted to number: ${emptyStrToNum}`); // Output: 0

    // Converting undefined to a number results in NaN.
    const undefinedToNum = Number(undefined);
    console.log(`Undefined converted to number: ${undefinedToNum}`); // Output: NaN
}
edgeCaseConversions();