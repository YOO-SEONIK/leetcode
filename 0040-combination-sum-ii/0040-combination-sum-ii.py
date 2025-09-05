class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(idx, cur, total):
            if total > target:
                return 
            if total == target:
                ans.append(cur.copy())

            prev = -1
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                dfs(i+1, cur, total+candidates[i])
                cur.pop()

                prev = candidates[i]

        dfs(0, [], 0)

        return ans
        