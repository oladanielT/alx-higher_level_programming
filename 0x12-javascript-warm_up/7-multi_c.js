#!/usr/bin/node
const arg = Number(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else if (arg > 0) {
  for (let l = 0; l < arg; l++) {
    console.log('C is fun');
  }
}
