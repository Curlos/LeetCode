class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        hashAnagram = {}
        
        for char in s:
            if char in hashAnagram:
                hashAnagram[char] += 1
            else:
                hashAnagram[char] = 1
        
        for char in t:
            if char not in hashAnagram or hashAnagram[char] <= 0:
                return False
            hashAnagram[char] -= 1
        
        return True
        