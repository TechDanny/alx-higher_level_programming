#!/usr/bin/node

const myArg = process.argv[2];
const x = Number(myArg);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
