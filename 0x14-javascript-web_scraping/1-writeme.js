#!/usr/bin/node
const MyArgs = require('process').argv;
const fs = require('fs');

fs.writeFile(myArgs[0], myArgs[1], 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
