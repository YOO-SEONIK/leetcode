class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        n = columnNumber
        while n > 0:
            n -= 1
            result = chr(n % 26 + ord('A')) + result
            n //= 26
        return result
        