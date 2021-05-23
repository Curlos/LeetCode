class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        tripletsHash = {}
        nums.sort()
        
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                tripleSum = nums[i] + nums[j] + nums[k]
                
                if i != j and i != k and j != k:
                    if tripleSum == 0:
                        tripletsTuple = (nums[i], nums[j], nums[k])
                        
                        if tripletsTuple not in tripletsHash:
                            triplets.append([nums[i], nums[j], nums[k]])
                            tripletsHash[tripletsTuple] = -1
                
                if tripleSum > 0:
                    k -= 1
                elif tripleSum < 0:
                    j += 1
                else:
                    k -= 1

        
        return triplets