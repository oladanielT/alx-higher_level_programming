#!/usr/bin/node
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

if (isNaN(a) || isNaN(b)) {
  console.error(NaN);
} else {
  function add (a, b) {
    return a + b;
  }
  console.log(add(a, b));
}
