#!/usr/bin/node
let url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
