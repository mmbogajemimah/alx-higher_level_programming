#!/usr/bin/node
function factorial (number) {
  if (number === 1) {
    return 1;
  } else if (number > 1) {
    return number * (factorial(number - 1));
  }
}

const varNumber = parseInt(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  console.log(factorial(varNumber));
}
