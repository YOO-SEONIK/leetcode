class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n <= 0:
            return False
        else:
            i = 0
            while 2**i < n:
                i +=1
                if n == 2**i:
                    return True
                    break
            return False        

        
        