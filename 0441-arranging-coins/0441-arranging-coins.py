class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        row = 1
        while n > 0:
            n -= row
            row += 1

            ans += 1
            

        if n < 0:
            return ans - 1
        
        return ans
