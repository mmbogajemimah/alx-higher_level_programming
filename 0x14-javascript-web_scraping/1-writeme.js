#!/usr/bin/node
// a script that writes a string to a file.

// Requiring the fs module used in reading and writing
const fs = require('fs');
// The content of the file must be written to in utf-8
const fileName = process.argv[2];
// Input string written in file
const inputString = process.argv[3];
// writing inputstring in the file
fs.writeFile(fileName, inputString, 'utf-8', function (error) {
  // if an error occurs print it out
  if (error) {
    console.log(error);
  }
});
