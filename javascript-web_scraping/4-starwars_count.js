#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  let count = 0;
  data.results.forEach((film) => {
    film.characters.forEach((charUrl) => {
      if (charUrl.includes('/18/')) {
        count++;
      }
    });
  });
  console.log(count);
});
