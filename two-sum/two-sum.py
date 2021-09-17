class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNums = {}
        
        for i, num in enumerate(nums):
            numToFind = target - num
            
            if numToFind in hashNums:
                return [hashNums[numToFind], i]
        
            hashNums[num] = i
        
        return []