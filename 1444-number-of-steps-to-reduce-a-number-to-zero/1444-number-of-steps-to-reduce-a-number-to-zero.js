/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    let numOfSteps = 0
    let numClone = num

    while (numClone !== 0) {
        const isEven = numClone % 2 === 0
        isEven ? numClone /= 2 : numClone -= 1
        numOfSteps++
    }
    
    return numOfSteps
};