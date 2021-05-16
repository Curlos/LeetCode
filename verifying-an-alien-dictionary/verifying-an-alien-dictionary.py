class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letters = {letter: i for i, letter in enumerate(order)}
        new_words = [[letters[letter] for i, letter in enumerate(word)] for word in words]
        return all(w1 <= w2 for w1, w2 in zip(new_words, new_words[1:]))