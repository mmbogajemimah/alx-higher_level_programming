#!/usr/bin/node

const numberSquare = parseInt(process.argv[2]);
let stringSquare = '';
if (!isNaN(process.argv[2])) {
  for (let i = 1; i <= numberSquare; i++) {
    for (let j = 1; j <= numberSquare; j++) {
      stringSquare += 'X';
    }
    if (i < numberSquare) {
      stringSquare += '\n';
    }
  }
  console.log(stringSquare);
} else {
  console.log('Missing size');
}
