class Solution:
    def grayCode(self, n: int) -> List[int]:
        ret = [0]
        for i in range(n):
            ret += [x + pow(2, i) for x in reversed(ret)]
        return ret
        