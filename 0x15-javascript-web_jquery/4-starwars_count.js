#!/usr/bin/node
const args = require('process').argv;
const request = require('request');

request(args[2], (error, response, body) => {
  if (error) {
    console.log(error);
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
