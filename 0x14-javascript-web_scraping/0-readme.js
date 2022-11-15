#!/usr/bin/node
/* A script that reads and prints the content of a file */

// Requiring the fs module used in reading and writing
const fs = require('fs');
// The first argument is the file path
const fileName = process.argv[2];
// The content of the file must be read in utf-8
fs.readFile(fileName, 'utf-8', function(err, data) {
	// If an error occurred during the reading, print the error object
	if (err) {
		console.log(error);
	// If data available print the data in the file
	} else {
		console.log(data);
	}
});
