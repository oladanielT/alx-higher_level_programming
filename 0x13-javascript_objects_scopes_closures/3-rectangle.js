#!/usr/bin/node



class Rectangle {
	constructor (w, h) {
		if (w <= 0 || h <= 0) {
			return {};
		} else {
			this.width = w;
			this.height = h;
		}
	}

	print () {
		for (let i = 0; i <= this.height; i++) {
			let line = '';
			for (let j = 0; j <= this.width; j++) {
				line += 'X';
			}
			console.log(line);
		}
	}
}

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();
