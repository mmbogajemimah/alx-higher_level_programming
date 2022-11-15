#!/usr/bin/node

const request = require('request');
const fileUrl = process.argv[2];
request
  .get(fileUrl)
  .on('response', function (response) {
    console.log('code: ', response.statusCode);
  });
