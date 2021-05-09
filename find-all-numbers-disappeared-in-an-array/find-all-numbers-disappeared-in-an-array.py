class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashNums = {}
        disappearedNums = []
        
        for num in nums:
            if num not in hashNums:
                hashNums[num] = 1
        
        for i in range(1, len(nums) + 1):
            if i not in hashNums:
                disappearedNums.append(i)
        
        return disappearedNums