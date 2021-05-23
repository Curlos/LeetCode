class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStrHash = {}
        maxSubStr = []
        currSubStrStart = 0
        idx = 0
        
        while idx < len(s):
            char = s[idx]
            
            if idx == len(s) - 1 and char not in subStrHash:
                subStrHash[char] = char
                
            
            if char in subStrHash or idx == len(s) - 1:
                if len(subStrHash.keys()) > len(maxSubStr):
                    maxSubStr = subStrHash.keys()
                    
                subStrHash = {}
                currSubStrStart += 1
                idx = currSubStrStart
            else:
                subStrHash[char] = char
                idx += 1
                
        return len(maxSubStr)