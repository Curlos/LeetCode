class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        
        def binaryToInt(binaryNum):
            totalSum = 0
            powerCount = 0
            
            for i in range(len(binaryNum) - 1, -1, -1):
                num = binaryNum[i]
                
                if num == '1':
                    totalSum += 2 ** powerCount
                    
                powerCount += 1
                
            return totalSum
        
        def intToBinary(intNum):
            if(intNum == 1):
                return "1"
            stack1 = []
            binaryArr = []
            
            while intNum > 1:
                if intNum % 2 == 0:
                    stack1.append('0')
                else:
                    stack1.append('1')
                    
                intNum = intNum // 2
            stack1.append('1')
            
            while len(stack1) > 0:
                binaryArr.append(stack1.pop())
            return "".join(binaryArr)

        num1 = binaryToInt(a)
        num2 = binaryToInt(b)
        num3 = num1 + num2
        return intToBinary(num3)