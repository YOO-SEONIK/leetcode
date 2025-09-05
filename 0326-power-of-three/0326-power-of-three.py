class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        if n == 1:
            return True
        else:    
          while 3**i <= n:
              i +=1
              if 3**i == n:
                  return True
          return False        
        