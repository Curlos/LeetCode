class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashNums = {}
        intersection = []
        
        for num in nums1:
            if num not in hashNums:
                hashNums[num] = 0
            hashNums[num] += 1
        
        for num in nums2:
            if num in hashNums:
                if hashNums[num] > 0:
                    hashNums[num] -= 1
                    intersection.append(num)
        
        return intersection