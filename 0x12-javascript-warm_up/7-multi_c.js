#!/usr/bin/node
const myNumber = parseInt(process.argv[2]);

if (!isNaN(process.argv[2]) && myNumber > 0) {
  let i = 0;
  while (i < myNumber) {
    console.log('C is fun');
    i = i + 1;
  }
} else {
  console.log('Missing number of occurrences');
}
