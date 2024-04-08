#!/usr/bin/node

const args = process.argv.map(Number);
const sortedArgs = args.filter(num => !isNaN(num)).sort((a, b) => a - b);

if (sortedArgs.length <= 1) {
  console.log(0);
} else {
  console.log(sortedArgs[sortedArgs.length - 2]);
}
