class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashStr = {}
        
        for char in s:
            if char not in hashStr:
                hashStr[char] = 0
            hashStr[char] += 1
        
        for char in t:
            if char not in hashStr:
                return False
            if hashStr[char] < 1:
                return False
            
            hashStr[char] -= 1
        
        return True