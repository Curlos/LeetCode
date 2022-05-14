class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashNums = {}
        
        for num in nums:
            if num in hashNums:
                return True
            hashNums[num] = True
        
        return False