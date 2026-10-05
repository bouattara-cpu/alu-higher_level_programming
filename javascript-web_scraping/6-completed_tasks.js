#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const completedTasks = {};
  body.forEach((task) => {
    if (task.completed) {
      if (completedTasks[task.userId] === undefined) {
        completedTasks[task.userId] = 0;
      }
      completedTasks[task.userId]++;
    }
  });
  console.log(completedTasks);
});
