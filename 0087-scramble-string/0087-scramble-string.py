from functools import lru_cache
from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):  # 강력한 프루닝
            return False

        @lru_cache(None)
        def dfs(a: str, b: str) -> bool:
            if a == b:
                return True
            if Counter(a) != Counter(b):  # 부분문자열 차원 프루닝
                return False

            n = len(a)
            for k in range(1, n):
                # 미스왑
                if dfs(a[:k], b[:k]) and dfs(a[k:], b[k:]):
                    return True
                # 스왑
                if dfs(a[:k], b[n-k:]) and dfs(a[k:], b[:n-k]):
                    return True
            return False

        return dfs(s1, s2)
