#!/usr/bin/node
exports.callMeMoby = function (x, callFunction) {
  for (let i = 0; i < x; i++) callFunction();
};
