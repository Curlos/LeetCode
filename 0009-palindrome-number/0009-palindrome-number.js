/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const strNumber = String(x).split('')

    let left = 0
    let right = strNumber.length - 1

    while (left < right) {
        if (strNumber[left] !== strNumber[right]) {
            return false
        }

        left += 1
        right -= 1
    }

    return true
};