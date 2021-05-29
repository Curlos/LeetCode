class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashNums = {}
        
        for i, num in enumerate(arr):
            if num not in hashNums:
                hashNums[num] = i
        
        for i, num in enumerate(arr):
            if num * 2 in hashNums and hashNums[num * 2] != i:
                return True
        
        return False