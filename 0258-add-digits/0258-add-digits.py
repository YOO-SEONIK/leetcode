class Solution:
    def addDigits(self, num: int) -> int:
        if num > 9:
            t_num = 0
            for n in str(num):
                t_num += int(n)
                if t_num > 9:
                    t_num = t_num%10 + t_num//10
                    
            num = t_num
            
        return num
        