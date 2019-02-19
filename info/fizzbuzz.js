/* FizzBuzz
https://medium.freecodecamp.org/a-software-engineering-survival-guide-fe3eafb47166
https://medium.freecodecamp.org/coding-interviews-for-dummies-5e048933b82b
https://stackoverflow.com/a/17623252
Write a program that prints the numbers from 1 to 100.
For multiples of three print 'Fizz' instead of the number.
For multiples of five print 'Buzz' instead of the number.
For multiples of both three and five print 'FizzBuzz'.
This solution uses the following syntax features:
Modulo (%, remainder)
Strict equality (===), avoiding type coercion (==)
Addition assignment (+=)
Boolean OR (||)
Template strings (``)
ES6 arrow functions (=>)
Immediately-invoked function expressions (IIFE)
*/

const fizzBuzz = () => {
  for (let i = 1; i <= 100; i++) {
    let out = ``
    if (i % 3 === 0) out += `Fizz`
    if (i % 5 === 0) out += `Buzz`
    console.log(out || i)
  }
}
fizzBuzz()
