/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // if (!nums || nums.length === 0) {
    //     return []
    // }

    const seenNumbers = {}

    for (let [i, num] of nums.entries()) {
        const x = target - num

        console.log(i, num, x, seenNumbers[x])

        if (seenNumbers[x] !== undefined) {
            return [seenNumbers[x], i]
        }

        seenNumbers[num] = i
    }

    return []
};