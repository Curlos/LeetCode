class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        validArr = []
        parentheses = []
        
        for i, char in enumerate(s):
            if char == '(':
                parentheses.append(['(', i])
                validArr.append(0)
            elif char == ')':
                if len(parentheses) != 0 and parentheses[-1][0] == '(':
                    openPar = parentheses.pop()
                    openParIdx = openPar[1]
                    validArr[openParIdx] = '('
                    validArr.append(')')
                else:
                    validArr.append(0)
            else:
                validArr.append(char)
        
        result = []
        
        for char in validArr:
            if char != 0:
                result.append(char)
        
        return "".join(result)