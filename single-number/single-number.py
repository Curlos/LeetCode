class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashNums = {}
        
        for num in nums:
            if num not in hashNums:
                hashNums[num] = 0
            hashNums[num] += 1
        
        for num, freq in hashNums.items():
            if freq == 1:
                return num