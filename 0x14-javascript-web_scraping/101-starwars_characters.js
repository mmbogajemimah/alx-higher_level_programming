#!/usr/bin/node
// a script that prints all characters of a Star Wars movie:

const request = require('request');

// Get command arguments
const movieID = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;

// Send request
request(url, function (error, response, body) {
  if (!error) {
    const characterIndex = 0;
    const characters = JSON.parse(body).characters;

    getCharacter(characters, characterIndex);
  }
});

function getCharacter (characters, characterIndex) {
  request(characters[characterIndex], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);

      if (characterIndex < characters.length - 1) {
        getCharacter(characters, characterIndex + 1);
      }
    }
  });
}
