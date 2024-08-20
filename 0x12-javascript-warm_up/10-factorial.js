#!/usr/bin/node
const num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log(1);
} else {
  function fact (num) {
    if (num === 1) {
      return 1;
    } else {
      return num * fact(num - 1);
    }
  }
  console.log(fact(num));
}
