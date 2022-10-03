#!/usr/bin/node
const arrayNums = [];

const lengthNums = process.argv.length;
if ((lengthNums === 2) || (lengthNums === 3)) {
  console.log(0);
} else {
  for (let i = 2; i < lengthNums; i++) {
    arrayNums.push(process.argv[i]);
  }
  arrayNums.sort().reverse();
  console.log(arrayNums[1]);
}
