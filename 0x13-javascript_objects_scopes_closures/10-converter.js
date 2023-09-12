#!/usr/bin/node

exports.converter = function (base) {
  return function converter (n) {
    return n.toString(base);
  };
};
