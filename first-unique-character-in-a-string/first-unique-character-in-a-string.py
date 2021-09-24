class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashChar = {}
        
        for char in s:
            if char not in hashChar:
                hashChar[char] = 0
            hashChar[char] += 1
        
        for i, char in enumerate(s):
            if hashChar[char] == 1:
                return i
        
        return -1