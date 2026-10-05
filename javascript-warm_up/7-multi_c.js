#!/usr/bin/node
const occurrences = parseInt(process.argv[2], 10);

if (isNaN(occurrences)) {
  console.log('Missing number of occurrences');
} else {
  let result = '';
  for (let i = 0; i < occurrences; i++) {
    result += 'C is fun\n';
  }
  console.log(result.trim());
}
