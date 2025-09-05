class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(n):
            if n == 1:
                return 1
            return n * factorial(n-1)
        nums = [str(i) for i in range(1, n+1)]
        if k == 1:
            return ''.join(nums)
        k -= 1
        ret = ''
        while k > 0:
            x = factorial(n-1)
            if k >= x:
                quotient = k // x
                k -= quotient * x
                ret += nums.pop(quotient)
            else:
                ret += nums.pop(0)
            n -= 1
        ret += ''.join(nums)
        return ret
        