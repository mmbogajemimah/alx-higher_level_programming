#!/usr/bin/node
const arrayNums = [];

const lengthNums = process.argv.length;
if ((lengthNums === 2) || (lengthNums === 3)) {
  console.log(0);
} else {
  for (let i = 2; i < lengthNums; i++) {
    arrayNums.push(process.argv[i]);
  }
  const maximum = Math.max(...arrayNums);
  arrayNums.splice(arrayNums.indexOf(maximum), 1);
  console.log(Math.max(...arrayNums));
}
