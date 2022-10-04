#!/usr/bin/node
const Square2 = require('./5-square');

class Square extends Square2 {
  charPrint (c) {
    let stringSquare = '';
    if (!c) {
      for (let i = 1; i <= this.height; i++) {
        for (let j = 1; j <= this.width; j++) {
          stringSquare += 'X';
        }
        if (i < this.height) {
          stringSquare += '\n';
        }
      }
    } else {
      for (let i = 1; i <= this.height; i++) {
        for (let j = 1; j <= this.width; j++) {
          stringSquare += c;
        }
        if (i < this.height) {
          stringSquare += '\n';
        }
      }
    }
    console.log(stringSquare);
  }
}

module.exports = Square;
