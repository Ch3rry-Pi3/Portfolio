// Import the Express library
const express = require('express');

// Initialise an instance of the Express app
const app = express();

// Define a route handler for the root path ('/')
app.get('/', (req, res) => {
    // Send a simple text response to the client
    res.send("Welcome to my awesome app!");
});

// Start the application and listen for incoming requests on port 3000
app.listen(3000, function () {
    // Log a message to indicate the server is running
    console.log("App listening on port 3000");
});