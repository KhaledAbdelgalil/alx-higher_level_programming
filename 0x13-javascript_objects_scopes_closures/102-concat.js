#!/usr/bin/node
const filesystemOperations = require('fs');

const firstFileContent = filesystemOperations.readFileSync(process.argv[2]).toString();
const secondFileContent = filesystemOperations.readFileSync(process.argv[3]).toString();
filesystemOperations.writeFileSync(process.argv[4], firstFileContent + secondFileContent);
