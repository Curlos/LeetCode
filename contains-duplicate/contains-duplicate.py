class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashNums = {}
        
        for num in nums:
            if num not in hashNums:
                hashNums[num] = num
            else:
                return True
        
        return False