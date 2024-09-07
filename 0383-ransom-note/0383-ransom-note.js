/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    // Sort both "ransomNote" and "magazine"
    const ransomNoteArr = ransomNote.split('').sort()
    const magazineArr = magazine.split('').sort()

    // Setup two pointers: one for "ransomNote" and one for "magazine"
    let ransomNotePointer = 0
    let magazinePointer = 0

    // Using the two pointers go through the letters in ransom note in the sorted order of letters

    // "aa"    "aab"
    while (ransomNotePointer < ransomNoteArr.length && magazinePointer < magazineArr.length) {
        if (ransomNoteArr[ransomNotePointer] === magazineArr[magazinePointer]) {
            ransomNotePointer++
            magazinePointer++
        } else {
            magazinePointer++
        }
        
    }

    const foundAllLetters = ransomNotePointer >= ransomNoteArr.length ? true : false
    return foundAllLetters
};