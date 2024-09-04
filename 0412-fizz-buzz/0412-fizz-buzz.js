/**
 * @description O(N) Time, O(N) Space
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    const fizzBuzzArr = []

    // Using the integer "n", iterate from 1 to n and for each number, depending on the condition it fulfills, push the value into the new array.
    for (let i = 1; i <= n; i++) {
        const divisibleBy3 = i % 3 === 0
        const divisibleBy5 = i % 5 === 0

        if (divisibleBy3 && divisibleBy5) {
            fizzBuzzArr.push("FizzBuzz")
        } else if (divisibleBy3) {
            fizzBuzzArr.push("Fizz")
        } else if (divisibleBy5) {
            fizzBuzzArr.push("Buzz")
        } else {
            fizzBuzzArr.push(String(i))
        }
    }

    return fizzBuzzArr
};