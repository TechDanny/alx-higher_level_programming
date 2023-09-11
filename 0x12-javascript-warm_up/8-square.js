#!/usr/bin/node

const myArg = process.argv[2];
const x = Number(myArg);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let n = 0; n < x; n++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
