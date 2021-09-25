class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashStr = {}
        
        for char in magazine:
            if char not in hashStr:
                hashStr[char] = 0
            hashStr[char] += 1
        
        for char in ransomNote:
            if char not in hashStr:
                return False
            if hashStr[char] < 1:
                return False
            hashStr[char] -= 1
        
        return True