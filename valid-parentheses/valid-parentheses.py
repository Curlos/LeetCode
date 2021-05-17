class Solution:
    def isValid(self, s: str) -> bool:
        openPar = ['(', '{', '[']
        hashPar = {')': '(', '}': '{', ']': '['}
        stackPar = []
        
        for char in s:
            if char in openPar:
                stackPar.append(char)
            elif char in hashPar:
                if len(stackPar) == 0:
                    return False
                if stackPar[-1] == hashPar.get(char):
                    stackPar.pop()
                else:
                    return False
        
        if stackPar:
            return False
        return True