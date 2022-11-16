#!/usr/bin/node
// Prints all characters of a starwars movie in the right order

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function getCharacter (characters, index) {
  request(characters[index], (err, resp, bd) => {
    if (err) console.error(err);
    if (resp && resp.statusCode === 200) {
      console.log(JSON.parse(bd).name);
      if (index < characters.length - 1) {
        getCharacter(characters, ++index);
      }
    }
  });
}

request(url, (error, response, body) => {
  if (error) console.error(error);
  if (response && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    getCharacter(characters, 0);
  }
});
