/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let runningSum = 0

    return nums.map((num) => {
        const newValue = runningSum + num
        runningSum += num
        return newValue
    })
};