class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        
        print(s)
        print(t)
        
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        
        return True