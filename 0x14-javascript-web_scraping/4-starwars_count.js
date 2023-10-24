#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');

request(MyArgs[2], (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  body = JSON.parse(body);
  let count = 0;
  for (const movie of body.results) {
    for (const chr of movie.characters) {
      if (chr.includes('18')) count++;
    }
  }
  console.log(count);
});
