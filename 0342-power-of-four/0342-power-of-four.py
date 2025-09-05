class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i=0
        if n == 1:
            return True
        else:    
            while 4**i <= n:
              i +=1
              if 4**i ==n:
                return True
            return False        
        