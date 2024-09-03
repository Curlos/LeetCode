/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    // [3, 1, 2, 10, 1]
    for (let i = 1; i < nums.length; i++) {
        // Get the current running sum by looking at the previous element's value
        const prevElemValue = nums[i - 1]
        const currElemValue = nums[i]

        nums[i] = prevElemValue + currElemValue
    }
    
    return nums
};