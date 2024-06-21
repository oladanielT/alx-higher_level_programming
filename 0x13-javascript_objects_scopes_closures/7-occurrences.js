#!/usr/bin/node


exports.nbOccurences = function (list, searchElement) {
	let nub = 0;
	for (let i = 0; i < list.length; i++) {
		if (searchElement === list[i]) {
			nub ++;
		}
	}
	return nub;
}
