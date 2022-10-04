#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let stringSquare = '';
    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) {
        stringSquare += 'X';
      }
      if (i < this.height) {
        stringSquare += '\n';
      }
    }
    console.log(stringSquare);
  }
}
module.exports = Rectangle;
