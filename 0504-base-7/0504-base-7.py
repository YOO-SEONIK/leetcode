class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return str(num)
        
        sign = 1 
        if num < 0:
            sign = -1
            
        num = abs(num)
        answer = ''
        
        while num:
            answer = str(num % 7) + answer
            num //= 7
            
        return ('-' if sign < 0 else '') + answer
        