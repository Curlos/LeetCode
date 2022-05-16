class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashNums = {}
        
        for i, num1 in enumerate(nums):
            num2 = target - num1
            
            if num2 in hashNums:
                return [i, hashNums[num2]]
            
            hashNums[num1] = i