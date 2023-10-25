#!/usr/bin/node

const fs = require('fs');
const fn = process.argv[2];
fs.readFile(fn, 'utf8', (error, data) => {
	if (error) {
		console.error("Error reading filr:", error);
		return;
	}
	console.log(data);
});
