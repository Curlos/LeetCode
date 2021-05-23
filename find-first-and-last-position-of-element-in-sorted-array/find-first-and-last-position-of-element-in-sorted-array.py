class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        startEnd = [-1, -1]
        
        for i, num in enumerate(nums):
            if num == target and startEnd[0] == -1:
                startEnd[0] = i
            if num == target and i == len(nums) - 1 or num == target and nums[i + 1] != target:
                startEnd[1] = i
        
        return startEnd