class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hashS = {}
        oddCount = 0
        
        for letter in s:
            if letter not in hashS:
                hashS[letter] = 0
            hashS[letter] += 1
        
        for letter, count in hashS.items():
            if count % 2 != 0:
                if oddCount == 0:
                    oddCount += 1
                else:
                    return False
        
        return True