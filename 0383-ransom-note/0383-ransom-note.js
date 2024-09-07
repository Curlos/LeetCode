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

    // Go through all the characters in ransom note and first check if that letter exists in the magazine hashmap. SECONDLY, check that there's enough of that letter left. Meaning the letter MUST EXIST and HAVE A COUNT GREATER THAN OR EQUAL TO 1 left. If it's at 0, then we've used all of that letter and the "ransomNote" cannot be re-created from "magazine". If at any point, one of these conditions do not pass, then return false.
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