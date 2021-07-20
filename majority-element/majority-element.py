class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashElems = {}
        
        for elem in nums:
            if elem not in hashElems:
                hashElems[elem] = 0
            hashElems[elem] += 1
        
        for elem in hashElems:
            if hashElems[elem] > len(nums) / 2:
                return elem