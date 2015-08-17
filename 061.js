#!/usr/bin/env node
'use strict';

var routes = {};

var Digit = function (name, num) {
  this.name  = name;
  this.value = num;
  this.head  = num.slice(0, 2);
  this.tail  = num.slice(2, 4);

  routes[this.head] = routes[this.head] || [];
  routes[this.head].push(this);
};

var find4digit = function (name, poly) {
  var ret = [];
  var digit;
  var n = 0;
  while (++n) {
    digit = poly(n);
    if (digit > 9999) {
      return ret;
    }

    if (digit > 999) {
      ret.push(new Digit(name, digit + ''));
    }
  }
};

var triangles = find4digit('triangle', function (n) {
  return n * (n + 1) / 2;
});

var squares = find4digit('square', function (n) {
  return n * n;
});

var pentagonals = find4digit('pentagon', function (n) {
  return n * (3 * n - 1) / 2;
});

var hexagonals = find4digit('hexagon', function (n) {
  return n * (2 * n  - 1);
});

var heptagonals = find4digit('heptagon', function (n) {
  return n * (5 * n  - 3) / 2;
});

var octagonals = find4digit('octagon', function (n) {
  return n * (3 * n  - 2);
});

Object.keys(routes).forEach(function (key) {
  routes[key].sort(function (a, b) {
    return a.tail - b.tail;
  });
});

var candidates = [];

var findNext = function (prev, keys, values) {
  if (! routes[prev.tail]) { return; };
  routes[prev.tail].forEach(function (next) {
    if (keys.indexOf(next.name) !== -1) {
      return;
    }

    var nextKeys = keys.slice(0);
    nextKeys.push(next.name);

    var nextValues = values.slice(0);
    nextValues.push(next);

    if (nextKeys.length === 6) {
      if (next.tail === values[0].head) {
        candidates.push(nextValues);
      }
      return;
    }

    findNext(next, nextKeys, nextValues);
  });
};

triangles.forEach(function (triangle) {
  if (! routes[triangle.tail]) { return; };
  findNext(triangle, ['triangle'], [triangle]);
});

console.log(candidates);


var result = candidates.map(function (ans) {
  return ans.reduce(function (a, b) {
    return a + parseInt(b.value, 10);
  }, 0);
});

console.log(result);
