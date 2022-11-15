#!/usr/bin/node
// a script that prints the title of a Star Wars movie where
// the episode number matches a given integer.

const request = require('request');
const number = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + number;

// Sending request
request(url, function (error, response, body) {
  const episode = JSON.parse(body);
  if (!error) console.log(episode.title);
});
