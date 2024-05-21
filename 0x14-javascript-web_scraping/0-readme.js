#!/usr/bin/node
const fileReader = require('fs');
fileReader.readFile(process.argv[2], 'utf-8', function(error, content) {
    console.log(error || content);
});