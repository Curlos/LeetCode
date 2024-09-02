class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        minLen = len(strs[0])
        minWord = strs[0]
        i = 0
        
        for word in strs:
            if len(word) < minLen:
                minLen = len(word)
                minWord = word
        
        while i < len(strs):
            word = strs[i]
            
            if word[:minLen] != minWord:
                minWord = minWord[:minLen - 1]
                minLen -= 1
                i = 0
            else:
                i += 1
        
        if i == len(strs):
            return minWord
        else:
            return ""