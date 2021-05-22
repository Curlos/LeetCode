class Solution:
    def reverse(self, x: int) -> int:
        if x < 10. and x > -10:
            return x
        
        isNegative = False
        
        if x < 0:
            isNegative = True
            x *= -1
        
        xInt = 0
        
        while x != 0:
            pop = x % 10
            x = x // 10
            xInt = xInt * 10 + pop
            
            if xInt < (-2 ** 31) or xInt > (2 **31) - 1:
                return 0
        
        if isNegative:
            return xInt * -1
        
        return xInt