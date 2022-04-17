class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        for i in range(len(nums) - 1):
            currNum = nums[i]
            nextNum = nums[i + 1]
            
            if currNum == nextNum:
                return True
            
        return False