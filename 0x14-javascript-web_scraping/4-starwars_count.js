#!/usr/bin/node
// Script that prints the number of movies where
// the character "Wedge Antilles" is present.
// Importing request module
const request = require('request');

// Get command line arguments
const URL = process.argv[2];

// Sending a get request
request(URL, function (error, response, body) {
  const films = JSON.parse(body).results;
  let counter = 0;

  if (!error) {
    // Loop films
    for (let i = 0; i < films.length; i++) {
      const film = films[i];

      // Loop through the film cgaracters
      for (let j = 0; j < film.characters.length; j++) {
        if (film.characters[j].endsWith('/18/')) {
          counter++;
          break;
        }
      }
    }
  }
  console.log(counter);
});
