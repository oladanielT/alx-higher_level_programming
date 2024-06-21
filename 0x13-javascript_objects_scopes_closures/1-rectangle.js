#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
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
