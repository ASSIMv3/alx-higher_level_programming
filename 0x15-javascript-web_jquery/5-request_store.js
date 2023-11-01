#!/usr/bin/node
const myArgs = process.argv.slice(2);
const fs = require('fs');
const request = require('request');

request(myArgs[0], function (error, response, body) {
  if (!error) {
    fs.writeFile(myArgs[1], body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
