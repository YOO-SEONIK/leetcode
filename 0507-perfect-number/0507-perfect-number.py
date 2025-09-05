class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1: 
            return False
        my_sum = 1
        for i in range(2, int(num**0.5 + 1)):
            if num % i == 0:
                my_sum = my_sum + i + num / i
        return num == my_sum
        