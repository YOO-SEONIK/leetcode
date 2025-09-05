class Solution:
    def fib(self, n: int) -> int:
        fi = [0]*31
        fi[1] = 1
        
        for idx in range(2, n+1):
            fi[idx] = fi[idx-1] + fi[idx-2]
            
        return fi[n]
        