#!/usr/bin/node

const myArg = Number(process.argv[2]);

function factorialNumber (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n <= 1) {
    return 1;
  } else {
    return n * factorialNumber(n - 1);
  }
}

if (!isNaN(myArg)) {
  console.log(factorialNumber(myArg));
} else {
  console.log('1');
}
