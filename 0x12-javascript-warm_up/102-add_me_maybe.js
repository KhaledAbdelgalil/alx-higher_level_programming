#!/usr/bin/node
exports.addMeMaybe = function (number, callFunction) {
  callFunction(++number);
};
