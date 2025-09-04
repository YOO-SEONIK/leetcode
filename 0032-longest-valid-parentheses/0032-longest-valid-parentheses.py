class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stck = [-1]
        cnt = 0

        for ind, ch in enumerate(s):
            if ch == '(':
                stck.append(ind)
            else:
                stck.pop()
                if not stck:
                    stck.append(ind)
                else:
                    cnt = max(cnt, ind - stck[-1])

        return cnt
        