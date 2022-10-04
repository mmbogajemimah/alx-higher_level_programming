#!/usr/bin/node

exports.esrever = function (list) {
  const listLength = list.length - 1;
  const arr = [];
  for (let i = listLength; i >= 0; i--) {
    arr.push(list[i]);
  }
  return arr;
};
