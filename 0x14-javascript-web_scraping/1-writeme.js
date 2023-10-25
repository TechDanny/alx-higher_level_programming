#!/usr/bin/node

const fs = require('fs');
const fn = process.argv[2];
fs.writeFile(fn, process.argv[3], 'utf8', error => {
  if (error) {
    console.log(error);
  }
});
