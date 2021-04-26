class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNums = {}
        
        for i, num in enumerate(nums):
            y = target - num
            
            if y in hashNums and hashNums[y] != i:
                return [hashNums[y], i]
            
            hashNums[num] = i