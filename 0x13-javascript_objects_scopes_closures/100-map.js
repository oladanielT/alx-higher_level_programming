#!/usr/bin/node


const list = require('./100-data.js');

let new_list = list.map((a, b) => a * b);
console.log(list);
console.log(new_list);
