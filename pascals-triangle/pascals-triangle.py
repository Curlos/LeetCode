class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        pascalRows = [[1]]
        
        for _ in range(1, numRows):
            prevRow = pascalRows[len(pascalRows) - 1]
            newRow = [1]
            
            for i in range(len(prevRow) - 1):
                newNum = prevRow[i] + prevRow[i + 1]
                newRow.append(newNum)
            
            newRow.append(1)
            pascalRows.append(newRow)
        
        return pascalRows