/**
 * Demonstrates a basic switch statement with individual cases.
 */
function individualCases() {
    const fruit = "apple";

    switch (fruit) {
        case "apple":
            console.log("Apples are red or green."); // Output: Apples are red or green.
            break;
        case "banana":
            console.log("Bananas are yellow.");
            break;
        case "orange":
            console.log("Oranges are orange.");
            break;
        default:
            console.log("Unknown fruit.");
    }
}
individualCases();

/**
 * Demonstrates a switch statement with joint cases.
 * 
 * Joint cases are useful when multiple cases share the same outcome.
 */
function jointCases() {
    const day = "Saturday";

    switch (day) {
        case "Saturday":
        case "Sunday":
            console.log("It's the weekend!"); // Output: It's the weekend!
            break;
        case "Monday":
        case "Tuesday":
        case "Wednesday":
        case "Thursday":
        case "Friday":
            console.log("It's a weekday.");
            break;
        default:
            console.log("Not a valid day.");
    }
}
jointCases();

/**
 * Demonstrates the use of a default case in a switch statement.
 * 
 * The default case executes if no other cases match.
 */
function defaultCase() {
    const weather = "windy";

    switch (weather) {
        case "sunny":
            console.log("Wear sunglasses.");
            break;
        case "rainy":
            console.log("Take an umbrella.");
            break;
        case "snowy":
            console.log("Wear a coat and boots.");
            break;
        default:
            console.log("Check the weather report."); // Output: Check the weather report.
    }
}
defaultCase();

/**
 * Demonstrates handling numeric cases in a switch statement.
 */
function numericCases() {
    const score = 85;

    switch (true) {
        case score >= 90:
            console.log("Grade: A");
            break;
        case score >= 80:
            console.log("Grade: B"); // Output: Grade: B
            break;
        case score >= 70:
            console.log("Grade: C");
            break;
        case score >= 60:
            console.log("Grade: D");
            break;
        default:
            console.log("Grade: F");
    }
}
numericCases();

/**
 * Demonstrates fallthrough behavior in a switch statement.
 * 
 * Cases without a `break` will continue to execute subsequent cases.
 */
function fallthroughBehavior() {
    const color = "yellow";

    switch (color) {
        case "red":
            console.log("Stop.");
            break;
        case "yellow":
            console.log("Caution."); // Output: Caution.
        case "green":
            console.log("Go."); // Output: Go.
            break;
        default:
            console.log("Invalid signal.");
    }
}
fallthroughBehavior();