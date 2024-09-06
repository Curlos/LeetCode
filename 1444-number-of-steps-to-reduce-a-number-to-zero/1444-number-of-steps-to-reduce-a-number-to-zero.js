/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    let numOfSteps = 0
    let numClone = num

    while (numClone > 0) {
        const isEven = numClone % 2 === 0

        if (isEven) {
            numClone /= 2
        } else {
            numClone -= 1
        }

        numOfSteps++
    }

    return numOfSteps
};