#!/usr/bin/node
const MyArgs = require('process').argv;
const request = require('request');

request(myArgs[0], function (error, response, body) {
  if (!error && response) {
    console.log('code:', response.statusCode);
  }
});
