#!/usr/bin/node
// Computes the number of tasks completed by user id
// Importing modules
const request = require('request');

// Command line arguments
const URL = process.argv[2];

// Sending a get request
request(URL, function (error, response, body) {
  if (!error) {
    const userTaskInfo = {};
    const todos = JSON.parse(body);

    // Looping the todos
    todos.forEach(todo => {
      if (!todo.completed) {
        return;
      }

      if (userTaskInfo[todo.userId]) {
        userTaskInfo[todo.userId] = userTaskInfo[todo.userId] + 1;
      } else {
        userTaskInfo[todo.userId] = 1;
      }
    });
    console.log(userTaskInfo);
  }
});
