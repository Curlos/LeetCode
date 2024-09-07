/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    // Go through "magazine" and create a hashmap of all the characters and the number of times they appear in "magazine". For example, if you have "aaab", then the hashmap will be {"a": 3, "b": 1}.
    const magazineChars = {}

    for (let letter of magazine) {
        if (!magazineChars[letter]) {
            magazineChars[letter] = 0
        }

        magazineChars[letter] += 1
    }

    // Go through all the characters in ransom note and check if that letter exists in the hashmap and that the count is greater than 0.
    for (let letter of ransomNote) {
        if (magazineChars[letter]) {
            magazineChars[letter] -= 1
        } else {
            return false
        }
    }

    // If we go through all of the characters in "magazine" without returning false, then this means that we had enough letters and so we can return true.
    return true
};