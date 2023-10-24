#!/usr/bin/node
const myArgs = process.argv.slice(2);
const fs = require('fs');

fs.writeFile(myArgs[0], myArgs[1], 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
