#!/usr/bin/node

// a script that gets the contents of a webpage and stores it in a file.
const URL = process.argv[2];
const filePath = process.argv[3];

const fs = require('fs');
const request = require('request');

// Sending request
request(URL, function (error, response, body) {
  if (!error) {
    fs.writeFile(filePath, body, 'utf-8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
