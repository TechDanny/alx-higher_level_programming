#!/usr/bin/node

const request = require('request');
const num = process.argv[2];
const GET_URL = 'https://swapi-api.alx-tools.com/api/films/';
request(GET_URL + num, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const content = JSON.parse(body);
    console.log(content.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
