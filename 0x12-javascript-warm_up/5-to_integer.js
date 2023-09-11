#!/usr/bin/node

const myArg = process.argv[2];
const newArg = Number(myArg);
const rounded = Math.floor(newArg);

if (!isNaN(myArg)) {
  console.log(`My number: ${rounded}`);
} else {
  console.log('Not a number');
}
