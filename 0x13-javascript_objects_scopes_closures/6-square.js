#!/usr/bin/node

const BaseSquare = require('./5-square.js');


class Square extends BaseSquare {
	constructor (size) {
		super(size, size);
	}

	charPrint (c) {
		for (let i = 0; i < this.height; i++) {
			if (c === undefined) {
				console.log('X'.repeat(this.width));
			} else {
				console.log(c.repeat(this.width));
			}
		}
	}
}
module.exports = Square;
