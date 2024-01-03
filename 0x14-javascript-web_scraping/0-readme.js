#!/usr/bin/node
const process = require('process');
const fs = require('fs');

// the first arg is the file path
const file = process.argv[2];
// file content on utf8
fs.readFile(file, 'utf8', function (err, data){
    // if err, print error object.
    if (err) {
        console.log(err);
    } else {
        process.stdout.write(data);
    }
});
