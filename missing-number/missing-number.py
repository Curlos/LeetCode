class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        
        for num in nums:
            if num != count:
                return count
            count += 1
        
        return count