#!/usr/bin/node

if (!isNaN(process.argv[2])) {
  const myNumber = parseInt(process.argv[2]);
  console.log(`My Number: ${myNumber}`);
} else {
  console.log('Not a Number');
}
