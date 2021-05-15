class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            low = 0
            high = len(row) - 1
            
            while low <= high:
                mid = low + (high - low) // 2
                
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    low = mid + 1
                elif row[mid] > target:
                    high = mid - 1
        
        return False