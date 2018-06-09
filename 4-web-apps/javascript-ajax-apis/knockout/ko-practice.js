// Require modules to run file from Node.js outside of browser
const ko = require('knockout')

// FSND JavaScript Design Patterns course
// Lesson 05 organizational library: Knockout
let firstName = 'Ben'
let lastName = 'Jaffe'
let fullName = `${firstName} ${lastName}`
let koName = ko.observable(`${firstName} ${lastName}`)
console.log(fullName, koName._latestValue)
