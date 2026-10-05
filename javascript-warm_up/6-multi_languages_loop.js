#!/usr/bin/node
const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let result = '';

for (let i = 0; i < languages.length; i++) {
  result += `${languages[i]}\n`;
}

console.log(result.trim());
