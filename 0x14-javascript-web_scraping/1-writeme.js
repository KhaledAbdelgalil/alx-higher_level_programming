#!/usr/bin/node
const file = require('fs');
file.writeFile(process.argv[2], process.argv[3], function (error) {
  if (error) console.log(error);
});
