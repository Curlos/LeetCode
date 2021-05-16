class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 1
        
        for i in range(len(nums) - 1, -1, -1):
            if j == k:
                return nums[i]
            j += 1