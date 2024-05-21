#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
request.get(url, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const films = JSON.parse(body);
  const characters = films.characters;
  for (const characterUrl of characters) {
    request.get(characterUrl, function (error, res, bodyCharacter) {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(bodyCharacter).name);
    });
  }
});
