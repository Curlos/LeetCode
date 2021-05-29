class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashS = {}
        
        for char in s:
            if char not in hashS:
                hashS[char] = 0
            hashS[char] += 1
        
        for i, char in enumerate(s):
            if hashS[char] == 1:
                return i
        
        return -1