from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []

        def backtrack(i: int, cnt: int, path: List[str]):
            
            rem = n - i
            blocks = 4 - cnt
            if rem < blocks or rem > 3 * blocks:
                return

            if cnt == 4 and i == n:
                res.append(".".join(path))
                return
            if cnt == 4:
                return

            
            for l in range(1, 4):
                if i + l > n:
                    break
                seg = s[i:i+l]

                
                if seg[0] == '0' and l > 1:
                    continue
                
                if int(seg) > 255:
                    continue

                path.append(seg)
                backtrack(i + l, cnt + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return res
        