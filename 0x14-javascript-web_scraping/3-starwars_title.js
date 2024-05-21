#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/';
const get_url = url + process.argv[2];
const request = require('request');
request(get_url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
