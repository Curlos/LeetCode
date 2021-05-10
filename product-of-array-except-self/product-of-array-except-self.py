class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        product = 1
        
        for num in nums:
            products.append(product)
            product *= num
        
        product = 1
        
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= product
            product *= nums[i]
        
        return products