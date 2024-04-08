#!/usr/bin/node
const arg = process.argv[2];
const num = Math.floor(Number(arg));
if (!isNaN(num) && arg.trim() !== '') {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
