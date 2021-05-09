class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashNums = {}
        
        for num in nums:
            if num in hashNums:
                return True
            hashNums[num] = 1
        
        return False