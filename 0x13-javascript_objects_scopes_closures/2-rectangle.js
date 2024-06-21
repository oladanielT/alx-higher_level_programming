#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return null;
    }
    this.width = w;
    this.height = h;
  }

  getWidth () {
    return this.width;
  }

  getHeight () {
    return this.height;
  }
}
module.exports = Rectangle;
