#!/usr/bin/node

module.exports = class Rectangle {
  constructor (_w, _h) {
    if (_w > 0 && _h > 0) {
      this.width = _w;
      this.height = _h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let n = 0; n < this.width; n++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
