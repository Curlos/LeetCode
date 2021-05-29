class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = {}
        sumUnique = 0
        
        for num in nums:
            if num not in counter:
                counter[num] = 0
            
            counter[num] += 1
        
        for num in nums:
            if counter[num] == 1:
                sumUnique += num
        
        return sumUnique