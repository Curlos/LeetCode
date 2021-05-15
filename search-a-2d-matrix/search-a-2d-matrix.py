class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        
        for row in matrix:
            if row[-1] >= target:
                arr = row
                break
        
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
        
        return False