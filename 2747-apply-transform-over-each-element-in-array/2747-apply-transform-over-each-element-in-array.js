/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const mappedArr = []

    arr.forEach((elem, i) => {
        const newVal = fn(elem, i)
        mappedArr.push(newVal)
    })

    return mappedArr
};